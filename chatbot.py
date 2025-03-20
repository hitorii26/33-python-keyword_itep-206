import random                       # 1. import
from datetime import datetime       # 2. from

# This class defines chatbot
class Chatbot:                              # 3. class
    def __init__ (self, name="Noe"):         # 4. def
        self.name = name
        self.user.name = None               # 5. none
        self.chat_history = []
        global chatbot_instance             # 6. global
        chatbot_instance = self  

    def set_user_name(self, name):
        global user_name
        user_name = name

    def get_greeting(self):
        return f"Hello! I'm {self.name} your chatbot assistant. May I know your name?"  # 7. return
    
    def save_chat(self):
        """Save chat history to a file."""
        with open("chat_history.txt", "w" ) as file:        # 8. with, 9. in, 10. as
            for line in self.chat_history:                  # 11. for
                file.write(line + "\n")

    def tell_jokes(self):
        jokes = [
            "Why don't programmers like nature? It has to many bugs."
            "Why do Java developers wear glasses? Because they don't C#\!"
        ]
        return random.choice(jokes)
    
    def get_time(self):
        return f"The current time is {datetime.now().strftime('%H:%M:%S')}"

    def process_input(self, user_input):
        """Process user input and generate a response."""
        self.chat_history.append(f"You: {user_input}")

        if user_input.lower() ["hello", "hi"]:                  # 12. if
            return "Hi there boss!"
        elif user_input.lower() == "what's your name?":         # 13. elif
            return f"I'm {self.name}!"
        elif user_input.lower == "tell me a joke":
            return self.tell_joke()
        elif user_input.lower == "what time is it?":
            return self.get_time()
        elif "exit" in user_input.lower():
            self.save_chat
            return "Sayonara!"
        else:                                                    # 14. else
            return "I'm not sure how to respond to that."


class AdvancedChatbot(Chatbot): 
    def __init__(self, name="AdvancedChatBot"):
        super().__init__(name)
        self.previous_question = None 

    def save_response(self, message):
        """Saves user responses dynamically."""
        nonlocal_var = "response saved"

        def inner_function():  
            nonlocal nonlocal_var                                   # 15. nonlocal
            nonlocal_var = f"Saved response: {message}"

        inner_function()
        return nonlocal_var
    
    def delete_memory(self, key):
        """Deletes a stored response if it exists."""
        if key in self.memory:
            del self.memory[key]                                    # 16. del 
            return f"Deleted memory: {key}"
        else:
            return f"{key} was not found in memory."

    def response_generator(self, keyword):
        """Generates multiple responses using yield."""
        responses = {
            "weather": ["It's sunny!", "It might rain later.", "Check the forecast."],
            "mood": ["I'm happy!", "I'm feeling great!", "I'm here to help."]
        }
        if keyword in responses:
            for response in responses[keyword]:
                yield response                                      # 17. yield

    def validate_message(self, message):
        """Uses assert to ensure valid message length."""
        assert len(message) > 0, "Message cannot be empty!"         # 18. assert
        return "Valid message received."

    def risky_action(self):
        """Uses try-except-raise-finally to simulate an error."""
        try:                                                                # 19. try
            user_input = input("Type a number: ")
            if not user_input.isdigit():
                raise ValueError("Invalid input! Must be a number.")        # 20. raise
            return int(user_input)
        except ValueError as e:                                             # 21. except
            return f"Error: {e}"
        finally:                                                            # 22. finally
            print("Operation complete.")

    def guess_the_number(self):
        """Mini-game: Guess the number."""
        secret_number = random.randint(1, 10) 
        print("Guess a number between 1 and 10!")
        while True: 
            try:
                guess = int(input("> "))
                if guess == secret_number:
                    print("🎉 Correct! You guessed the number!")
                    break 
                elif guess is False:                                            # 23. is, 24. false
                    print("Out of range. PLease guess it between 1 and 10")
                elif guess < secret_number:
                    print("Too low! Try again.")
                else:
                    print("Too high! Try again.")
            except ValueError:
                print("Please enter a valid number.")


    
# This function is user interaction
def chat():
    bot = AdvancedChatbot()
    print(bot.get_greeting())

    while True:                                                     # 25. while,  26. true
        try:  
            user_input = input("> ").strip()
            if not user_input:                                      # 27. not
                continue                                            # 28. continue
            if user_input.lower() == "exit":
                print(bot.process_input(user_input))
                break                                               # 29. break
            
            responses = {
                "hello": lambda: "Hi there!",                       # 30. lambda
                "joke": lambda: bot.tell_joke(),
                "time": lambda: bot.get_time(),
                "game": lambda: bot.guess_the_number(),
                "memory": lambda: f"Memory: {bot.memory}"
            }

            if "validate" in user_input.lower():
                print(bot.validate_message(user_input))
                continue

            elif "weather" in user_input.lower() or "mood" in user_input.lower():                                   # 31. or
                generator = bot.response_generator("weather" if "weather" in user_input.lower() else "mood")
                print(next(generator)) 
            elif user_input.lower().startswith("is "):  
                key = user_input.split(" ", 1)[1]
                print(f"{key} is in memory: {key in bot.memory}")  
                print(f"Checking identity: {key is False}")  

            elif "check" in user_input.lower():
                if "weather" in bot.memory and "mood" in bot.memory:                # 32. and     
                    print("You have stored both weather and mood responses.")
                else:
                    print("You need to add more memory first.")
            else:
                print("I'm not sure how to respond to that.")
        
        except KeyboardInterrupt:  
            print("\nChat ended.")
            break

        finally:  
            pass                                                    # 33. pass

chat()