from utils import get_time, get_date, random_response

responses = {
    "greeting": ["Hello!", "Hi there!", "Hey! How can I help you?"],
    
    "how_are_you": [
        "I'm doing great!",
        "I'm fine, thanks for asking!",
        "All good here!"
    ],
    
    "name": [
        "I am your chatbot.",
        "You can call me ChatBot.",
        "I am a simple Python chatbot."
    ],
    
    "college": [
        "This is a college chatbot project.",
        "I can help with basic college queries."
    ],
    
    "courses": [
        "Courses include AI, Python, Data Science.",
        "We offer Machine Learning and Web Development."
    ],
    
    "help": [
        "You can ask about courses, time, date, etc.",
        "Try asking: What courses are available?"
    ],
    
    "bye": [
        "Goodbye! Have a great day!",
        "Bye! Take care!",
        "See you soon!"
    ],
    
    "default": [
        "Sorry, I didn't understand.",
        "Please try asking something else.",
        "I'm still learning!"
    ]
}

def chatbot():
    print("="*50)
    print("🤖 CHATBOT STARTED")
    print("Type 'bye' or 'exit' to stop")
    print("="*50)

    while True:
        user_input = input("\nYou: ").lower()

        if not user_input.strip():
            print("Chatbot: Please enter something.")
            continue

        if "hi" in user_input or "hello" in user_input:
            print("Chatbot:", random_response(responses["greeting"]))

        elif "how are you" in user_input:
            print("Chatbot:", random_response(responses["how_are_you"]))

        elif "name" in user_input:
            print("Chatbot:", random_response(responses["name"]))

        elif "college" in user_input:
            print("Chatbot:", random_response(responses["college"]))

        elif "course" in user_input:
            print("Chatbot:", random_response(responses["courses"]))

        elif "time" in user_input:
            print("Chatbot: Current time is", get_time())

        elif "date" in user_input:
            print("Chatbot: Today's date is", get_date())

        elif "help" in user_input:
            print("Chatbot:", random_response(responses["help"]))

        elif "bye" in user_input or "exit" in user_input:
            print("Chatbot:", random_response(responses["bye"]))
            break

        else:
            print("Chatbot:", random_response(responses["default"]))


if __name__ == "__main__":
    chatbot()