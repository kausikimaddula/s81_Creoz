"""
Embeddings Demo for Creoz

This script demonstrates how to generate embeddings for text within your project.
"""

import numpy as np

def simple_text_embedding(text, embedding_dim=8):
    """
    Generates a simple embedding for the input text.
    (For demonstration: uses character codes and averages them. Real LLMs use neural models.)
    Args:
        text (str): Input text to embed.
        embedding_dim (int): Size of the embedding vector.
    Returns:
        np.ndarray: Embedding vector.
    """
    # Convert each character to its Unicode code point
    char_codes = [ord(c) for c in text]
    # Pad or truncate to embedding_dim
    if len(char_codes) < embedding_dim:
        char_codes += [0] * (embedding_dim - len(char_codes))
    else:
        char_codes = char_codes[:embedding_dim]
    # Normalize
    embedding = np.array(char_codes) / 256.0
    return embedding

if __name__ == "__main__":
    text = input("Enter text to generate its embedding: ")
    embedding = simple_text_embedding(text)
    print(f"\nGenerated Embedding Vector:\n{embedding}")

    # Video Explanation (for your script):
    # Embeddings are numerical vector representations of text, computed by LLMs.
    # They capture the semantic meaning of words, sentences, or documents.
    # Embeddings are used for search, clustering, recommendations, and more in AI applications.
    # In production, you would use model APIs (like OpenAI or HuggingFace) to generate high