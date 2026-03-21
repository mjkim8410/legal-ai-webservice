import requests
import json
from time import sleep

# ===============================
# 1️⃣ 설정
# ===============================
OC = "your_id"  # 사용자 ID, 이메일 앞부분 등
BASE_URL = "https://www.law.go.kr/DRF/lawSearch.do"
OUTPUT_FILE = "data/cases/korean_case_qna.json"

# 가져올 판례 ID 리스트 (예시: 연속 ID)
CASE_IDS = range(228541, 228551)  # 필요에 따라 범위 변경 가능

# ===============================
# 2️⃣ 판례 가져오기 함수
# ===============================
def fetch_case(case_id):
    params = {
        "OC": OC,
        "target": "prec",
        "type": "JSON",
        "query": "개인정보"
    }
    try:
        resp = requests.get(BASE_URL, params=params)
        resp.raise_for_status()
        data = resp.json()
        print(data)
        if "prec" in data:
            return data["prec"][0]  # 판례 정보가 리스트로 들어있음
        else:
            return None
    except Exception as e:
        print(f"[ERROR] case_id={case_id} 실패: {e}")
        return None

# ===============================
# 3️⃣ 판례 → Q&A 변환
# ===============================
def case_to_qa(case_data):
    if not case_data:
        return None

    # 판시사항과 판결요지를 질문/답변으로 변환
    question = case_data.get("판시사항", "").strip()
    answer = case_data.get("판결요지", "").strip()

    if not question or not answer:
        return None

    return {
        "case_id": case_data.get("판례정보일련번호"),
        "question": question,
        "answer": answer,
        "raw": case_data.get("판례내용", "").strip()
    }

# ===============================
# 4️⃣ 전체 스크랩
# ===============================
qna_dataset = []

for case_id in CASE_IDS:
    print(f"Fetching case {case_id}...")
    case_data = fetch_case(case_id)
    print(case_data)
    qa_entry = case_to_qa(case_data)
    if qa_entry:
        qna_dataset.append(qa_entry)
    sleep(0.5)  # 서버 부담 줄이기

# ===============================
# 5️⃣ JSON 저장
# ===============================
with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
    json.dump(qna_dataset, f, ensure_ascii=False, indent=2)

print(f"✅ 완료! {len(qna_dataset)}개의 판례 Q&A를 {OUTPUT_FILE}에 저장했습니다.")