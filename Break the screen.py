import tkinter as tk
from random import randint

class BreakingWindow:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Разбивающееся окно")
        
        # Создаем холст
        self.canvas = tk.Canvas(self.root, width=400, height=400, bg='black')
        self.canvas.pack(expand=True, fill='both')
        
        # Создаем кнопку
        self.break_button = tk.Button(self.root, text="Разбить!", command=self.break_pixels)
        self.break_button.place(relx=0.5, rely=0.5, anchor='center')
        
    def break_pixels(self):
        # Получаем размеры холста
        width = self.canvas.winfo_width()
        height = self.canvas.winfo_height()
        
        # Создаем 10 белых пикселей в случайных местах
        for _ in range(10):
            x = randint(0, width-1)
            y = randint(0, height-1)
            self.canvas.create_rectangle(x, y, x+1, y+1, fill='white', outline='white')
    
    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    app = BreakingWindow()
    app.run()
