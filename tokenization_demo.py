"""
Tokens and Tokenization Demo for Creoz

This script demonstrates how to count and log the number of tokens used in an AI prompt.
"""

def count_tokens(text):
    """
    Counts the number of tokens in the given text.
    For demonstration, we assume each word is a token (real AI models may use more complex tokenization).
    """
    return len(text.split())

def generate_dynamic_prompt(user_topic, detail_level="concise"):
    """
    Generates a dynamic prompt for the AI tutor based on user input.
    """
    if detail_level == "detailed":
        return f"Explain the topic '{user_topic}' in detail with examples suitable for a high school student."
    else:
        return f"Give a concise summary of '{user_topic}' suitable for a beginner."

# Example usage
if __name__ == "__main__":
    # Simulate user input
    topic = input("Enter a topic you want to learn about: ")
    level = input("Do you want a 'concise' or 'detailed' explanation? ").strip().lower()

    prompt = generate_dynamic_prompt(topic, level)
    print("\nGenerated Dynamic Prompt for AI:")
    print(prompt)

    # Tokenization: count and log tokens
    num_tokens = count_tokens(prompt)
    print(f"\nNumber of tokens in the prompt: {num_tokens}")

    # Video Explanation (for your script):
    # Tokens are the basic units of text that AI models process—often words or word pieces.
    # Tokenization is the process of splitting text into these units.
    # Logging token counts helps monitor and optimize AI usage for correctness,