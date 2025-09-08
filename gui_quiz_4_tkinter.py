import tkinter as tk
from tkinter import messagebox
import random

# --- Global Variables ---
current_question = 0
score = 0
lives = 5
attempts_left = 5
selected_section = "Both"
user_name = ""
section_scores = {"Fashion History": 0, "Music Genres": 0, "Fashion & Music": 0}
question_order = []

# --- Quiz Data ---
quiz_data = [
    # Section 1: Fashion History (10 questions)
    {"section": "Fashion History", "question": "Which decade popularized the miniskirt?",
     "options": ["1960s", "1970s", "1980s", "1990s"], "answer": "1960s",
     "hint": "Think about the revolutionary 60s fashion."},
    {"section": "Fashion History", "question": "Who is the designer of the 'New Look'?",
     "options": ["Coco Chanel", "Christian Dior", "Yves Saint Laurent", "Vivienne Westwood"], "answer": "Christian Dior",
     "hint": "He introduced it in 1947."},
    {"section": "Fashion History", "question": "Which fabric was primarily used in Victorian dresses?",
     "options": ["Cotton", "Silk", "Wool", "Polyester"], "answer": "Silk",
     "hint": "A luxurious and shiny material."},
    {"section": "Fashion History", "question": "Who created the iconic wrap dress?",
     "options": ["Diane von Furstenberg", "Coco Chanel", "Betsey Johnson", "Giorgio Armani"], "answer": "Diane von Furstenberg",
     "hint": "She’s known for empowering women through dresses."},
    {"section": "Fashion History", "question": "Which style is associated with the 1920s flapper?",
     "options": ["Baggy trousers", "Short skirts & fringe dresses", "Padded shoulders", "Pencil skirts"], "answer": "Short skirts & fringe dresses",
     "hint": "Think Charleston dance style."},
    {"section": "Fashion History", "question": "Who is known for the little black dress?",
     "options": ["Coco Chanel", "Vivienne Westwood", "Christian Dior", "Yves Saint Laurent"], "answer": "Coco Chanel",
     "hint": "A French designer famous for timeless elegance."},
    {"section": "Fashion History", "question": "Which era popularized bell-bottom pants?",
     "options": ["1960s-70s", "1950s", "1980s", "1990s"], "answer": "1960s-70s",
     "hint": "Hippie era vibes."},
    {"section": "Fashion History", "question": "The punk fashion movement started in which country?",
     "options": ["USA", "UK", "France", "Germany"], "answer": "UK",
     "hint": "Think of London’s rebellious youth."},
    {"section": "Fashion History", "question": "Which designer is famous for colorful geometric patterns in the 1960s?",
     "options": ["Pierre Cardin", "Jean Paul Gaultier", "Versace", "Dior"], "answer": "Pierre Cardin",
     "hint": "He was futuristic and avant-garde."},
    {"section": "Fashion History", "question": "What accessory is iconic to Audrey Hepburn's style in 'Breakfast at Tiffany's'?",
     "options": ["Pearl necklace", "Hat", "Sunglasses", "Scarf"], "answer": "Pearl necklace",
     "hint": "A timeless piece for elegance."},

    # Section 2: Music Genres (10 questions)
    {"section": "Music Genres", "question": "Which genre is associated with jazz improvisation?",
     "options": ["Hip-Hop", "Jazz", "Rock", "Pop"], "answer": "Jazz",
     "hint": "Think swing and saxophones."},
    {"section": "Music Genres", "question": "Which genre is Tupac Shakur most associated with?",
     "options": ["Rap", "Country", "Jazz", "Rock"], "answer": "Rap",
     "hint": "West Coast 90s vibes."},
    {"section": "Music Genres", "question": "Which genre originated in the Mississippi Delta?",
     "options": ["Blues", "Reggae", "Classical", "Pop"], "answer": "Blues",
     "hint": "Emotional guitar and soulful vocals."},
    {"section": "Music Genres", "question": "Which genre is characterized by heavy electric guitar riffs?",
     "options": ["Jazz", "Rock", "Hip-Hop", "Folk"], "answer": "Rock",
     "hint": "Think Led Zeppelin."},
    {"section": "Music Genres", "question": "Which genre emerged from Jamaican dance halls in the 1960s?",
     "options": ["Reggae", "Disco", "Metal", "Jazz"], "answer": "Reggae",
     "hint": "Bob Marley vibes."},
    {"section": "Music Genres", "question": "EDM stands for what?",
     "options": ["Electronic Dance Music", "Electric Disco Music", "Experimental Digital Music", "Electronic Drum Music"], "answer": "Electronic Dance Music",
     "hint": "Popular in festivals."},
    {"section": "Music Genres", "question": "Which genre is Billie Holiday famous for?",
     "options": ["Jazz", "Rock", "Pop", "Hip-Hop"], "answer": "Jazz",
     "hint": "Her voice is soulful and emotional."},
    {"section": "Music Genres", "question": "Which genre is associated with rapping and DJing?",
     "options": ["Rap", "Blues", "Classical", "Country"], "answer": "Rap",
     "hint": "Hip-Hop culture."},
    {"section": "Music Genres", "question": "Grunge music is most associated with which decade?",
     "options": ["1980s", "1990s", "2000s", "1970s"], "answer": "1990s",
     "hint": "Seattle, plaid shirts, Nirvana."},
    {"section": "Music Genres", "question": "Which genre is known for improvisation and swing rhythm?",
     "options": ["Jazz", "Pop", "Rock", "Hip-Hop"], "answer": "Jazz",
     "hint": "Saxophone solos."},

    # Section 3: Fashion & Music (10 questions)
    {"section": "Fashion & Music", "question": "Which music movement inspired studded leather jackets in the 1970s?",
     "options": ["Punk", "Hip-Hop", "Disco", "Grunge"], "answer": "Punk",
     "hint": "Think Sex Pistols."},
    {"section": "Fashion & Music", "question": "Which pop star influenced leather jackets & skinny jeans in the 1980s?",
     "options": ["Madonna", "Michael Jackson", "Prince", "Cyndi Lauper"], "answer": "Michael Jackson",
     "hint": "Moonwalk era."},
    {"section": "Fashion & Music", "question": "Which 1990s music style brought back flannel shirts as fashion?",
     "options": ["Grunge", "Hip-Hop", "Pop", "R&B"], "answer": "Grunge",
     "hint": "Seattle and Nirvana again."},
    {"section": "Fashion & Music", "question": "The hip-hop culture in the 1980s popularized which fashion item?",
     "options": ["Baggy pants", "Mini skirts", "Platform shoes", "Bowler hats"], "answer": "Baggy pants",
     "hint": "Think Run-DMC style."},
    {"section": "Fashion & Music", "question": "Which designer worked with Madonna to create stage outfits in the 1980s?",
     "options": ["Jean Paul Gaultier", "Versace", "Armani", "Dior"], "answer": "Jean Paul Gaultier",
     "hint": "Famous for cone bra."},
    {"section": "Fashion & Music", "question": "Which footwear became iconic for hip-hop artists in the 1980s?",
     "options": ["Air Jordans", "Converse", "Loafers", "Boots"], "answer": "Air Jordans",
     "hint": "Basketball shoes became street fashion."},
    {"section": "Fashion & Music", "question": "Which British music genre influenced Vivienne Westwood’s punk designs?",
     "options": ["Punk Rock", "Disco", "Pop", "Jazz"], "answer": "Punk Rock",
     "hint": "London punk scene."},
    {"section": "Fashion & Music", "question": "MTV in the 1980s helped popularize which fashion trend?",
     "options": ["Bold colors & big hair", "Flapper dresses", "Tweed suits", "Minimalism"], "answer": "Bold colors & big hair",
     "hint": "Think Madonna and Cyndi Lauper."},
    {"section": "Fashion & Music", "question": "Which 1970s disco trend influenced fashion?",
     "options": ["Bell-bottom pants & sequins", "Plaid shirts", "Baggy pants", "Leather jackets"], "answer": "Bell-bottom pants & sequins",
     "hint": "Studio 54 vibes."},
    {"section": "Fashion & Music", "question": "Which rapper helped make gold chains a mainstream fashion accessory?",
     "options": ["Run DMC", "Tupac", "Jay-Z", "Eminem"], "answer": "Run DMC",
     "hint": "Hip-hop bling."}
]

