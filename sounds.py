from tkinter import *
import pygame

root=Tk()
root.title("Tansen: Music Player")
root.geometry("500x400")

pygame.mixer.init()

def play():
	pygame.mixer.music.load("audio/Attention.mp3")
	pygame.mixer.music.play(loops=0)

def stop():
	pygame.mixer.music.stop()
myButton=Button(root,text="Play song",command=play,font=("Helvetica",32))
myButton.pack(pady=40)

stop_button=Button(root,text="stop",command=stop)
stop_button.pack(pady=20)


root.mainloop()
