import random
from banner import Text 

def easy_questions(user):

    questions = [
    b'Write a function, that takes a single integer as input and returns the sum of the integers from zero to the input parameter. \n\nThe function should return 0 if a non-integer is passed in.\n\n', 
    b'Given two integer values, return their sum. If the two values are the same, then return double their sum.\n\n', 
    b'Given 2 integers, a and b, return True if one if them is 10 or if their sum is 10. Otherwise return False.\n\n' ]
    prefix = Text.green_text('💥YOUR CHALLENGE:💥\n\n')
    random_question = random.choice(questions)
    user.socket.sendall(prefix + random_question)
