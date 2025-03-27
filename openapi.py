import os
from openai import OpenAI
from dotenv import load_dotenv
load_dotenv()
# Load API key from environment variable
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
if not OPENAI_API_KEY:
    raise ValueError("Missing OpenAI API Key. Set OPENAI_API_KEY as an environment variable.")

client = OpenAI(api_key=OPENAI_API_KEY)

# Predefined questions and responses
predefined_responses = {
    "who is siddhesh": "Siddhesh Somvanshi is a Data Engineer Intern at Altysys with experience in software development, AI, and project management.",
    "tell me about siddhesh": "Siddhesh is a skilled software developer with expertise in React.js, Python, SQL, Machine Learning, and more.",
    "his skills": "Siddhesh's skills include React.js, Python, SQL, Databricks Lakehouse, Delta Lake, PySpark, and Agile methodologies.",
    "his work experience": "He has worked as a Project Team Leader at VishvaConnect, Software Developer Intern at VishvaConnect & Incronix Technology, and is currently a Data Engineer Intern at Altysys.",
    "download siddhesh cv": "You can download Siddhesh's CV from: [Insert CV URL Here]"
}

def chatbot():
    while True:
        user_message = input("You: ").strip().lower()
        
        if user_message in ["exit", "quit", "bye"]:
            print("Chatbot: Goodbye!")
            break
        
        # Check if question is predefined
        if user_message in predefined_responses:
            print(f"Chatbot: {predefined_responses[user_message]}")
            continue
        
        # Use OpenAI API for custom queries
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": user_message}]
        )
        
        print(f"Chatbot: {response.choices[0].message.content}")

if __name__ == "__main__":
    chatbot()
