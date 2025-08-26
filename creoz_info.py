"""
Creoz – AI-Powered Personalized Learning Universe

This module provides information about the Creoz platform and its features.
"""

def get_creoz_features():
    features = {
        "Adaptive AI Learning": [
            "Dynamic study paths tailored to each student’s strengths & weaknesses",
            "Smart quizzes, flashcards, and coding challenges powered by AI",
            "Context-based explanations using real-world analogies"
        ],
        "Immersive 3D Learning Universe": [
            "Explore thematic zones: Math Galaxy, Science Jungle, History Tower",
            "Built using React Three Fiber + Three.js for interactive experiences",
            "Gamified progress with coins, levels, and achievement badges"
        ],
        "AI Notes & Smart Summaries": [
            "Upload PDFs, textbooks, or lecture notes → instant AI-generated summaries",
            "Generate visual mind maps & structured notes",
            "Export content as PDF, Markdown, or flashcards for revision"
        ],
        "Productivity & Focus Hub": [
            "AI-driven Pomodoro Coach with reminders",
            "Productivity tracking dashboard with insights & analytics",
            "Motivational nudges using animations and sounds"
        ],
        "AI Tutor (Chat & Voice)": [
            "24/7 AI tutor for Q&A and doubt solving",
            "Voice-enabled tutoring for hands-free learning",
            "Function-calling for fetching facts, formulas, and examples instantly"
        ]
    }
    return features

def get_tech_stack():
    tech_stack = {
        "Frontend": [
            "Next.js (React Framework)",
            "TailwindCSS + Framer Motion (UI + animations)",
            "Three.js + React Three Fiber (3D environments)"
        ],
        "Backend": [
            "Node.js + Express.js (APIs & authentication)",
            "MongoDB (user data, notes, progress, quizzes)"
        ],
        "AI & Data": [
            "OpenAI GPT APIs (tutoring, summarization, quizzes)",
            "RAG (Retrieval-Augmented Generation) with Wikipedia & academic datasets"
        ],
        "Deployment": [
            "Vercel (Frontend)",
            "Render / Railway / Heroku (Backend)"
        ]
    }
    return tech_stack

if __name__ == "__main__":
    print("Creoz – AI-Powered Personalized Learning Universe\n")
    print("Features:")
    for section, items in get_creoz_features().items():
        print(f"\n{section}:")
        for item in items:
            print(f"  - {item}")
    print("\nTech Stack:")
    for section, items in get_tech_stack().items():
        print(f"\n{section}:")
        for item in items:    
             print(f"  - {item}")