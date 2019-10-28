import face_recognition
from tkinter import filedialog, messagebox
from tkinter import *
from PIL import ImageTk, Image


# Event Handlers
def select_source_image():
    window.sourceFilename = filedialog.askopenfilename(initialdir=".", title="Select Source file",
                                                       filetypes=(("jpeg files", "*.jpg"), ("all files", "*.*")))
    load = Image.open(window.sourceFilename)
    render = ImageTk.PhotoImage(load.resize((100, 100), Image.ANTIALIAS))
    label = Label(window, image=render)
    label.image = render
    label.place(x=200, y=10)


def select_compare_image():
    window.compareFilename = filedialog.askopenfilename(initialdir=".", title="Select Compare file",
                                                        filetypes=(("jpeg files", "*.jpg"), ("all files", "*.*")))
    load = Image.open(window.compareFilename)
    render = ImageTk.PhotoImage(load.resize((100, 100), Image.ANTIALIAS))
    label = Label(window, image=render)
    label.image = render
    label.place(x=200, y=150)


def compare_images():
    if not window.sourceFilename or not window.compareFilename:
        messagebox.showinfo("Facial Recognition", "Please select both files for comparision")
    else:
        known_image = face_recognition.load_image_file(window.sourceFilename)
        unknown_image = face_recognition.load_image_file(window.compareFilename)
        know_encoding = face_recognition.face_encodings(known_image)[0]
        unknown_encoding = face_recognition.face_encodings(unknown_image)[0]
        results = face_recognition.compare_faces([know_encoding], unknown_encoding)
        label = Label(window, text=results)
        label.place(x=200, y=300)



# Create Main Window
window = Tk()
window.title("Facial Recognition")
window.geometry("350x400")
window.compareFilename = ''
window.sourceFilename = ''

# Create Button for select source file
sourceButton = Button(text="Select Source Image", command=select_source_image)
sourceButton.place(x=10, y=10)

# Create Button for select compare file
compareButton = Button(text="Select Face Image", command=select_compare_image)
compareButton.place(x=10, y=150)

# Create Button for select compare file
runButton = Button(text="Compare", command=compare_images)
runButton.place(x=10, y=300)

# Show Main Window
window.mainloop()
