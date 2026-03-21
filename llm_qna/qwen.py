from transformers import AutoModelForCausalLM, AutoTokenizer
from query_db import query

class Qwen:
    def __init__(self):
        self.model_name = "Qwen/Qwen2.5-7B-Instruct"
        self.tokenizer = AutoTokenizer.from_pretrained(self.model_name)
        self.model = AutoModelForCausalLM.from_pretrained(self.model_name,torch_dtype="auto",device_map="auto")
    
    def answer_query(self, user_query):

        with open("system_prompt.txt", encoding="utf-8") as f:
            system_prompt = f.read()

        context = query(user_query)

        prompt = f"""
            {system_prompt}

            참고조항:
            {context}

            질문:
            {user_query}

            답변:
            """

        messages = [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": prompt}
        ]
        text = self.tokenizer.apply_chat_template(
            messages,
            tokenize=False,
            add_generation_prompt=True
        )
        model_inputs = self.tokenizer([text], return_tensors="pt").to(self.model.device)

        generated_ids = self.model.generate(
            **model_inputs,
            max_new_tokens=512
        )
        generated_ids = [
            output_ids[len(input_ids):] for input_ids, output_ids in zip(model_inputs.input_ids, generated_ids)
        ]

        response = self.tokenizer.batch_decode(generated_ids, skip_special_tokens=True)[0]
        return response

