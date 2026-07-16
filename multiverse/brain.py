class Brain:
    def __init__(self, name="Multiverse AI"):
        self.name = name

    def think(self, message):
        message = message.lower()

        if "hello" in message or "hi" in message:
            return "Hello! 👋 I am Multiverse AI."

        if "how are you" in message:
            return "I'm doing great. Ready to help you!"

        return "Sorry, I don't understand that yet."