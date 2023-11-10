import tkinter as tk
from tkinter import messagebox

# Define a list of questions and answers
questions = [
    {
        "question": "What is the capital of France?",
        "options": ["A) London", "B) Berlin", "C) Paris", "D) Madrid"],
        "answer": "C"
    },
    {
        "question": "Which planet is known as the Red Planet?",
        "options": ["A) Venus", "B) Mars", "C) Jupiter", "D) Saturn"],
        "answer": "B"
    },
    {
        "question": "What is 2 + 2?",
        "options": ["A) 3", "B) 4", "C) 5", "D) 6"],
        "answer": "B"
    }
]

# Initialize variables
current_question = 0
score = 0

# Function to handle the "Next" button click
def next_question():
    global current_question, score

    user_answer = var.get()

    if user_answer == questions[current_question]["answer"]:
        score += 1

    current_question += 1

    if current_question < len(questions):
        show_question()
    else:
        messagebox.showinfo("Quiz Complete", f"You scored {score} out of {len(questions)}.")

# Function to display the current question
def show_question():
    question_label.config(text=questions[current_question]["question"])
    for i in range(4):
        option_labels[i].config(text=questions[current_question]["options"][i])
    var.set(None)

# Create the main window
root = tk.Tk()
root.title("Simple Quiz Application")

# Create question label
question_label = tk.Label(root, text="", font=("Arial", 12))
question_label.pack(pady=10)

# Create option labels and radio buttons
option_labels = []
var = tk.StringVar()
for i in range(4):
    option_label = tk.Label(root, text="", font=("Arial", 10))
    option_label.pack()
    option_labels.append(option_label)
    option_radio = tk.Radiobutton(root, variable=var, value=chr(ord('A') + i))
    option_radio.pack()

# Create "Next" button
next_button = tk.Button(root, text="Next", command=next_question)
next_button.pack(pady=10)

# Start the quiz
show_question()

root.mainloop()
