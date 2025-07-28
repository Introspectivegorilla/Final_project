# flashcard app
import random
print("Welcome to Study Habits!")
print("Create your Personalized flashcards")

# flashcard_q = input("Type in your prompt")
# flashcard_a = input("Type in your answer")

# study_q = []
# study_a = []
# study_q.append(flashcard_q)
# study_a.append(flashcard_a)

# Defining question list


def questions(prompt, old_list):
    user_input = input(prompt)
    old_list.append(user_input)

    return old_list


# Defining answer list


def answers(prompt, old_list):

    user_input = input(prompt)
    old_list.append(user_input)

    return old_list

# def finish_list(list_one, list_two):
#     questions.append(list_one)
#     answers.append(list_two)

#     return list_one and list_two


# creating dictionary

status = input("Do you want to add a flashcard y/n")
first_letter = status[0]

flashcard_q = []
flashcard_a = []


while first_letter.lower() == "y":
    flashcard_q = questions("Type in your questions", flashcard_q)
    flashcard_a = answers("Type in your answers", flashcard_a)
    status = input("Do you want to add a flashcard y/n")
    first_letter = status[0]


if first_letter.lower() == "n":
    print(flashcard_q)
    print(flashcard_a)

else:
    status = input("Doesn't make sense. Start over")
    exit()
# study_dict = dict(zip(flashcard_q, flashcard_a))
study_dict = {key: value for key, value in zip(flashcard_q, flashcard_a)}
print(study_dict)
print("Great, lets get started!")
print("I will ask you a question and you will type out the answer")
move_on_letter = "y"
random.shuffle(flashcard_q)
print(flashcard_q)
pick = 0

while move_on_letter.lower() == "y":
    print(flashcard_q[pick])
    value = study_dict[flashcard_q[pick]]
    answer = input()
    pick = pick + 1
    if answer == value:
        print("Correct")
    else:
        print("Wrong")
    move_on = input("Do you want to move on y/n? ")
    move_on_letter = move_on[0]
if move_on_letter.lower() == "n":
    print("Bye")
    exit()


# # if the user puts a random letter
# else:
#     status = input("Do you want to add a flashcard y/n")
# # for flashcard_q in range[0,]:

# confirm_list = input("Is this your full list y/n? ")
# first_letter_cl = confirm_list[0]


# if first_letter_cl.lower() == "y":
#     print("Great, lets get started!")


# while first_letter_cl.lower() == "n":
#     status = input("Do you want to add a flashcard y/n")
#     first_letter = status[0]

#     while first_letter.lower() == "y":

#         flashcard_q = questions("Type in your questions", flashcard_q)
#         flashcard_a = answers("Type in your answers", flashcard_a)
#         status = input("Do you want to add a flashcard y/n")
#         first_letter = status[0]

#     if first_letter.lower() == "n":
#         print(flashcard_q)
#         print(flashcard_a)

# # if the user puts a random letter
#     else:
#         status = input("Do you want to add a flashcard y/n")

#     confirm_list = input("Is this your full list y/n? ")
#     first_letter_cl = confirm_list[0]

#     if first_letter_cl.lower() == "y":
#         print("Great, lets get started!")


# # random.choice(flashcard_q)
