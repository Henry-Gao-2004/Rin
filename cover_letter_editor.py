from utils import prompt_gpt

def generate_cover_letter(company: str, position: str):
    """
    Generate a cover letter for a given company and position using a template and resume.
    company: str, the name of the company
    position: str, the position to apply for
    return: tuple(bool, str), (status, cover_letter or error message)
    """
    with open("data/cover_letter_template.txt", "r") as file:
        cover_letter_template = file.read()
    with open("data/resume.txt", "r") as file:
        resume = file.read()
    prompt = "Here is my resume: \n"+resume+"\nHere is a cover_letter template: \n"+cover_letter_template+"\n Generate a cover for the position "+position+" at "+company+" using the template and my resume."
    status, response = prompt_gpt(prompt)
    if status:
        return True, response
    else:
        return False, response