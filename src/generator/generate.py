from src.retrievers.retrieve import retrieve_chunks
from src.chains.flash_card_chain import get_flashcard_chain
from langchain.schema import BaseMessage, AIMessage
import re


def _extract_text_from_result(result) -> str:
    """
    Normalize the chain.invoke result into a plain string.
    Handles dict outputs, AIMessage, and BaseMessage types.
    """
    if isinstance(result, dict):
        val = next(iter(result.values()))
    else:
        val = result
    if isinstance(val, (AIMessage, BaseMessage)) and hasattr(val, "content"):
        return val.content
    return str(val)


def parse_qa_pairs(text: str) -> list[tuple[str, str]]:
    """
    Parse raw LLM output into a list of (question, answer) pairs.
    """
    pairs = re.findall(r"Q:\s*(.*?)\s*A:\s*(.*?)(?=\nQ:|\Z)", text, flags=re.DOTALL)
    return [(q.strip(), a.strip()) for q, a in pairs]


def generate_flashcards_for_topics(topics: list[str], k: int = 5) -> list[dict]:
    """
    Generate flashcards for each topic by retrieving relevant chunks and
    invoking the flashcard generation chain. Returns a list of dicts with keys: topic, question, answer.
    """
    chain = get_flashcard_chain()
    all_cards = []
    for topic in topics:
        snippets = "\n\n".join(doc.page_content for doc in retrieve_chunks(topic, k))
        # Invoke chain and normalize output
        result = chain.invoke({"snippets": snippets, "topic": topic})
        text = _extract_text_from_result(result)
        # Parse Q&A pairs
        for q, a in parse_qa_pairs(text):
            all_cards.append({"topic": topic, "question": q, "answer": a})
    return all_cards