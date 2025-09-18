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
    # Fashion History
    {"section": "Fashion History", "question": "Which decade popularized the miniskirt?",
     "options": ["1960s", "1970s", "1980s", "1990s"], "answer": "1960s",
     "hint": "Think about the revolutionary 60s fashion.",
     "info": "The miniskirt became a symbol of youth culture and liberation in the 1960s."},
    {"section": "Fashion History", "question": "Who is the designer of the 'New Look'?",
     "options": ["Coco Chanel", "Christian Dior", "Yves Saint Laurent", "Vivienne Westwood"], "answer": "Christian Dior",
     "hint": "Introduced it in 1947.",
     "info": "Dior's 'New Look' emphasized a nipped waist and full skirt, redefining post-war fashion."},
    {"section": "Fashion History", "question": "Which fabric was primarily used in Victorian dresses?",
     "options": ["Cotton", "Silk", "Wool", "Polyester"], "answer": "Silk",
     "hint": "A luxurious and shiny material.",
     "info": "Silk was used in Victorian dresses for its elegance and fine texture."},
    {"section": "Fashion History", "question": "Who created the iconic wrap dress?",
     "options": ["Diane von Furstenberg", "Coco Chanel", "Betsey Johnson", "Giorgio Armani"], "answer": "Diane von Furstenberg",
     "hint": "Known for empowering women through dresses.",
     "info": "The wrap dress became a symbol of independent working women in the 1970s."},
    {"section": "Fashion History", "question": "Which style is associated with the 1920s flapper?",
     "options": ["Baggy trousers", "Short skirts & fringe dresses", "Padded shoulders", "Pencil skirts"], "answer": "Short skirts & fringe dresses",
     "hint": "Think Charleston dance style.",
     "info": "Flapper dresses were short, fringed, and reflected the liberated spirit of women in the 1920s."},
    {"section": "Fashion History", "question": "Who is known for the little black dress?",
     "options": ["Coco Chanel", "Vivienne Westwood", "Christian Dior", "Yves Saint Laurent"], "answer": "Coco Chanel",
     "hint": "French designer known for timeless elegance.",
     "info": "Coco Chanel introduced the little black dress as a symbol of chic simplicity."},
    {"section": "Fashion History", "question": "Which era popularized bell-bottom pants?",
     "options": ["1960s-70s", "1950s", "1980s", "1990s"], "answer": "1960s-70s",
     "hint": "Think hippie and disco eras.",
     "info": "Bell-bottoms became iconic in the 60s-70s counterculture and disco scenes."},
    {"section": "Fashion History", "question": "The punk fashion movement started in which country?",
     "options": ["USA", "UK", "France", "Germany"], "answer": "UK",
     "hint": "Home of the Sex Pistols.",
     "info": "Punk fashion originated in the UK, characterized by leather jackets, spikes, and rebellious style."},
    {"section": "Fashion History", "question": "Which designer is famous for colorful geometric patterns in the 1960s?",
     "options": ["Pierre Cardin", "Jean Paul Gaultier", "Versace", "Dior"], "answer": "Pierre Cardin",
     "hint": "Known for space-age fashion.",
     "info": "Pierre Cardin was known for bold geometric prints and futuristic designs."},
    {"section": "Fashion History", "question": "What accessory is iconic to Audrey Hepburn's style in 'Breakfast at Tiffany's'?",
     "options": ["Pearl necklace", "Hat", "Sunglasses", "Scarf"], "answer": "Pearl necklace",
     "hint": "Classic elegance around the neck.",
     "info": "Audrey Hepburn made the pearl necklace a timeless symbol of elegance."},

    # Music Genres
    {"section": "Music Genres", "question": "Which genre is associated with jazz improvisation?",
     "options": ["Hip-Hop", "Jazz", "Rock", "Pop"], "answer": "Jazz",
     "hint": "Originated in New Orleans.",
     "info": "Jazz is famous for improvisation, swing, and syncopated rhythms."},
    {"section": "Music Genres", "question": "Which genre is Tupac Shakur most associated with?",
     "options": ["Rap", "Country", "Jazz", "Rock"], "answer": "Rap",
     "hint": "90s West Coast artist.",
     "info": "Tupac helped shape modern rap with social and political messages."},
    {"section": "Music Genres", "question": "Which genre originated in the Mississippi Delta?",
     "options": ["Blues", "Reggae", "Classical", "Pop"], "answer": "Blues",
     "hint": "Soulful and emotional roots music.",
     "info": "The blues originated in the Deep South, reflecting African-American experiences."},
    {"section": "Music Genres", "question": "Which genre is characterized by heavy electric guitar riffs?",
     "options": ["Jazz", "Rock", "Hip-Hop", "Folk"], "answer": "Rock",
     "hint": "Classic band setup with drums and guitar.",
     "info": "Rock music features strong rhythms and amplified guitar riffs."},
    {"section": "Music Genres", "question": "Which genre emerged from Jamaican dance halls in the 1960s?",
     "options": ["Reggae", "Disco", "Metal", "Jazz"], "answer": "Reggae",
     "hint": "Bob Marley genre.",
     "info": "Reggae developed from ska and rocksteady and focuses on rhythm and social themes."},
    {"section": "Music Genres", "question": "EDM stands for what?",
     "options": ["Electronic Dance Music", "Electric Disco Music", "Experimental Digital Music", "Electronic Drum Music"], "answer": "Electronic Dance Music",
     "hint": "Popular in nightclubs.",
     "info": "EDM includes house, techno, trance and is designed for dancing."},
    {"section": "Music Genres", "question": "Which genre is Billie Holiday famous for?",
     "options": ["Jazz", "Rock", "Pop", "Hip-Hop"], "answer": "Jazz",
     "hint": "Legendary 1930s-40s singer.",
     "info": "Billie Holiday's expressive voice defined jazz singing."},
    {"section": "Music Genres", "question": "Which genre is associated with rapping and DJing?",
     "options": ["Rap", "Blues", "Classical", "Country"], "answer": "Rap",
     "hint": "Originated in NYC Bronx.",
     "info": "Rap features rhythmic speech, beats, and DJing elements."},
    {"section": "Music Genres", "question": "Grunge music is most associated with which decade?",
     "options": ["1980s", "1990s", "2000s", "1970s"], "answer": "1990s",
     "hint": "Seattle bands like Nirvana.",
     "info": "Grunge influenced fashion with flannel shirts and ripped jeans."},
    {"section": "Music Genres", "question": "Which genre is known for improvisation and swing rhythm?",
     "options": ["Jazz", "Pop", "Rock", "Hip-Hop"], "answer": "Jazz",
     "hint": "Think Duke Ellington.",
     "info": "Jazz improvisation allows musicians to creatively interact in real-time."},

    # Fashion & Music
    {"section": "Fashion & Music", "question": "Which music movement inspired studded leather jackets in the 1970s?",
     "options": ["Punk", "Hip-Hop", "Disco", "Grunge"], "answer": "Punk",
     "hint": "Think rebellious UK bands.",
     "info": "Punk rock influenced fashion with leather, studs, and DIY aesthetics."},
    {"section": "Fashion & Music", "question": "Which pop star influenced leather jackets & skinny jeans in the 1980s?",
     "options": ["Madonna", "Michael Jackson", "Prince", "Cyndi Lauper"], "answer": "Michael Jackson",
     "hint": "Thriller era iconic style.",
     "info": "Michael Jackson's style set trends with leather jackets and unique accessories."},
    {"section": "Fashion & Music", "question": "Which 1990s music style brought back flannel shirts as fashion?",
     "options": ["Grunge", "Hip-Hop", "Pop", "R&B"], "answer": "Grunge",
     "hint": "Seattle bands like Nirvana.",
     "info": "Grunge music popularized flannel shirts, ripped jeans, and casual looks."},
    {"section": "Fashion & Music", "question": "The hip-hop culture in the 1980s popularized which fashion item?",
     "options": ["Baggy pants", "Mini skirts", "Platform shoes", "Bowler hats"], "answer": "Baggy pants",
     "hint": "Loose and comfortable pants.",
     "info": "Hip-hop fashion included oversized clothing, sneakers, and gold chains."},
    {"section": "Fashion & Music", "question": "Which designer worked with Madonna to create stage outfits in the 1980s?",
     "options": ["Jean Paul Gaultier", "Versace", "Armani", "Dior"], "answer": "Jean Paul Gaultier",
     "hint": "Famous French designer.",
     "info": "Gaultier designed Madonna's iconic cone bra and stage outfits."},
    {"section": "Fashion & Music", "question": "Which footwear became iconic for hip-hop artists in the 1980s?",
     "options": ["Air Jordans", "Converse", "Loafers", "Boots"], "answer": "Air Jordans",
     "hint": "Basketball sneakers turned fashion.",
     "info": "Air Jordans became a status symbol in hip-hop culture."},
    {"section": "Fashion & Music", "question": "Which British music genre influenced Vivienne Westwood’s punk designs?",
     "options": ["Punk Rock", "Disco", "Pop", "Jazz"], "answer": "Punk Rock",
     "hint": "Sex Pistols and rebellion.",
     "info": "Westwood's punk designs mirrored the aggressive, anti-establishment spirit of punk rock."},
    {"section": "Fashion & Music", "question": "MTV in the 1980s helped popularize which fashion trend?",
     "options": ["Bold colors & big hair", "Flapper dresses", "Tweed suits", "Minimalism"], "answer": "Bold colors & big hair",
     "hint": "Think 80s pop stars.",
     "info": "MTV music videos influenced young people to adopt vibrant colors and dramatic hairstyles."},
    {"section": "Fashion & Music", "question": "Which 1970s disco trend influenced fashion?",
     "options": ["Bell-bottom pants & sequins", "Plaid shirts", "Baggy pants", "Leather jackets"], "answer": "Bell-bottom pants & sequins",
     "hint": "Glitter and dancing.",
     "info": "Disco culture encouraged flashy clothing with sequins and flared pants."},
    {"section": "Fashion & Music", "question": "Which rapper helped make gold chains a mainstream fashion accessory?",
     "options": ["Run DMC", "Tupac", "Jay-Z", "Eminem"], "answer": "Run DMC",
     "hint": "Old-school hip-hop group.",
     "info": "Run DMC popularized wearing large gold chains as a fashion statement."}
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

