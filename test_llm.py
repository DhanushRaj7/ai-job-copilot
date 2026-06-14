from llm import llm

response = llm.invoke(
    "Explain what a LangGraph state is in one sentence."
)

print(response.content)