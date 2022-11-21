import sys
import tkinter as tk
from tkinter.scrolledtext import ScrolledText
from tkinter import filedialog
import pandas as pd
from threading import Thread
from datetime import datetime, timedelta
from main import send


class Main:
    def __init__(self, master):
        self.master = master

        self.lbl_msg = tk.Label(self.master, text="Message")
        self.lbl_msg.grid(column=0, row=0)

        self.msgFrame = ScrolledText(self.master, height=10, width=48)
        self.msgFrame.place(x=0, y=20)

        self.lbl_phones = tk.Label(self.master, text="Phone Number list (+79999999999)")
        self.lbl_phones.place(x=0, y=205)

        self.phoneFrame = ScrolledText(self.master,height=10, width=48)
        self.phoneFrame.place(x=0, y=230)

        self.open_btn = tk.Button(self.master, text='Open File', command=lambda: Thread(target=self.open).start())
        self.open_btn.place(x=300, y=198)

    
        self.start_btn = tk.Button(self.master, text='Start', command=lambda: Thread(target=self.start).start(), bg='white')
        self.start_btn.place(x=335, y=410)

        self.lbl_time = tk.Label(self.master, text="Time step (in minutes)")
        self.lbl_time.place(x=0, y=410)

        self.time = tk.Entry()
        self.time.place(x=160, y=410)


        

    def start(self):
        self.msgText = self.msgFrame.get('1.0', tk.END)  # Get all text in widget.
        # print(self.msgText)

        self.timeText = int(self.time.get())
        

        self.phoneText = self.phoneFrame.get('1.0', tk.END)  # Get all text in widget.

        plus_minut = 0
        for i in self.phoneText.split('\n'):
            if len(i) > 0:
                plus_minut += self.timeText
                time = datetime.now() + timedelta(minutes=plus_minut)
                Thread(target=send, args=(i, self.msgText, time.hour, time.minute)).start()

    def open(self):
        filename = filedialog.askopenfilename()
        df = pd.read_excel(filename)

        phones = ''
        for i in df.to_dict(orient='records'):
            phones += '+' + str(i['Моб. телефон']) + '\n'

        self.phoneFrame.insert('1.0', phones)

root = tk.Tk()
root.geometry("400x500")
project = Main(root)
root.mainloop()