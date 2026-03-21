import re
from sentence_transformers import SentenceTransformer
from docx import Document

class DocParser:
    def __init__(self, model_name="dragonkue/BGE-m3-ko"):
        self.model = SentenceTransformer(model_name, device="cuda")

    def read_docx(self, path):
        doc = Document(path)
        paragraphs = [p.text.strip() for p in doc.paragraphs if p.text.strip()]
        return paragraphs
    
    def chunk_by_article(self, paragraphs):
        chunks = []
        current_chunk = ""
        status = "current"

        for p in paragraphs:

             # 조 시작
            if re.match(r"제\s*\d+\s*조", p):
                if current_chunk:
                    chunks.append(current_chunk.strip())
                current_chunk = p

            else:
                current_chunk += "\n" + p

        if current_chunk:
            chunks.append(current_chunk.strip())

        head = chunks[0].splitlines()[0]
        # Regex to capture statute and abbreviation
        m = re.match(r"^(.*?)\s*\(\s*약칭:\s*(.*?)\s*\)\s*$", head)
        if m:
            statute = m.group(1)
            abbreviation = m.group(2)
        else:
            statute = head
            abbreviation = None

        processed_chunks = []

        for chunk in chunks:
            match = re.search(r"\[시행일:\s*(.*?)\]", chunk)

            if match:
                status = "future"
                effective_date = match.group(1).strip()
                effective_date = effective_date.replace(". ", "-")
                effective_date = effective_date.replace(".", "")
            else:
                status = "current"
                effective_date = None

            processed_chunks.append({
                "text": chunk,
                "status": status,
                "effective_date": effective_date
            })

        return statute, abbreviation, processed_chunks
    
    def parse_article(self, statute, abbreviation, article):

        article_text = article["text"]
        status = article["status"]
        effective_date = article["effective_date"]
        
        # 조 번호 + 제목 추출
        match = re.match(r"(제\s*\d+\s*조(?:의\s*\d+)?)\s*\(([^)]+)\)", article_text)

        # 삭제된 조는 패턴에 맞지 않으므로 None 반환
        if not match:
            return None
        
        article_text = re.sub(r"\<\s*.*?(개정|신설|이동).*?\>", "", article_text, flags=re.DOTALL)

        article_text = re.sub(r"\[\s*.*?(본조|개정|신설|이동).*?\]", "", article_text, flags=re.DOTALL)

        article_text = re.sub(r"\[시행일:.*?\]\s*(?:\n\s*)?제\s*\d+조(?:의\d+)?", "", article_text)

        article_num = match.group(1)
        title = match.group(2)

        body = article_text[match.end():].strip()

        return {
            "statute": statute,
            "abbreviation": abbreviation,
            "article": article_num,
            "title": title,
            "body": body,
            "status": status,
            "effective_date": effective_date    
        }

    def parse_qa(self, text):
        pattern = r"(Q[:：].*?)(A[:：].*?)(?=Q[:：]|$)"
        matches = re.findall(pattern, text, re.DOTALL)

        qa_pairs = []
        for q, a in matches:
            q = re.sub(r"Q[:：]\s*", "", q).strip()
            a = re.sub(r"A[:：]\s*", "", a).strip()
            qa_pairs.append((q, a))

        return qa_pairs

    def embed(self, text):
        emb = self.model.encode(text, normalize_embeddings=True, device="cuda")
        return emb