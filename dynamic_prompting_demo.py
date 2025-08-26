"""
Dynamic Prompting Demo for Creoz

This script demonstrates the concept of dynamic prompting in AI systems.
"""

def generate_dynamic_prompt(user_topic, detail_level="concise"):
    """
    Generates a dynamic prompt for the AI tutor based on user input.

    Args:
        user_topic (str): The topic the user wants to learn about.
        detail_level (str): Level of detail for the explanation ("concise" or "detailed").

    Returns:
        str: A dynamically generated prompt.
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

    # Video Explanation (for your script):
    # Dynamic prompting means creating AI prompts on-the-fly based on user input or context.
    # In this demo, the prompt changes according to the user's chosen topic and detail level.
    # This ensures the AI returns correct, relevant data efficiently for each unique request.
    # The approach is scalable, as prompts are generated programmatically for any number of