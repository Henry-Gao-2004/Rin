from utils import prompt_gpt, response_to_text


def prompt_gpt_test():
    prompt = "What is the capital of France?"
    response = prompt_gpt(prompt)
    print(response)

def response_to_text_test():
    prompt = "What is the capital of France?"
    response = prompt_gpt(prompt)
    text_response = response_to_text(response)
    print(text_response)


if __name__ == "__main__":
    prompt_gpt_test()