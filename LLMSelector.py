from langchain import LLMSelector

llm_selector = LLMSelector()
llm_model = llm_selector.select_llm_model("gpt2")
