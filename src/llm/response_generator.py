from .prompt_templates import qa_prompt

def generate(llm, context, query):
    return llm.generate(qa_prompt(context, query))
