import pyttsx3
import tkinter as tk
from tkinter import filedialog, messagebox

# Initialize TTS engine with Windows-specific driver
engine = pyttsx3.init('sapi5')
engine.setProperty('rate', 150)
engine.setProperty('volume', 1.0)

# Set a working voice (try different indexes if needed)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)  # Try voices[1] if this doesn't work

# GUI setup
def speak_text():
    text = text_box.get("1.0", tk.END).strip()
    if text:
        try:
            engine.say(text)
            engine.runAndWait()
        except Exception as e:
            messagebox.showerror("Speech Error", f"Could not speak text:\n{e}")
    else:
        messagebox.showwarning("No Text", "Please enter or load some text first.")

def load_file():
    file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])
    if file_path:
        try:
            with open(file_path, "r", encoding="utf-8") as file:
                content = file.read()
                text_box.delete("1.0", tk.END)
                text_box.insert(tk.END, content)
        except Exception as e:
            messagebox.showerror("File Error", f"Could not load file:\n{e}")

# Create window
window = tk.Tk()
window.title("EchoVerse Audiobook Demo")
window.geometry("500x400")

text_box = tk.Text(window, wrap=tk.WORD, font=("Arial", 12))
text_box.pack(padx=10, pady=10, expand=True, fill=tk.BOTH)

btn_frame = tk.Frame(window)
btn_frame.pack(pady=10)

load_btn = tk.Button(btn_frame, text="Load Text File", command=load_file)
load_btn.pack(side=tk.LEFT, padx=10)

speak_btn = tk.Button(btn_frame, text="Speak", command=speak_text)
speak_btn.pack(side=tk.LEFT, padx=10)

window.mainloop()
