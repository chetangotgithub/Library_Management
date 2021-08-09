from tkinter import *
from PIL import ImageTk,Image #PIL -> Pillow
import mysql.connector
from tkinter import messagebox
from AddBook import *
from ViewBooks import *
from DeleteBook import *
from IssueBook import *
from ReturnBook import *
root =Tk()
root.title("Library")
root.minsize(width=900,height=670)
root.geometry("600x500")
same = True
n = 4
# Adding a background image
background_image = Image.open("lib.jpg")
[imageSizeWidth, imageSizeHeight] = background_image.size
newImageSizeWidth = int(imageSizeWidth * n)
if same:
    newImageSizeHeight = int(imageSizeHeight * n)
else:
    newImageSizeHeight = int(imageSizeHeight / n)

background_image = background_image.resize((newImageSizeWidth, newImageSizeHeight), Image.ANTIALIAS)
img = ImageTk.PhotoImage(background_image)
Canvas1 = Canvas(root)
Canvas1.create_image(300, 340, image=img)
Canvas1.config(bg="white", width=600, height=600)
Canvas1.pack(expand=True, fill=BOTH)
headingFrame1 = Frame(root,bg="#FFBB00",bd=5)
headingFrame1.place(relx=0.2,rely=0.1,relwidth=0.6,relheight=0.16)
headingLabel = Label(headingFrame1, text="Welcome to \n Vidyalankar Library", bg='#4C342F', fg='white',font=('Courier',15))
headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)
btn1 = Button(root, text="Add Book Details", bg='#4C342F', fg='#F1F407',command=lambda :addBook())
btn1.place(relx=0.28, rely=0.4, relwidth=0.45, relheight=0.1)

btn2 = Button(root, text="Delete Book", bg='#4C342F', fg='#F1F407',command=lambda :delete())
btn2.place(relx=0.28, rely=0.5, relwidth=0.45, relheight=0.1)

btn3 = Button(root, text="View Book List", bg='#4C342F', fg='#F1F407',command=lambda :View())
btn3.place(relx=0.28, rely=0.6, relwidth=0.45, relheight=0.1)

btn4 = Button(root, text="Issue Book to Student", bg='#4C342F', fg='#F1F407',command=lambda :issueBook())
btn4.place(relx=0.28, rely=0.7, relwidth=0.45, relheight=0.1)

btn5 = Button(root, text="Return Book", bg='#4C342F', fg='#F1F407',command=lambda :returnBook())
btn5.place(relx=0.28, rely=0.8, relwidth=0.45, relheight=0.1)
root.mainloop()

