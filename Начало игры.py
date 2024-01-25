from tkinter import Tk, Button, Entry, Label

root = Tk()
root.title("Scrabble")
root.geometry("400x300")

def calculate_score():
    word = entry.get()
    score = 0
    for letter in word:
        if letter in ['н', 'е', 'а', 'и', 'о', '', '', '', 't', 'u']:
            score += 1
        elif letter in ['д', 'м', 'т', 'й', 'л', 'в', 'р']:
            score += 2
        elif letter in ['я', 'г', '', '']:
            score += 3
        elif letter in ['f', 'h', 'v', 'w', 'y']:
            score += 4
        elif letter == ['ь', 'х', 'ч', 'ы']:
            score += 5
        elif letter in ['', '']:
            score += 8
        elif letter in ['ц', '']:
            score += 10
    score_label.config(text="Score: " + str(score))

entry = Entry(root)
entry.pack()

score_button = Button(root, text="Calculate Score", command=calculate_score)
score_button.pack()

score_label = Label(root, text="Score: ")
score_label.pack()

root.mainloop()

