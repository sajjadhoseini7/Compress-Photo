from tkinter import ttk
from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
from PIL import Image, ImageDraw, ImageFont
import os, time

root =Tk()
root.title('Compress Photos')
root.resizable(0,0)
displaycanvas = Canvas(root,width = 320, height = 150)
displaycanvas.pack()

def app_guide():
    messagebox.showinfo('app guide','''
1. Click on Choose your pictures' folder path and choose the wanted folder
2. Click on Choose a folder path to save compressed images
3. Click on Compress to start the process
''')
def app_creator():
    messagebox.showinfo('app creator','This app is created by Sajjad Hoseini & all rights reserved.')

menubar= Menu(root)
creditmenu=Menu(menubar,tearoff=0)
creditmenu.add_command(label='How to use the app?',command=app_guide)
creditmenu.add_separator()
creditmenu.add_command(label='Credit',command=app_creator)
menubar.add_cascade(label='Menu',menu=creditmenu)
root.config(menu=menubar)

textbox = Text(root,height=10,width=36)
textbox.pack(side='left',fill=Y)
scroll_bar=Scrollbar(root)
scroll_bar.pack(side='right',fill=Y)
textbox.configure(yscrollcommand=scroll_bar.set)
scroll_bar.configure(command=textbox.yview)

def browse_files_folder():
    folder_dir = filedialog.askdirectory(
        initialdir="/", 
    )
    if folder_dir:
        op_entry.delete(0,END)
        op_entry.insert(0,folder_dir)
        
op_var=StringVar()
op_entry=Entry(root,textvariable=op_var,width=50)
op_entry.place(x=10,y=35)
ttk.Button(root, text="Choose your pictures' folder path", command=browse_files_folder).place(x=10,y=10)

def browse_folder_to_save():
    folder_dir = filedialog.askdirectory(
        initialdir="/",  # Optional: Set initial directory
    )
    if folder_dir:
        cp_entry.delete(0,END)
        cp_entry.insert(0,folder_dir)
        
cp_var=StringVar()
cp_entry=Entry(root,textvariable=cp_var,width=50)
cp_entry.place(x=10,y=90)
ttk.Button(root, text="Choose a folder path to save compressed images", command=browse_folder_to_save).place(x=10,y=65)

def compress():
    t1 = time.time()
    folder_path = op_var.get()
    image_extensions = ('.jpg', '.JPG','.JPEG','.jpeg','png','PNG')
    compressed_pics_path=cp_var.get()
    i=1
    length = len(os.listdir(folder_path))
    textbox.configure(state=NORMAL)
    textbox.delete('1.0',END)
    textbox.tag_configure('left',justify='left',font=('Times New Roman',10))
    textbox.insert(END,length)
    textbox.insert(END,'\n')
    textbox.tag_add('left',1.0,'end')
    root.update()
    for filename in os.listdir(folder_path):
        if filename.lower().endswith(image_extensions):
            image_path = os.path.join(folder_path, filename)
            im = Image.open(image_path)
            draw = ImageDraw.Draw(im)
            im.save(f'{compressed_pics_path}\compressed {filename}')
            percent = round((i/length*100),2)
            textbox.insert(END,f'{filename}, Percentage completed: {percent}%')
            textbox.insert(END,'\n')
            textbox.tag_add('left',1.0,'end')
            i+=1
            root.update()
    t2 = time.time()
    exec_time = round(t2-t1,2)
    textbox.insert(END,f'Execution time: {exec_time} seconds')
    textbox.tag_add('left',1.0,'end')
    textbox.configure(state=DISABLED)
    root.update()

ttk.Button(root ,text = "Compress" ,command=compress).place(x=115,y=120)

root.mainloop()

#author: Sajjad Hoseini