# --- Functions ---
def start_quiz():
    global question_order
    welcome_frame.pack_forget()
    if selected_section != "Both":
        question_order = [i for i, q in enumerate(quiz_data) if q["section"] == selected_section]
    else:
        question_order = list(range(len(quiz_data)))
    random.shuffle(question_order)
    show_question()

def show_question():
    global current_question, lives
    if current_question < len(question_order):
        idx = question_order[current_question]
        q_data = quiz_data[idx]
        section_label.config(text=f"Section: {q_data['section']}")
        question_label.config(text=q_data["question"])
        for i, option in enumerate(q_data["options"]):
            option_buttons[i].config(text=option, state=tk.NORMAL)
        feedback_label.config(text=f"Lives: {lives} | Attempts left: {attempts_left}")
    else:
        end_quiz()

def check_answer(selected):
    global current_question, score, lives, section_scores
    idx = question_order[current_question]
    q_data = quiz_data[idx]

    if selected == q_data["answer"]:
        score += 1
        section_scores[q_data["section"]] += 1
        feedback_label.config(text="Correct!", fg="green")
    else:
        lives -= 1
        feedback_label.config(text=f"Incorrect! {q_data['hint']}", fg="red")

    for btn in option_buttons:
        btn.config(state=tk.DISABLED)

    current_question += 1
    root.after(1000, show_question)

