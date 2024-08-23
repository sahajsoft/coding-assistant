import ollama

def gen_embeddings(value: str, embedding_model: str) -> str | None:
    """

    """
    try:
        response = ollama.embeddings(model=embedding_model, prompt=value)
    except Exception as e:
        print(f"failed to generate embedding for {value}: {e}")
        return None
    embedding = response["embedding"]
    return embedding
