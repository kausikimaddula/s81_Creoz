"""
Top P (Nucleus Sampling) Demo for Creoz

This script demonstrates how to set the Top P parameter in an AI call.
"""

import random

def mock_ai_call(prompt, top_p=0.9):
    """
    Simulates an AI call with a configurable Top P parameter.
    Args:
        prompt (str): The prompt to send to the AI.
        top_p (float): The Top P (nucleus sampling) value for controlling randomness.
    Returns:
        str: Simulated AI response.
    """
    # For demonstration, we'll just return a string showing the top_p value.
    # In a real scenario, this would be passed to the LLM API (e.g., OpenAI, Cohere, etc.)
    responses = [
        f"Here's a creative answer to '{prompt}'.",
        f"This is a factual summary for '{prompt}'.",
        f"An alternative perspective on '{prompt}'."
    ]
    # Simulate randomness: higher top_p means more creative/random response
    if top_p >= 0.9:
        return random.choice(responses)
    else:
        return responses[1]  # More deterministic

if __name__ == "__main__":
    prompt = input("Enter your AI prompt: ")
    try:
        top_p = float(input("Enter Top P value (0.0 - 1.0): "))
    except ValueError:
        top_p = 0.9  # Default

    response = mock_ai_call(prompt, top_p=top_p)
    print(f"\nAI Response (Top P={top_p}):")
    print(response)

    # Video Explanation (for your script):
    # Top P (nucleus sampling) is a parameter that controls the diversity of AI-generated text.
    # A higher Top P allows the model to consider more possible next words, making responses more creative.
    # A lower Top P makes the output more focused and deterministic.
    # Adjusting Top P helps balance correctness, efficiency, and scalability in LLM-powered