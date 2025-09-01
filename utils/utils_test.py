from utils import prompt_gpt


def prompt_gpt_test():
    prompt = "What is the capital of France?"
    response = prompt_gpt(prompt)
    print(response)


if __name__ == "__main__":
    prompt_gpt_test()