#hjhjhggj
def show_question():
    global current_question, lives
    if current_question < len(question_order) and lives > 0:
        idx = question_order[current_question]
        q_data = quiz_data[idx]
        section_label.config(text=f"Section: {q_data['section']}")
        question_label.config(text=q_data["question"])
        hint_label.config(text=f"Hint: {q_data['hint']}")
        for i, option in enumerate(q_data["options"]):
            option_buttons[i].config(text=option, state=tk.NORMAL)
        feedback_label.config(text=f"Lives: {lives} | Attempts left: {attempts_left}")
    else:
        end_quiz()
 
def check_answer(selected):
    global current_question, score, lives, section_scores
    idx = question_order[current_question]
    q_data = quiz_data[idx]

    for btn in option_buttons:
        btn.config(state=tk.DISABLED)

    if selected == q_data["answer"]:
        score += 1
        section_scores[q_data["section"]] += 1
        feedback_label.config(text=f"Correct! {q_data['info']}", fg="green")
    else:
        lives -= 1
        feedback_label.config(text=f"Incorrect! {q_data['info']}", fg="red")

    current_question += 1
    root.after(2000, show_question)

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
    selected_section = sec
    section_selection_frame.pack_forget()
    start_quiz()

# --- GUI Setup ---
root = tk.Tk()
root.title("Fashion & Music Quiz")
root.geometry("700x700")

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

# Quiz Widgets
section_label = tk.Label(root, text="", font=("Arial", 14))
section_label.pack(pady=10)

question_label = tk.Label(root, text="", font=("Arial", 16), wraplength=650)
question_label.pack(pady=10)

hint_label = tk.Label(root, text="", font=("Arial", 12), fg="blue")
hint_label.pack(pady=5)

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


for btn in option_buttons:
    btn.config(state=tk.DISABLED)


root.mainloop()
