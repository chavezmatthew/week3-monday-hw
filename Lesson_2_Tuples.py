# 1. Tuple Mastery in Python

# Objective: The aim of this assignment is to deepen your understanding of tuples in Python, along with their interaction with lists, dictionaries, and basic Python functionalities like functions, input handling, and string formatting. By completing this assignment, you will enhance your skills in data structuring, manipulation, and application of tuples in practical scenarios.

# Task 1: Formatting Flight Itineraries Create a Python function that takes a list of tuples as an argument. Each tuple contains information about a flight itinerary: (traveler_name, origin, destination). The function should loop through the list of itineraries and print a formatted string for each. For example, if the input is [("Alice", "New York", "London"), ("Bob", "Tokyo", "San Francisco")], the output should be:

# "Itinerary 1: Alice - From New York to London"
# "Itinerary 2: Bob - From Tokyo to San Francisco"

itinerary_list = []

def itineraries ():
    while True:
        traveler_name = input("Please enter the traveler's name: \n")
        origin = input("Please enter the traveler's origin: \n")
        destination = input ("Please enter the traveler's destination: \n")
        itinerary_tuple = (traveler_name, origin, destination)
        itinerary_list.append(itinerary_tuple)
        for index, (traveler_name, origin, destination) in enumerate(itinerary_list, start=1):
            print (f"Success! Itinerary {index}: {traveler_name} - From {origin} to {destination}")
        another = input("Would you like to add another itinerary? \n")
        if another.lower() != 'yes':
            print("Thanks for using our itinerary app!")
            break

itineraries()

# 2. Python Data Structure Challenges in Real-World Scenarios

#  Objective: This assignment is designed to enhance your understanding and application of Python's core data structures - tuples, lists, and dictionaries - in real-world contexts. By engaging with these tasks, you will practice manipulating these data structures, applying built-in Python methods, and implementing error handling in practical situations.

# Task 1: Library System Enhancement Sharpen your skills in managing and modifying data within tuples and lists.

# Problem Statement: You are maintaining a library system where each book is stored as a tuple within a list. Your task is to update this system by adding new books and ensuring no duplicates.

# Existing Library Data:

library = [("1984", "George Orwell"), ("Brave New World", "Aldous Huxley")]


# Add functionality to insert new books into library.
# Ensure that adding a duplicate book is handled appropriately (hint: do a membership check to see if the new book is already in the library).


def add_books():
    while True:
        book = input ("Please enter the book you'd like to add: \n")
        author = input ("Please enter the author of the book you'd like to add: \n")
        book_tuple = (book, author)
        if book_tuple in library:
            print("This book is already in the library.")
        else:
            library.append(book_tuple)
            print("Book added! Updated library: ", library)
        another = input ("Would you like to add another book? \n")
        if another.lower() != 'yes':
            print("Thanks for using our interactive library!")
            break

add_books()