import random
greetings = ["Hello!", "Hi there!", "It's nice to meet you!"]
questions = {
    "name": "What is your name?",
    "age": "How old are you?",
    "hobby": "What's your favorite hobby?"
}
answers = {
    "name": "Nice to meet you, {name}!",
    "age": "Interesting! I'm just a bunch of code.",
    "hobby": "That sounds Great! I don't have hobbies, but I like learning new things like {name}."
}
farewell = "It was nice talking to you! See you later."

print(random.choice(greetings))

for i in questions.keys():
    print(questions[i])
    response = input()
    print(answers[i].format(name=response))

print(farewell)
