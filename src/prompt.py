questions_prompt_template = """
You are an expert at creating questions based on any subject. here I will provide you the chunks of information, your task is to generate questions out of it.
You do this by asking questions about the text below:

------------
{text}
------------

Make sure that your output is the ONLY the python list of questions so that I can further apply python list operations on it.
example : ["question1", "question2","question3"]

QUESTIONS:
"""