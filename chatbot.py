class CustomerChatbot:

    def get_response(self, user_input):
        user_input = user_input.lower()

        # Greetings
        if "hello" in user_input or "hi" in user_input:
            return "Hello! Welcome to our store. How can I help you?"

        # Order status
        elif "order" in user_input and "status" in user_input:
            return "Please provide your Order ID to check the status."

        # Return / refund
        elif "return" in user_input or "refund" in user_input:
            return "You can request a return within 7 days of delivery."

        # Delivery
        elif "delivery" in user_input or "shipping" in user_input:
            return "Delivery usually takes 3-5 business days."

        # Payment
        elif "payment" in user_input:
            return "We accept UPI, Credit/Debit Cards, and Net Banking."

        # Contact support
        elif "contact" in user_input or "support" in user_input:
            return "You can contact us at support@store.com"

        # Exit condition
        elif "bye" in user_input or "exit" in user_input:
            return "Thank you for visiting! Have a great day!"

        # Default response
        else:
            return "Sorry, I didn't understand that. Can you rephrase?"

    def chat(self):
        print("Customer Support Chatbot (type 'bye' to exit)")
        while True:
            user_input = input("You: ")
            response = self.get_response(user_input)
            print("Bot:", response)

            if "bye" in user_input.lower():
                break


# Run chatbot
bot = CustomerChatbot()
bot.chat()