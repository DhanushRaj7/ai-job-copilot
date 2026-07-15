"""Manual smoke test for the LLM connection (NOT run by pytest/CI).

Requires a real GROQ_API_KEY in your environment or .env. Run it by hand to
confirm the Groq/Llama model is reachable:

    python examples/smoke_llm.py
"""

from llm import llm

if __name__ == "__main__":
    response = llm.invoke("Explain what a LangGraph state is in one sentence.")
    print(response.content)
