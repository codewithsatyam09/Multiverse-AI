from multiverse.brain import Brain

assistant = Brain()

print("=" * 40)
print("🚀 Multiverse AI")
print("=" * 40)

while True:
    user = input("You: ")

    if user.lower() == "exit":
        print("Multiverse: Goodbye! 👋")
        break

    reply = assistant.think(user)
    print("Multiverse:", reply)

while True:
    user = input("You: ")

    if user.lower() == "exit":
        print("Multiverse: Goodbye! 👋")
        break

    reply = assistant.think(user)
    print("Multiverse:", reply)