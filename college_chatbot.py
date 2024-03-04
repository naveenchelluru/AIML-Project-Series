# Import necessary libraries
import random
from collections import defaultdict  # Use defaultdict for easier context storage

# Define dictionaries and variables
greetings = ["Hello! Welcome to the College Admission Help Center.", "Hi! How can I help you with your college admission journey today?"]
admission_info = {
    "requirements": "Admission requirements vary based on the college and program you choose. Generally, they include transcripts, standardized test scores, essays, and letters of recommendation.",
    "deadlines": "Application deadlines also vary by college and program. You should always check the college's website for specific deadlines.",
    "procedures": "The admission process typically involves submitting an application form, transcripts, test scores, essays, and other supporting documents.",
    "financial aid": "Financial aid is available in various forms, including scholarships, grants, and loans. You can explore options through the college's financial aid office or government websites.",
}
# Use defaultdict to store context with default values
context = defaultdict(lambda: None)  # Topic: None, Details: None

# Functions for greetings and farewell
def greet():
    print(random.choice(greetings))

def farewell():
    print("Thank you for using the College Admission Help Center. Best of luck with your applications!")

# Function to handle user questions
def answer_questions():
    while True:
        user_input = input("Ask me any college admission questions you have (or type 'exit' to end): ").lower()

        if user_input == "exit":
            break

        # Check for topic-specific follow-up questions
        if context["topic"] and (user_input.startswith("more about") or user_input.startswith("tell me more about")):
            # Provide additional information based on the stored topic
            print(f"Following up on {context['topic']}: {admission_info[context['topic']]}")
            del context["topic"]  # Remove used context

        elif user_input in admission_info.keys():
            # Provide basic answer and potentially set context
            print(admission_info[user_input])
            if user_input in ["financial aid", "programs"]:
                context["topic"] = user_input  # Store the topic for follow-up questions

        elif "college" in user_input and (not context["details"] or "name" not in context["details"]):
            # Extract college name if mentioned and store it for context
            college_name = user_input.split()[1] if len(user_input.split()) > 1 else None
            context["details"] = {"name": college_name}
            print(f"Got it! You mentioned {college_name}. How can I help you regarding {college_name}?")

        else:
            # Handle unknown questions with specific feedback
            if "specific college" in user_input:
                print("While I cannot access specific college information yet, I can provide general advice. Please ask away!")
            else:
                print("I apologize, I don't understand your question. Please try rephrasing or visit the college's website for more details.")

# Main program flow
greet()
answer_questions()
farewell()