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

# --- Quiz Data (30 Questions) ---
quiz_data = [
    # Section 1: Fashion History
    {"section": "Fashion History", "question": "Which decade popularized the miniskirt?", 
     "options": ["1960s", "1970s", "1980s", "1990s"], "answer": "1960s"},
    {"section": "Fashion History", "question": "Who is the designer of the 'New Look'?", 
     "options": ["Coco Chanel", "Christian Dior", "Yves Saint Laurent", "Vivienne Westwood"], "answer": "Christian Dior"},
    {"section": "Fashion History", "question": "Which fabric was primarily used in Victorian dresses?", 
     "options": ["Cotton", "Silk", "Wool", "Polyester"], "answer": "Silk"},
    {"section": "Fashion History", "question": "Who created the iconic wrap dress?", 
     "options": ["Diane von Furstenberg", "Coco Chanel", "Betsey Johnson", "Giorgio Armani"], "answer": "Diane von Furstenberg"},
    {"section": "Fashion History", "question": "Which style is associated with the 1920s flapper?", 
     "options": ["Baggy trousers", "Short skirts & fringe dresses", "Padded shoulders", "Pencil skirts"], "answer": "Short skirts & fringe dresses"},
    {"section": "Fashion History", "question": "Who is known for the little black dress?", 
     "options": ["Coco Chanel", "Vivienne Westwood", "Christian Dior", "Yves Saint Laurent"], "answer": "Coco Chanel"},
    {"section": "Fashion History", "question": "Which era popularized bell-bottom pants?", 
     "options": ["1960s-70s", "1950s", "1980s", "1990s"], "answer": "1960s-70s"},
    {"section": "Fashion History", "question": "The punk fashion movement started in which country?", 
     "options": ["USA", "UK", "France", "Germany"], "answer": "UK"},
    {"section": "Fashion History", "question": "Which designer is famous for colorful geometric patterns in the 1960s?", 
     "options": ["Pierre Cardin", "Jean Paul Gaultier", "Versace", "Dior"], "answer": "Pierre Cardin"},
    {"section": "Fashion History", "question": "What accessory is iconic to Audrey Hepburn's style in 'Breakfast at Tiffany's'?", 
     "options": ["Pearl necklace", "Hat", "Sunglasses", "Scarf"], "answer": "Pearl necklace"},
    
    # Section 2: Music Genres
    {"section": "Music Genres", "question": "Which genre is associated with jazz improvisation?", 
     "options": ["Hip-Hop", "Jazz", "Rock", "Pop"], "answer": "Jazz"},
    {"section": "Music Genres", "question": "Which genre is Tupac Shakur most associated with?", 
     "options": ["Rap", "Country", "Jazz", "Rock"], "answer": "Rap"},
    {"section": "Music Genres", "question": "Which genre originated in the Mississippi Delta?", 
     "options": ["Blues", "Reggae", "Classical", "Pop"], "answer": "Blues"},
    {"section": "Music Genres", "question": "Which genre is characterized by heavy electric guitar riffs?", 
     "options": ["Jazz", "Rock", "Hip-Hop", "Folk"], "answer": "Rock"},
    {"section": "Music Genres", "question": "Which genre emerged from Jamaican dance halls in the 1960s?", 
     "options": ["Reggae", "Disco", "Metal", "Jazz"], "answer": "Reggae"},
    {"section": "Music Genres", "question": "EDM stands for what?", 
     "options": ["Electronic Dance Music", "Electric Disco Music", "Experimental Digital Music", "Electronic Drum Music"], "answer": "Electronic Dance Music"},
    {"section": "Music Genres", "question": "Which genre is Billie Holiday famous for?", 
     "options": ["Jazz", "Rock", "Pop", "Hip-Hop"], "answer": "Jazz"},
    {"section": "Music Genres", "question": "Which genre is associated with rapping and DJing?", 
     "options": ["Rap", "Blues", "Classical", "Country"], "answer": "Rap"},
    {"section": "Music Genres", "question": "Grunge music is most associated with which decade?", 
     "options": ["1980s", "1990s", "2000s", "1970s"], "answer": "1990s"},
    {"section": "Music Genres", "question": "Which genre is known for improvisation and swing rhythm?", 
     "options": ["Jazz", "Pop", "Rock", "Hip-Hop"], "answer": "Jazz"},
    
    # Section 3: Fashion & Music
    {"section": "Fashion & Music", "question": "Which music movement inspired studded leather jackets in the 1970s?", 
     "options": ["Punk", "Hip-Hop", "Disco", "Grunge"], "answer": "Punk"},
    {"section": "Fashion & Music", "question": "Which pop star influenced leather jackets & skinny jeans in the 1980s?", 
     "options": ["Madonna", "Michael Jackson", "Prince", "Cyndi Lauper"], "answer": "Michael Jackson"},
    {"section": "Fashion & Music", "question": "Which 1990s music style brought back flannel shirts as fashion?", 
     "options": ["Grunge", "Hip-Hop", "Pop", "R&B"], "answer": "Grunge"},
    {"section": "Fashion & Music", "question": "The hip-hop culture in the 1980s popularized which fashion item?", 
     "options": ["Baggy pants", "Mini skirts", "Platform shoes", "Bowler hats"], "answer": "Baggy pants"},
    {"section": "Fashion & Music", "question": "Which designer worked with Madonna to create stage outfits in the 1980s?", 
     "options": ["Jean Paul Gaultier", "Versace", "Armani", "Dior"], "answer": "Jean Paul Gaultier"},
    {"section": "Fashion & Music", "question": "Which footwear became iconic for hip-hop artists in the 1980s?", 
     "options": ["Air Jordans", "Converse", "Loafers", "Boots"], "answer": "Air Jordans"},
    {"section": "Fashion & Music", "question": "Which British music genre influenced Vivienne Westwood’s punk designs?", 
     "options": ["Punk Rock", "Disco", "Pop", "Jazz"], "answer": "Punk Rock"},
    {"section": "Fashion & Music", "question": "MTV in the 1980s helped popularize which fashion trend?", 
     "options": ["Bold colors & big hair", "Flapper dresses", "Tweed suits", "Minimalism"], "answer": "Bold colors & big hair"},
    {"section": "Fashion & Music", "question": "Which 1970s disco trend influenced fashion?", 
     "options": ["Bell-bottom pants & sequins", "Plaid shirts", "Baggy pants", "Leather jackets"], "answer": "Bell-bottom pants & sequins"},
    {"section": "Fashion & Music", "question": "Which rapper helped make gold chains a mainstream fashion accessory?", 
     "options": ["Run DMC", "Tupac", "Jay-Z", "Eminem"], "answer": "Run DMC"}
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
        feedback_label.config(text=f"Incorrect! Answer: {q_data['answer']}", fg="red")
    for btn in option_buttons:
        btn.config(state=tk.DISABLED)
    current_question += 1
    root.after(1000, show_question)

def end_quiz():
    section_summary = "\n".join([f"{sec}: {s} points" for sec, s in section_scores.items()])
    messagebox.showinfo("Quiz Complete", f"{player_name}, your total score is {score} / {len(filtered_data)}\n\nSection Scores:\n{section_summary}")
    root.destroy()

# --- GUI Setup ---
root = tk.Tk()
root.title("Fashion & Music Quiz")
root.geometry("700x500")

# Greetings
welcome_label = tk.Label(root, text="Welcome to the Fashion & Music Quiz!", font=("Arial", 16))
welcome_label.pack(pady=20)
instructions_label = tk.Label(root, text="Enter your name, select a section, and answer the questions.", font=("Arial", 14))
instructions_label.pack(pady=10)

# Name input
name_label = tk.Label(root, text="Enter your name:", font=("Arial", 14))
name_label.pack(pady=10)
name_entry = tk.Entry(root, font=("Arial", 14))
name_entry.pack(pady=5)
name_button = tk.Button(root, text="Start", font=("Arial", 14), command=lambda: save_name())
name_button.pack(pady=10)

def save_name():
    global player_name
    player_name = name_entry.get() if name_entry.get() != "" else "Player"
    start_quiz()

# Section selection
section_choice_label = tk.Label(root, text="Choose a section:", font=("Arial", 14))
section_buttons = []
for sec in ["Fashion History", "Music Genres", "Both"]:
    btn = tk.Button(root, text=sec, font=("Arial", 14), width=20, command=lambda s=sec: choose_section(s))
    section_buttons.append(btn)

# Quiz widgets
section_label = tk.Label(root, text="", font=("Arial", 14))
section_label.pack(pady=10)
question_label = tk.Label(root, text="", font=("Arial", 16), wraplength=600)
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

root.mainloop()
