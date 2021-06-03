from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title('Jai Hind!!!')
root.geometry('1080x720')
root.iconbitmap('india_flag.ico')
root.resizable(1,1)
root.config(bg='black')

top_frame = Frame(root, bg="#FF9933", height=240, width=1080)
middle_frame = Frame(root, bg = "#FFFFFF", height=240, width=1080)
bottom_frame = Frame(root, bg = "#138808", height=240, width=1080)

top_frame.pack(fill=BOTH, expand=False)
middle_frame.pack(fill=BOTH, expand=False)
bottom_frame.pack(fill=BOTH, expand=False)

img = ImageTk.PhotoImage(Image.open("ashoka.png"))
panal = Label(middle_frame, image=img, bg='#FFFFFF')
panal.pack(expand=True)

root.mainloop()