import customtkinter as ctk
from PIL import Image

class QuizDisplay:
    def __init__(self, root, game):
        self.root = root
        self.game = game

        self.root.title("車クイズ")
        self.root.geometry("600x600")

        self.title = ctk.CTkLabel(
            root,
            text="車クイズ",
            font=("Arial", 28)
        )
        self.title.pack(pady=20)

        self.question_label = ctk.CTkLabel(
            root,
            text="",
            font=("Arial", 20)
        )
        self.question_label.pack(pady=10)

        self.image_label = ctk.CTkLabel(root, text="")
        self.image_label.pack(pady=10)

        self.buttons = []

        for i in range(4):
            button = ctk.CTkButton(
                root,
                text="",
                width=300,
                height=40,
                command=lambda index=i: self.game.check_answer(index)
            )
            button.pack(pady=5)
            self.buttons.append(button)

        self.result_label = ctk.CTkLabel(
            root,
            text="",
            font=("Arial", 18)
        )
        self.result_label.pack(pady=10)

        self.next_button = ctk.CTkButton(
            root,
            text="次の問題へ",
            command=self.game.next_question
        )
        self.next_button.pack(pady=10)

        self.show_question()

    def show_question(self):
        question = self.game.get_question()

        self.question_label.configure(
            text=question["question"]
        )

        for i, choice in enumerate(question["choices"]):
            self.buttons[i].configure(
                text=choice,
                state="normal"
            )

        self.result_label.configure(text="")

        try:
            image = Image.open(question["image"])
            image = image.resize((300, 180))
            self.photo = ctk.CTkImage(
                light_image=image,
                dark_image=image,
                size=(300, 180)
            )
            self.image_label.configure(image=self.photo)
        except FileNotFoundError:
            self.image_label.configure(
                image=None,
                text="画像がありません"
            )

    def show_result(self, correct):
        if correct:
            self.result_label.configure(
                text="正解！",
                text_color="green"
            )
        else:
            self.result_label.configure(
                text="不正解！",
                text_color="red"
            )

        for button in self.buttons:
            button.configure(state="disabled")

    def show_final_score(self, score, total):
        self.question_label.configure(
            text=f"クイズ終了！\n{total}問中{score}問正解"
        )

        self.image_label.configure(image=None, text="")

        for button in self.buttons:
            button.pack_forget()

        self.next_button.configure(
            text="終了",
            state="disabled"
        )

        self.result_label.configure(text="")