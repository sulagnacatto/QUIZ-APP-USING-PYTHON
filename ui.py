from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
QUIZ_FONT = ("Arial", 20, "italic")


class Interface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizz Time")
        self.window.config(padx=20, pady=20,bg=THEME_COLOR)
        #self.window.iconphoto(True, PhotoImage(file="quiz_pig.png")) doubt
        self.score_label = Label(text="Score: 0", fg="white", bg=THEME_COLOR)
        self.score_label.grid(row=0, column=1)

        self.canvas = Canvas(height=200, width=400, bg="white")
        self.question_text = self.canvas.create_text(200, 100, width=280, text="meow meow", fill=THEME_COLOR, font=QUIZ_FONT)
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        true_img = PhotoImage(file="images/true.png")
        self.true_answer = Button(image=true_img, highlightthickness=0, command=self.true_press)
        self.true_answer.grid(row=2, column=1)

        false_img = PhotoImage(file="images/false.png")
        self.false_answer = Button(image=false_img, highlightthickness=0, command=self.false_press)
        self.false_answer.grid(row=2, column=0)

        self.get_the_next_question()  # Call the method to get the first question

        self.window.mainloop()

    def get_the_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score: {self.quiz.score}")  # Corrected method name
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text=f"THE END")
            self.true_answer.config(state="disabled")
            self.false_answer.config(state="disabled")

    def true_press(self):
        is_right = self.quiz.check_answer("True")
        self.give_feedback(is_right)

    def false_press(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.configure(bg="green")
        else:
            self.canvas.configure(bg="red")
        self.window.after(1000, self.get_the_next_question)  # Corrected method name
