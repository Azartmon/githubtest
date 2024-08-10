import tkinter as tk
from tkinter import messagebox
import time


class TypingSpeedTestApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Typing Speed Test")
        self.sample_text = "The quick brown fox jumps over the lazy dog."
        self.start_time = None
        self.end_time = None

        self.create_widgets()

    def create_widgets(self):
        self.sample_text_label = tk.Label(self.root, text=self.sample_text, wraplength=300, justify="left")
        self.sample_text_label.pack(pady=10)

        self.text_entry = tk.Text(self.root, height=5, width=50, wrap='word')
        self.text_entry.pack(pady=10)
        self.text_entry.bind("<FocusIn>", self.start_timer)

        self.submit_button = tk.Button(self.root, text="Submit", command=self.calculate_wpm)
        self.submit_button.pack(pady=10)

    def start_timer(self, event):
        if not self.start_time:
            self.start_time = time.time()

    def calculate_wpm(self):
        self.end_time = time.time()
        typed_text = self.text_entry.get("1.0", tk.END).strip()
        if not typed_text:
            messagebox.showerror("Error", "Please type the text before submitting.")
            return

        elapsed_time = self.end_time - self.start_time
        word_count = len(typed_text.split())
        wpm = (word_count / elapsed_time) * 60
        self.show_results(wpm)

    def show_results(self, wpm):
        messagebox.showinfo("Results", f"Your typing speed is {wpm:.2f} words per minute.")


if __name__ == "__main__":
    root = tk.Tk()
    app = TypingSpeedTestApp(root)
    root.mainloop()