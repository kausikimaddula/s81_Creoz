"""
Top K Demo for Creoz

This script demonstrates how to set the Top K parameter in an AI call.
"""

import random

def mock_ai_call(prompt, top_p=0.9, temperature=0.7, top_k=3):
    """
    Simulates an AI call with configurable Top P, Temperature, and Top K parameters.
    Args:
        prompt (str): The prompt to send to the AI.
        top_p (float): The Top P (nucleus sampling) value for controlling randomness.
        temperature (float): The Temperature value for controlling creativity.
        top_k (int): The Top K value for limiting the number of candidate tokens.
    Returns:
        str: Simulated AI response.
    """
    responses = [
        f"Here's a creative answer to '{prompt}'.",
        f"This is a factual summary for '{prompt}'.",
        f"An alternative perspective on '{prompt}'.",
        f"A brief explanation of '{prompt}'.",
        f"An in-depth analysis of '{prompt}'."
    ]
    # Simulate Top K: only consider the top_k most likely responses
    available_responses = responses[:max(1, min(top_k, len(responses)))]
    # Simulate randomness with temperature
    if temperature >= 0.8:
        return random.choice(available_responses)
    elif temperature <= 0.3:
        return available_responses[0]  # Most likely/deterministic
    else:
        return available_responses[-1]  # Balanced

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
    try:
        top_k = int(input("Enter Top K value (1 - 5): "))
    except ValueError:
        top_k = 3  # Default

    response = mock_ai_call(prompt, top_p=top_p, temperature=temperature, top_k=top_k)
    print(f"\nAI Response (Top P={top_p}, Temperature={temperature}, Top K={top_k}):")
    print(response)

    # Video Explanation (for your script):
    # Top K is a parameter that limits the AI's next-token choices to the K most likely options.
    # A lower Top K makes the output more focused and deterministic.
    # A higher Top K allows for more diversity and creativity in responses.
    # Adjusting Top K helps balance correctness, efficiency, and scalability in LLM-powered