import subprocess
import sys
import tkinter


try:
    from PIL import Image, ImageTk
except:
    subprocess.check_call([sys.executable, "-m", "pip", "install", "pillow"])




main_window = tkinter.Tk()
main_window.title("SECRET NOTES")
main_window.config(background="#c6c6be")
main_window.maxsize(350,800)
main_window.minsize(350,800)


snake_image = Image.open("secretnotes.jpeg")
resized_snake = snake_image.resize((350,350))
photo = ImageTk.PhotoImage(resized_snake)


label_widget_photo = tkinter.Label()
label_widget_photo.config(image=photo, width=350, height=350)
label_widget_photo.pack()


label_widget_1 = tkinter.Label(text="ENTER TITLE FOR NOTE TO ENCRYPT")
label_widget_1.config(font="Bold", background="#c6c6be")
label_widget_1.pack()


entry_widget_1 = tkinter.Entry()
entry_widget_1.pack()


label_widget_2 = tkinter.Label(text="ENTER NOTE THAT WILL ENCRYPT")
label_widget_2.config(font="Bold", background="#c6c6be")
label_widget_2.pack()


label_widget_text = tkinter.Text()
label_widget_text.config(height=10)
label_widget_text.pack()


label_widget_3 = tkinter.Label(text="ENTER YOUR MASTER KEYWORD") #THAT WILL ENCRYPT YOUR TEXT")
label_widget_3.config(font="Bold", background="#c6c6be")
label_widget_3.pack()


label_widget_4 = tkinter.Label(text="THAT WILL ENCRYPT YOUR TEXT")
label_widget_4.config(font="Bold", background="#c6c6be")
label_widget_4.pack()


entry_widget_2 = tkinter.Entry()
entry_widget_2.pack()

def title_save():
    file_name = "data_file"
    try:
        with open(file_name, "r"):
            with open(file_name, "a") as stored_file:
                stored_file.write(entry_widget_1.get()+"\n")
                stored_file.write(label_widget_text.get("1.0","end-1c")+"\n")

    except FileNotFoundError:
        with open(file_name, "w") as stored_file:
            stored_file.write(entry_widget_1.get()+"\n")
            stored_file.write(label_widget_text.get("1.0","end-1c" )+"\n")


encrypt_button = tkinter.Button()
encrypt_button.config(text="Encrypt And Save", command=title_save)
encrypt_button.pack()


decrypt_button = tkinter.Button()
decrypt_button.config(text="Decrypt")
decrypt_button.pack()



main_window.mainloop()
