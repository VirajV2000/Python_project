from tkinter import *
import pygame

root=Tk()
root.title("Tansen : Music player")
root.geometry("500x300")


#initialize the pygame mixer
pygame.mixer.init()

#craete a playlist box
sound_box=Listbox(root,bg="black",fg="green",width=60)
sound_box.pack(pady=30)


#define a photoimage
back_btn_img=PhotoImage(file='images/back50.png')
forward_btn_img=PhotoImage(file='images/forward50.png')
pause_btn_img=PhotoImage(file='images/pause50.png')
play_btn_img=PhotoImage(file='images/play50.png')
stop_btn_img=PhotoImage(file='images/stop50.png')

root.mainloop()
