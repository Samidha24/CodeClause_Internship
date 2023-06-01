import os
from tkinter import *
from PIL import ImageTk, Image
from pygame import mixer

c1 = '#ffffff' #white
c2 = '#354C2B' #dark
c3 = '#859864' #light
c4 = '#333133' #grey
c5 = '#C3CA92'  #lighter

window = Tk()
window.title("")
window.geometry('455x355')
window.configure(background=c1)
window.resizable(width=FALSE, height=FALSE)

#events
def play_music():
    running = listbox.get(ACTIVE)
    running_song['text'] = running
    mixer.music.load(running)
    mixer.music.play()

def pause_music():
    mixer.music.pause()

def continue_music():
    mixer.music.unpause()

def stop_music():
    mixer.music.stop()

def next_music():
    playing = running_song['text']
    index = songs.index(playing)
    size = len(songs)
    new_index = (index % (size-1)) + 1
    playing = songs[new_index]
    mixer.music.load(playing)
    mixer.music.play()

    listbox.delete(0, END)

    show()

    listbox.select_set(new_index)
    running_song['text'] = playing

def prev_music():
    playing = running_song['text']
    index = songs.index(playing)
    new_index = index - 1
    if new_index == 0 :
        new_index = len(songs) - 1

    playing = songs[new_index]
    mixer.music.load(playing)
    mixer.music.play()

    listbox.delete(0, END)

    show()

    listbox.select_set(new_index)
    running_song['text'] = playing

#frames
left_frame = Frame(window, width=200, height=200, bg=c2)
left_frame.grid(row=0, column=0, padx=1, pady=1)

right_frame = Frame(window, width=150, height=300, bg=c4)
right_frame.grid(row=0, column=1, padx=0)

down_frame = Frame(window, width=500, height=250, bg=c3)
down_frame.grid(row=1, column=0, columnspan=3, padx=0, pady=1)

#right frame
listbox = Listbox(right_frame, selectmode=SINGLE, font=("Arial 10 bold"), width=27, height=13, bg=c4, fg=c1)
listbox.grid(row=0, column=0)

w = Scrollbar(right_frame)
w.grid(row=0, column=1)

listbox.config(yscrollcommand=w.set)
w.config(command= listbox.yview)

#images
img_1 = Image.open("C:\\Users\\HP\\Desktop\\Musicplayer\\Pics\\1.png")
img_1 = img_1.resize((170,170))
img_1 = ImageTk.PhotoImage(img_1)
app_image = Label(left_frame, height=200, image= img_1, padx=10, bg=c5)
app_image.place(x=12, y=15)

img_2 = Image.open("C:\\Users\\HP\\Desktop\\Musicplayer\\Pics\\2.png")
img_2 = img_2.resize((60,60))
img_2 = ImageTk.PhotoImage(img_2)
play_button = Button(down_frame, width=60,height=60, image= img_2, padx=10, bg=c1, font=("Ivy 10"), command=play_music)
play_button.place(x=70+20, y=46)

img_3 = Image.open("C:\\Users\\HP\\Desktop\\Musicplayer\\Pics\\3.png")
img_3 = img_3.resize((60,60))
img_3 = ImageTk.PhotoImage(img_3)
prev_button = Button(down_frame, width=60,height=60, image= img_3, padx=10, bg=c1, font=("Ivy 10"), command=prev_music)
prev_button.place(x=20, y=46)

img_4 = Image.open("C:\\Users\\HP\\Desktop\\Musicplayer\\Pics\\4.png")
img_4 = img_4.resize((60,60))
img_4 = ImageTk.PhotoImage(img_4)
next_button = Button(down_frame, width=60,height=60, image= img_4, padx=10, bg=c1, font=("Ivy 10"), command=next_music)
next_button.place(x=140+20, y=46)

img_5 = Image.open("C:\\Users\\HP\\Desktop\\Musicplayer\\Pics\\5.png")
img_5 = img_5.resize((60,60))
img_5 = ImageTk.PhotoImage(img_5)
pause_button = Button(down_frame, width=60,height=60, image= img_5, padx=10, bg=c1, font=("Ivy 10"), command=pause_music)
pause_button.place(x=210+20, y=46)

img_6 = Image.open("C:\\Users\\HP\\Desktop\\Musicplayer\\Pics\\6.png")
img_6 = img_6.resize((60,60))
img_6 = ImageTk.PhotoImage(img_6)
continue_button = Button(down_frame, width=60,height=60, image= img_6, padx=10, bg=c1, font=("Ivy 10"), command=continue_music)
continue_button.place(x=280+20, y=46)

img_7 = Image.open("C:\\Users\\HP\\Desktop\\Musicplayer\\Pics\\7.png")
img_7 = img_7.resize((60,60))
img_7 = ImageTk.PhotoImage(img_7)
stop_button = Button(down_frame, width=60,height=60, image= img_7, padx=10, bg=c1, font=("Ivy 10"), command=stop_music)
stop_button.place(x=350+20, y=46)

line = Label(left_frame, width=200, height=1, padx=10, bg=c3)
line.place(x=0, y=1)

line = Label(left_frame, width=200, height=1, padx=10, bg=c1)
line.place(x=0, y=3)

running_song = Label(down_frame, text="Choose a Song", font=("Ivy 15"), width=70, height=1, padx=10, bg=c1, fg=c2, anchor=NW)
running_song.place(x=0, y=1)

os.chdir(r'C:\Users\HP\Desktop\\Songs')
songs = os.listdir()

def show():
    for i in songs:
        if(".mp3" in i) :
            listbox.insert(END, i)

show()

mixer.init()
music_state = StringVar()
music_state.set("Choose one!")

window.mainloop()