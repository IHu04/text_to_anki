from langchain.chat_models import init_chat_model
from langchain.prompts import PromptTemplate

def get_flashcard_chain():

    llm = init_chat_model(
        "gemini-2.0-flash",
        model_provider="google_genai",
        temperature=0.3,
    )

    flashcard_prompt = PromptTemplate(
        input_variables=["snippets", "topic"],
        template=(
            "You are an expert creating Anki flashcards.\n"
            "Given these excerpts about {topic}:\n\n"
            "{snippets}\n\n"
            "Generate 3–5 clear Q&A pairs in the format:\n"
            "Q: question here\n"
            "A: answer here"
        )
    )

    return flashcard_prompt | llm