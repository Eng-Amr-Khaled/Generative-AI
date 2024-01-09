from langchain import PromptTemplateCreator

template_creator = PromptTemplateCreator()

# Create a prompt template for translation task
translation_template = template_creator.create_template("Translate the following English text to French: {text}")

# Create a prompt template for summarization task
summarization_template = template_creator.create_template("Summarize the given text: {text}")
