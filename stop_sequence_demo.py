"""
Stop Sequence Demo for Creoz

This script demonstrates how to implement a stop sequence in an AI call.
"""

import random

def mock_ai_call_with_stop(prompt, stop_sequence=None, top_p=0.9, temperature=0.7, top_k=3):
    """
    Simulates an AI call that stops generating output when a stop sequence is encountered.
    Args:
        prompt (str): The prompt to send to the AI.
        stop_sequence (str or None): The sequence at which to stop generation.
        top_p (float): The Top P value.
        temperature (float): The Temperature value.
        top_k (int): The Top K value.
    Returns:
        str: Simulated AI response, stopped at the stop sequence if present.
    """
    # Simulated possible completions
    completions = [
        f"Here's a creative answer to '{prompt}'. END",
        f"This is a factual summary for '{prompt}'. [STOP]",
        f"An alternative perspective on '{prompt}'. <END>"
    ]
    available_completions = completions[:max(1, min(top_k, len(completions)))]
    if temperature >= 0.8:
        response = random.choice(available_completions)
    elif temperature <= 0.3:
        response = available_completions[0]
    else:
        response = available_completions[-1]

    # Implement stop sequence logic
    if stop_sequence and stop_sequence in response:
        response = response.split(stop_sequence)[0].strip()
    return response

if __name__ == "__main__":
    prompt = input("Enter your AI prompt: ")
    stop_sequence = input("Enter a stop sequence (e.g., END, [STOP], <END>): ").strip()
    stop_sequence = stop_sequence if stop_sequence else None
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

    response = mock_ai_call_with_stop(
        prompt, stop_sequence=stop_sequence, top_p=top_p, temperature=temperature, top_k=top_k
    )
    print(f"\nAI Response (stopped at '{stop_sequence}'):\n{response}")

    # Video Explanation (for your script):
    # A stop sequence is a string that tells the AI model when to stop generating further output.
    # This is useful for controlling response length and ensuring outputs end at logical points.
    # Stop sequences improve correctness, efficiency, and scalability in LLM-powered