from mistral_inference.transformer import Transformer
from mistral_inference.generate import generate

from mistral_common.tokens.tokenizers.mistral import MistralTokenizer
from mistral_common.protocol.instruct.messages import UserMessage
from mistral_common.protocol.instruct.request import ChatCompletionRequest
from query_db import query  

class Mistral:
    def __init__(self):
        self.mistral_models_path = 'mistral_models/7B-Instruct-v0.3'
        self.tokenizer = MistralTokenizer.from_file(f"{self.mistral_models_path}/tokenizer.model.v3")
        self.model = Transformer.from_folder(self.mistral_models_path)

    def answer_query(self, user_query):

        with open("system_prompt.txt") as f:
            system_prompt = f.read()

        context = query(user_query)

        prompt = f"""
            {system_prompt}

            문맥:
            {context}

            질문:
            {user_query}

            답변:
            """

        completion_request = ChatCompletionRequest(
            messages=[
                UserMessage(content=prompt)
            ]
        )

        tokens = self.tokenizer.encode_chat_completion(completion_request).tokens

        out_tokens, _ = generate([tokens], self.model, max_tokens=1024, temperature=0.1, eos_id=self.tokenizer.instruct_tokenizer.tokenizer.eos_id)
        decoded = self.tokenizer.instruct_tokenizer.tokenizer.decode(out_tokens[0])

        answer = decoded.split("Answer:")[-1].strip()

        return answer

