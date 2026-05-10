# 1. Define a function to handle the chatbot's logic
def get_bot_response(user_input):
    # Convert input to lowercase so "Hello" and "hello" are treated the same
    user_input = user_input.lower().strip()
    
    # 2. Use if-elif statements for predefined rules
    if user_input == "hello":
        return "Hi!"
    elif user_input == "how are you":
        return "I'm fine, thanks!"
    elif user_input == "bye":
        return "Goodbye!"
    else:
        # A fallback response just in case they type something else
        return "Sorry, I only understand 'hello', 'how are you', and 'bye'."

# 3. Define the main function to run the chat loop
def start_chat():
    print("--- Chatbot Started ---")
    print("(Type 'bye' to exit the chat)\n")
    
    # 4. Use a loop to keep the conversation going
    while True:
        # 5. Input/Output
        text_from_user = input("You: ")
        
        # Pass the input to our logic function
        bot_reply = get_bot_response(text_from_user)
        
        print(f"Bot: {bot_reply}")
        
        # Break the loop if the user wants to leave
        if text_from_user.lower().strip() == "bye":
            break

# Start the program
if __name__ == "__main__":
    start_chat()
