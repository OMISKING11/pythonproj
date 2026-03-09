import random
import tkinter as tk
from tkinter import messagebox

# Updated dictionary with the first 20 elements and other important ones
elements = {
    "Hydrogen (H)": 1,
    "Helium (He)": 4,
    "Lithium (Li)": 7,
    "Beryllium (Be)": 9,
    "Boron (B)": 11,
    "Carbon (C)": 12,
    "Nitrogen (N)": 14,
    "Oxygen (O)": 16,
    "Fluorine (F)": 19,
    "Neon (Ne)": 20,
    "Sodium (Na)": 23,
    "Magnesium (Mg)": 24,
    "Aluminum (Al)": 27,
    "Silicon (Si)": 28,
    "Phosphorus (P)": 31,
    "Sulfur (S)": 32,
    "Chlorine (Cl)": 35.5,
    "Argon (Ar)": 40,
    "Potassium (K)": 39,
    "Calcium (Ca)": 40,
    "Iron (Fe)": 56,
    "Copper (Cu)": 63.5,
    "Zinc (Zn)": 65,
    "Silver (Ag)": 108,
    "Barium (Ba)": 137,
    "Gold (Au)": 197,
    "Lead (Pb)": 207,
}

class ElementQuiz:
    def __init__(self, master):
        self.master = master
        self.master.title("Element Quiz")
        self.master.geometry("1000x600")  # Increased window size
        self.score = 0
        self.current_element = ""
        
        self.score_label = tk.Label(master, text="Score: 0", font=("Arial", 24))  # Increased font size
        self.score_label.pack(pady=20)

        self.question_label = tk.Label(master, text="", font=("Arial", 22))  # Increased font size
        self.question_label.pack(pady=20)

        self.buttons_frame = tk.Frame(master)
        self.buttons_frame.pack(pady=20)

        self.option_buttons = []
        for i in range(4):
            button = tk.Button(self.buttons_frame, text="", font=("Arial", 18), width=12, height=3,  # Increased button size
                               command=lambda b=i: self.check_answer(b))
            button.grid(row=0, column=i, padx=20)
            self.option_buttons.append(button)

        self.next_question()  # Load the first question

    def next_question(self):
        self.current_element, correct_mass = random.choice(list(elements.items()))
        options = [correct_mass]
        
        # Generate 3 random incorrect options, mixing integers and floats
        while len(options) < 4:
            incorrect_mass = random.choice([round(random.uniform(1, 210), 1), random.randint(1, 210)])
            if incorrect_mass not in options:
                options.append(incorrect_mass)

        random.shuffle(options)

        self.question_label.config(text=f"What is the atomic mass of {self.current_element}?")
        for i, option in enumerate(options):
            self.option_buttons[i].config(text=str(option), state=tk.NORMAL)

    def check_answer(self, selected_index):
        correct_mass = elements[self.current_element]
        selected_mass = float(self.option_buttons[selected_index].cget("text"))

        if selected_mass == correct_mass:
            self.score += 1
            messagebox.showinfo("Correct!", f"Well done! Your score: {self.score}")
        else:
            messagebox.showerror("Incorrect", f"The correct atomic mass is {correct_mass} u.")

        self.score_label.config(text=f"Score: {self.score}")  # Update score display
        for button in self.option_buttons:
            button.config(state=tk.DISABLED)  # Disable buttons after answering

        # Load the next question after a short delay
        self.master.after(1000, self.next_question)  # 1-second delay

if __name__ == "__main__":
    root = tk.Tk()
    quiz = ElementQuiz(root)
    root.mainloop()
