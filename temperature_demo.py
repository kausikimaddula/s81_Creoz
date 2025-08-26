"""
Temperature Demo for Creoz

This script demonstrates how to set the Temperature parameter in an AI call.
"""

import random

def mock_ai_call(prompt, top_p=0.9, temperature=0.7):
    """
    Simulates an AI call with configurable Top P and Temperature parameters.
    Args:
        prompt (str): The prompt to send to the AI.
        top_p (float): The Top P (nucleus sampling) value for controlling randomness.
        temperature (float): The Temperature value for controlling creativity.
    Returns:
        str: Simulated AI response.
    """
    responses = [
        f"Here's a creative answer to '{prompt}'.",
        f"This is a factual summary for '{prompt}'.",
        f"An alternative perspective on '{prompt}'."
    ]
    # Simulate randomness: higher temperature means more creative/random response
    if temperature >= 0.8:
        return random.choice(responses)
    elif temperature <= 0.3:
        return responses[1]  # More deterministic
    else:
        return responses[0]  # Balanced

if __name__ == "__main__":
    prompt = input("Enter your AI prompt: ")
    try:
        top_p = float(input("Enter Top P value (0.0 - 1.0): "))
    except ValueError:
        top_p = 0.9  # Default
    try:
        temperature = float(input("Enter Temperature value (0.0 - 1.0): "))
    except ValueError:
        temperature = 0.7  # Default

    response = mock_ai_call(prompt, top_p=top_p, temperature=temperature)
    print(f"\nAI Response (Top P={top_p}, Temperature={temperature}):")
    print(response)

    # Video Explanation (for your script):
    # Temperature is a parameter that controls the randomness of AI-generated text.
    # A higher temperature (closer to 1) makes the output more creative and diverse.
    # A lower temperature (closer to 0) makes the output more focused and deterministic.
    # Adjusting temperature helps balance correctness, efficiency, and scalability in LLM-