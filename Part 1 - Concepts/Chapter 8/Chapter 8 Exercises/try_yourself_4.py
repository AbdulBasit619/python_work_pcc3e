# text_messages = [
#     "Hello Coders!",
#     "I love Python!",
#     "I am into Machine Learning",
#     "I want to learn Sci-kit Learn, Keras and Tensorflow",
# ]


# def show_messages():
#     for message in text_messages:
#         print(message)


# show_messages()


text_messages = [
    "Hello Coders!",
    "I love Python!",
    "I am into Machine Learning",
    "I want to learn Sci-kit Learn, Keras and Tensorflow",
]

sent_messages = []


def send_messages(messages):
    while messages:
        message = messages.pop()
        print(message)

        sent_messages.append(message)


# send_messages(text_messages)
send_messages(text_messages[:])

print(text_messages)
print(sent_messages)
