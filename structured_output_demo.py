"""
Structured Output Demo for Creoz

This script demonstrates how to implement structured output in an AI call.
"""

import random

def mock_ai_call_structured(prompt, top_p=0.9, temperature=0.7, top_k=3):
    """
    Simulates an AI call that returns structured output (as a dictionary).
    Args:
        prompt (str): The prompt to send to the AI.
        top_p (float): The Top P (nucleus sampling) value.
        temperature (float): The Temperature value.
        top_k (int): The Top K value.
    Returns:
        dict: Simulated structured AI response.
    """
    responses = [
        {
            "type": "creative",
            "summary": f"Here's a creative answer to '{prompt}'.",
            "confidence": random.uniform(0.7, 0.95)
        },
        {
            "type": "factual",
            "summary": f"This is a factual summary for '{prompt}'.",
            "confidence": random.uniform(0.9, 1.0)
        },
        {
            "type": "alternative",
            "summary": f"An alternative perspective on '{prompt}'.",
            "confidence": random.uniform(0.6, 0.85)
        }
    ]
    available_responses = responses[:max(1, min(top_k, len(responses)))]
    if temperature >= 0.8:
        result = random.choice(available_responses)
    elif temperature <= 0.3:
        result = available_responses[0]
    else:
        result = available_responses[-1]
    # Add metadata for demonstration
    result["parameters"] = {
        "top_p": top_p,
        "temperature": temperature,
        "top_k": top_k
    }
    return result

if __name__ == "__main__":
    prompt = input("Enter your AI prompt: ")
    try:
        top_p = float(input("Enter Top P value (0.0 - 1.0): "))
    except ValueError:
        top_p = 0.9
    try:
        temperature = float(input("Enter Temperature value (0.0 - 1.0): "))
    except ValueError:
        temperature = 0.7
    try:
        top_k = int(input("Enter Top K value (1 - 3): "))
    except ValueError:
        top_k = 3

    response = mock_ai_call_structured(prompt, top_p=top_p, temperature=temperature, top_k=top_k)
    print(f"\nStructured AI Response:\n{response}")

    # Video Explanation (for your script):
    # Structured output means the AI returns data in a predictable format, like a dictionary or JSON.
    # This makes it easier for applications to parse, display, and use the results programmatically.
    # Structured output improves correctness, efficiency, and scalability for LLM