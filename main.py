import random


def ask_name():
    name = input("Please enter your name: ")
    return name


def display_question(question, choices):
    print(question)
    for i, choice in enumerate(choices, 1):
        print(f"{i}. {choice}")
    user_choice = int(input("Enter the number of your choice (1, 2, 3, or 4): "))
    return user_choice

def check_answer(user_choice, correct_answer):
    return user_choice == correct_answer


def update_high_score(name, score):
    with open("high_scores.txt", "a") as file:
        file.write(f"{name}: {score}\n")

def get_high_score():
    high_scores = {}
    try:
        with open("high_scores.txt", "r") as file:
            for line in file:
                name, score = line.strip().split(": ")
                high_scores[name] = float(score)
    except FileNotFoundError:
        pass
    return high_scores

def get_random_questions():
    questions = [
        {
            "question": "What is the full form of CSE?",
            "choices": ["Computer System Engineering", "Computer Science and Electronics",
                        "Computer Science and Engineering", "Computer Software Engineering"],
            "correct_answer": 3,
        },
        {
            "question": "What is a high-level programming language?",
            "choices": ["Machine Language", "Assembly Language", "C++", "Binary Code"],
            "correct_answer": 3,
        },
        {
            "question": "What does CPU stand for?",
            "choices": ["Computer Processing Unit", "Central Processing Unit", "Central Programming Unit",
                        "Computer Programming Unit"],
            "correct_answer": 2,
        },
        {
            "question": "Which data structure follows the Last In, First Out (LIFO) principle?",
            "choices": ["Queue", "Stack", "Linked List", "Tree"],
            "correct_answer": 2,
        },
        {
            "question": "Which sorting algorithm has the best average-case time complexity?",
            "choices": ["Bubble Sort", "Insertion Sort", "Merge Sort", "Selection Sort"],
            "correct_answer": 3,
        },
        {
            "question": "Which programming language is often used for web development?",
            "choices": ["Java", "Python", "C#", "JavaScript"],
            "correct_answer": 4,
        },
        {
            "question": "What is the primary purpose of an operating system?",
            "choices": ["Managing hardware resources", "Creating web applications", "Designing databases",
                        "Debugging code"],
            "correct_answer": 1,
        },
        {
            "question": "Which data structure uses a unique identifier to access its elements?",
            "choices": ["Array", "Linked List", "Dictionary", "Stack"],
            "correct_answer": 3,
        },
        {
            "question": "Which data structure is used for implementing recursion?",
            "choices": ["Stack", "Queue", "Array", "Tree"],
            "correct_answer": 1,
        },
        {
            "question": "What is the maximum value that can be represented using 8 bits?",
            "choices": ["128", "256", "64", "512"],
            "correct_answer": 2,
        },
        {
            "question": "Which data structure is used to represent a hierarchical relationship between elements?",
            "choices": ["Array", "Graph", "Tree", "Stack"],
            "correct_answer": 3,
        },
        {
            "question": "What is the purpose of an IDE (Integrated Development Environment)?",
            "choices": ["Managing databases", "Writing code", "Designing user interfaces", "Storing files and folders"],
            "correct_answer": 2,
        },
        {
            "question": "Which algorithm is used to find the shortest path in a weighted graph?",
            "choices": ["Breadth-First Search (BFS)", "Depth-First Search (DFS)", "Dijkstra's Algorithm",
                        "Bubble Sort"],
            "correct_answer": 3,
        },
        {
            "question": "Which programming language is commonly used for scientific and mathematical computing?",
            "choices": ["Java", "C++", "Python", "Ruby"],
            "correct_answer": 3,
        },
        {
            "question": "Which data structure uses the First In, First Out (FIFO) principle?",
            "choices": ["Stack", "Queue", "Linked List", "Tree"],
            "correct_answer": 2,
        },
        {
            "question": "What is the full form of URL?",
            "choices": ["Universal Resource Locator", "Uniform Resource Locator", "Uniform Remote Link",
                        "Universal Remote Link"],
            "correct_answer": 2,
        },
        {
            "question": "Which search algorithm is efficient for a sorted list?",
            "choices": ["Linear Search", "Binary Search", "Depth-First Search (DFS)", "Breadth-First Search (BFS)"],
            "correct_answer": 2,
        },
        {
            "question": "Which encryption algorithm is used for secure data transmission over the internet?",
            "choices": ["RSA", "AES", "SHA-256", "MD5"],
            "correct_answer": 2,
        },
        {
            "question": "Which programming paradigm focuses on breaking a problem into smaller subproblems?",
            "choices": ["Procedural Programming", "Object-Oriented Programming (OOP)", "Functional Programming",
                        "Imperative Programming"],
            "correct_answer": 3,
        },
        {
            "question": "What is the purpose of a compiler?",
            "choices": ["Translating source code to machine code", "Executing code line by line", "Debugging code",
                        "Managing memory allocation"],
            "correct_answer": 1,
        },
        {
            "question": "Which data structure is a collection of key-value pairs?",
            "choices": ["Array", "Stack", "Queue", "Dictionary"],
            "correct_answer": 4,
        },
        {
            "question": "Which algorithm is used to find the maximum value in an unsorted list?",
            "choices": ["Bubble Sort", "Insertion Sort", "Selection Sort", "Linear Search"],
            "correct_answer": 3,
        },
        {
            "question": "Which programming language is widely used for game development?",
            "choices": ["Java", "Python", "C++", "Ruby"],
            "correct_answer": 3,
        },
        {
            "question": "What is the primary role of a database management system (DBMS)?",
            "choices": ["Creating graphical user interfaces", "Storing files and folders",
                        "Managing and organizing data", "Debugging code"],
            "correct_answer": 3,
        },
        {
            "question": "Which data structure uses a hierarchical ordering of elements?",
            "choices": ["Stack", "Queue", "Tree", "Linked List"],
            "correct_answer": 3,
        },
        {
            "question": "What is the purpose of a loop in programming?",
            "choices": ["Declaring variables", "Executing code repeatedly", "Writing comments",
                        "Formatting text output"],
            "correct_answer": 2,
        },
        {
            "question": "Which sorting algorithm is known for its stable sorting property?",
            "choices": ["Bubble Sort", "Selection Sort", "Insertion Sort", "Merge Sort"],
            "correct_answer": 4,
        },
        {
            "question": "Which programming language is often used for data analysis and machine learning?",
            "choices": ["Python", "Java", "C#", "JavaScript"],
            "correct_answer": 1,
        },
        {
            "question": "What is the primary function of a network router?",
            "choices": ["Transmitting data within a computer", "Connecting devices to the internet",
                        "Allocating memory to programs", "Executing machine code"],
            "correct_answer": 2,
        },
        {
            "question": "Which data structure uses a First In, Last Out (FILO) principle?",
            "choices": ["Stack", "Queue", "Linked List", "Tree"],
            "correct_answer": 1,
        },

    ]

    random.shuffle(questions)
    return questions[:10]