def swap_section():
    global selected_section
    if selected_section == "Fashion History":
        selected_section = "Music Genres"
    elif selected_section == "Music Genres":
        selected_section = "Fashion History"
    feedback_label.config(text=f"Swapped section to {selected_section}")
    root.after(500, show_question)

def end_quiz():
    global attempts_left
    section_summary = "\n".join([f"{sec}: {s} points" for sec, s in section_scores.items()])
    messagebox.showinfo("Quiz Complete",
                        f"{user_name}, your total score is {score} / {len(question_order)}\n\nSection Scores:\n{section_summary}")
    attempts_left -= 1
    if attempts_left > 0:
        root.destroy()
    else:
        messagebox.showinfo("Quiz Over", "No more attempts left.")
        root.destroy()

def quit_quiz():
    root.destroy()

def save_name():
    global user_name
    user_name = name_entry.get()
    if user_name.strip() == "":
        user_name = "Player"
    welcome_frame.pack_forget()
    section_selection_frame.pack()

def choose_section(sec):
    global selected_section
    global question_order
    selected_section = sec
    section_selection_frame.pack_forget()
    start_quiz()

# --- GUI Setup ---
root = tk.Tk()
root.title("Fashion & Music Quiz")
root.geometry("700x500")

# Welcome Frame
welcome_frame = tk.Frame(root)
welcome_frame.pack(pady=50)

welcome_label = tk.Label(welcome_frame, text="Welcome to the Fashion & Music Quiz!", font=("Arial", 16))
welcome_label.pack(pady=10)

name_label = tk.Label(welcome_frame, text="Enter your name:", font=("Arial", 14))
name_label.pack(pady=5)

name_entry = tk.Entry(welcome_frame, font=("Arial", 14))
name_entry.pack(pady=5)

name_button = tk.Button(welcome_frame, text="Continue", font=("Arial", 14), command=save_name)
name_button.pack(pady=10)

# Section Selection Frame
section_selection_frame = tk.Frame(root)

section_label_title = tk.Label(section_selection_frame, text="Choose a section to start with:", font=("Arial", 14))
section_label_title.pack(pady=10)

sections = ["Fashion History", "Music Genres", "Both"]
for sec in sections:
    btn = tk.Button(section_selection_frame, text=sec, font=("Arial", 14), width=20, command=lambda s=sec: choose_section(s))
    btn.pack(pady=5)

# Quiz Frame
section_label = tk.Label(root, text="", font=("Arial", 14))
section_label.pack(pady=10)

question_label = tk.Label(root, text="", font=("Arial", 16), wraplength=600)
question_label.pack(pady=20)

option_buttons = []
for i in range(4):
    btn = tk.Button(root, text="", font=("Arial", 14), width=30, command=lambda i=i: check_answer(option_buttons[i]["text"]))
    btn.pack(pady=5)
    option_buttons.append(btn)

feedback_label = tk.Label(root, text="", font=("Arial", 12))
feedback_label.pack(pady=10)

swap_button = tk.Button(root, text="Swap Section", font=("Arial", 14), command=swap_section)
swap_button.pack(pady=5)

quit_button = tk.Button(root, text="Quit", font=("Arial", 14), command=quit_quiz)
quit_button.pack(pady=5)

# Disable buttons initially
for btn in option_buttons:
    btn.config(state=tk.DISABLED)

root.mainloop()
