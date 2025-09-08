# --- Imports ---
import tkinter as tk
from tkinter import messagebox

# --- Global Variables ---
current_question = 0
score = 0
section_scores = {"Fashion History": 0, "Music Genres": 0, "Fashion & Music": 0}
selected_section = ""
player_name = ""
filtered_data = []

# --- Quiz Data with hints & info ---
quiz_data = [
    # Fashion History Examples
    {"section": "Fashion History", "question": "Which decade popularized the miniskirt?", 
     "options": ["1960s", "1970s", "1980s", "1990s"], 
     "answer": "1960s",
     "hint": "Think of the decade with Swinging London.",
     "info": "The miniskirt became iconic in the 1960s thanks to Mary Quant."},

    {"section": "Fashion History", "question": "Who is the designer of the 'New Look'?", 
     "options": ["Coco Chanel", "Christian Dior", "Yves Saint Laurent", "Vivienne Westwood"], 
     "answer": "Christian Dior",
     "hint": "Launched in 1947, reshaping post-war fashion.",
     "info": "Dior's 'New Look' featured cinched waists and full skirts."},

    # Music Genres Examples
    {"section": "Music Genres", "question": "Which genre is associated with jazz improvisation?", 
     "options": ["Hip-Hop", "Jazz", "Rock", "Pop"], 
     "answer": "Jazz",
     "hint": "Originated in the early 20th century USA.",
     "info": "Jazz emphasizes swing and improvisation."},

    {"section": "Music Genres", "question": "Which genre is Tupac Shakur most associated with?", 
     "options": ["Rap", "Country", "Jazz", "Rock"], 
     "answer": "Rap",
     "hint": "Think of 90s West Coast style.",
     "info": "Tupac was a leading figure in rap and hip-hop culture."},

    # Fashion & Music Examples
    {"section": "Fashion & Music", "question": "Which music movement inspired studded leather jackets in the 1970s?", 
     "options": ["Punk", "Hip-Hop", "Disco", "Grunge"], 
     "answer": "Punk",
     "hint": "Anti-establishment style.",
     "info": "Punk musicians and fans popularized leather and studs as rebellion fashion."},

    {"section": "Fashion & Music", "question": "Which pop star influenced leather jackets & skinny jeans in the 1980s?", 
     "options": ["Madonna", "Michael Jackson", "Prince", "Cyndi Lauper"], 
     "answer": "Michael Jackson",
     "hint": "Moonwalk king.",
     "info": "MJ's style inspired 80s fashion trends including jackets and jeans."},
    
    # Add remaining 24 questions in same format
]

# --- Functions ---
def start_quiz():
    welcome_label.pack_forget()
    instructions_label.pack_forget()
    name_label.pack_forget()
    name_entry.pack_forget()
    name_button.pack_forget()
    section_choice_label.pack()
    for btn in section_buttons:
        btn.pack()
    quit_button.pack(pady=10)

def choose_section(section):
    global selected_section, filtered_data, current_question
    selected_section = section
    current_question = 0
    if selected_section != "Both":
        filtered_data = [q for q in quiz_data if q["section"] == selected_section]
    else:
        filtered_data = quiz_data
    section_choice_label.pack_forget()
    for btn in section_buttons:
        btn.pack_forget()
    show_question()

def show_question():
    global current_question
    if current_question < len(filtered_data):
        q_data = filtered_data[current_question]
        section_label.config(text=f"Section: {q_data['section']}")
        question_label.config(text=q_data["question"])
        for i, option in enumerate(q_data["options"]):
            option_buttons[i].config(text=option, state=tk.NORMAL)
        feedback_label.config(text="")
    else:
        end_quiz()

def check_answer(selected):
    global current_question, score
    q_data = filtered_data[current_question]
    if selected == q_data["answer"]:
        score += 1
        section_scores[q_data["section"]] += 1
        feedback_label.config(text="Correct!", fg="green")
    else:
        feedback_label.config(text=f"Incorrect! {q_data['info']}", fg="red")
    for btn in option_buttons:
        btn.config(state=tk.DISABLED)
    current_question += 1
    root.after(1500, show_question)

def show_hint():
    if current_question < len(filtered_data):
        hint = filtered_data[current_question].get("hint", "No hint available")
        messagebox.showinfo("Hint", hint)

def swap_section():
    for btn in option_buttons:
        btn.config(state=tk.DISABLED)
    section_choice_label.pack()
    for btn in section_buttons:
        btn.pack()

def quit_quiz():
    if messagebox.askyesno("Quit Quiz", "Are you sure you want to quit?"):
        root.destroy()

def end_quiz():
    section_summary = "\n".join([f"{sec}: {s} points" for sec, s in section_scores.items()])
    messagebox.showinfo("Quiz Complete", f"{player_name}, your total score is {score} / {len(filtered_data)}\n\nSection Scores:\n{section_summary}")
    root.destroy()

def save_name():
    global player_name
    player_name = name_entry.get() if name_entry.get() != "" else "Player"
    start_quiz()

# --- GUI Setup ---
root = tk.Tk()
root.title("Fashion & Music Quiz")
root.geometry("750x550")

# Greeting
welcome_label = tk.Label(root, text="Welcome to the Fashion & Music Quiz!", font=("Arial", 16))
welcome_label.pack(pady=20)
instructions_label = tk.Label(root, text="Enter your name, select a section, and answer the questions.", font=("Arial", 14))
instructions_label.pack(pady=10)

# Name input
name_label = tk.Label(root, text="Enter your name:", font=("Arial", 14))
name_label.pack(pady=10)
name_entry = tk.Entry(root, font=("Arial", 14))
name_entry.pack(pady=5)
name_button = tk.Button(root, text="Start", font=("Arial", 14), command=save_name)
name_button.pack(pady=10)

# Section selection
section_choice_label = tk.Label(root, text="Choose a section:", font=("Arial", 14))
section_buttons = []
for sec in ["Fashion History", "Music Genres", "Both"]:
    btn = tk.Button(root, text=sec, font=("Arial", 14), width=20, command=lambda s=sec: choose_section(s))
    section_buttons.append(btn)

# Quiz widgets
section_label = tk.Label(root, text="", font=("Arial", 14))
section_label.pack(pady=10)
question_label = tk.Label(root, text="", font=("Arial", 16), wraplength=650)
question_label.pack(pady=20)

option_buttons = []
for i in range(4):
    btn = tk.Button(root, text="", font=("Arial", 14), width=30, command=lambda i=i: check_answer(option_buttons[i]["text"]))
    btn.pack(pady=5)
    option_buttons.append(btn)
for btn in option_buttons:
    btn.config(state=tk.DISABLED)

feedback_label = tk.Label(root, text="", font=("Arial", 12))
feedback_label.pack(pady=10)

# Extra buttons
hint_button = tk.Button(root, text="Hint", font=("Arial", 14), command=show_hint)
hint_button.pack(pady=5)
swap_button = tk.Button(root, text="Swap Section", font=("Arial", 14), command=swap_section)
swap_button.pack(pady=5)
quit_button = tk.Button(root, text="Quit", font=("Arial", 14), command=quit_quiz)

root.mainloop()
