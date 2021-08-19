import random
from banner import Text 

def easy_questions(user):

    questions = [
    b'Write a function, that takes a single integer as input and returns the sum of the integers from zero to the input parameter. \n\nThe function should return 0 if a non-integer is passed in.\n\n', 
    b'Given two integer values, return their sum. If the two values are the same, then return double their sum.\n\n', 
    b'Given 2 integers, a and b, return True if one if them is 10 or if their sum is 10. Otherwise return False.\n\n',
    b'Write a function called reverseArray which takes an array as an argument. Without utilizing any of the built-in methods available, return an array with elements in reversed order.\n\n',
    b'Given a matrix, find the sum of each row.\n\n',
    b'Reverse a Singly Linked List without utilizing any of the built-in methods available.\n\n',
    b'Validate whether or not a Linked List is palindrome. A palindrome is a word, phrase, number, or sequence of nodes which reads the same backward as forward.\n\n',
    b'Write a method that returns the biggest element in a stack. Max Stack is defined as a Stack with an additional getMax member function which returns the biggest element in the Stack.\n\n',]
    prefix = Text.green_text('💥YOUR CHALLENGE:💥\n\n')
    random_question = random.choice(questions)
    user.socket.sendall(prefix + random_question)
