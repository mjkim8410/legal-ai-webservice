from qwen import Qwen

if __name__ == "__main__":
    qwen = Qwen()
    user_query = ""
    response = qwen.answer_query(user_query)
    print(response)
