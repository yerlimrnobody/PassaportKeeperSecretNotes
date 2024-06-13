import subprocess
import sys
import tkinter
from tkinter import messagebox


try:
    from PIL import Image, ImageTk
    from cryptography.fernet import Fernet
    import base64
    import hashlib

except:
    subprocess.check_call([sys.executable, "-m", "pip", "install", "pillow"])
    subprocess.check_call([sys.executable, "-m", "pip", "install", "cryptography"])
    subprocess.check_call([sys.executable, "-m", "pip", "install", "base64"])
    subprocess.check_call([sys.executable, "-m", "pip", "install", "hashlib"])



main_window = tkinter.Tk()
main_window.title("SECRET NOTES")
main_window.config(background="#c6c6be")
main_window.maxsize(350,740)
main_window.minsize(350,740)


snake_image = Image.open("secretnotes.jpeg")
resized_snake = snake_image.resize((350,350))
photo = ImageTk.PhotoImage(resized_snake)


label_widget_photo = tkinter.Label()
label_widget_photo.config(image=photo, width=350, height=350)
label_widget_photo.pack()


label_widget_1 = tkinter.Label(text="ENTER A NOTE TO REMEMBER")
label_widget_1.config(font="Bold", background="#c6c6be")
label_widget_1.place(x=47, y=320)


entry_widget_1 = tkinter.Entry()
entry_widget_1.place(x=10, y=350, width=330)


label_widget_2 = tkinter.Label(text="ENTER INFO THAT WILL BE ENCRYPTED")
label_widget_2.config(font="Bold", background="#c6c6be")
label_widget_2.place(x=15, y=375)


label_widget_text = tkinter.Text()
label_widget_text.config(height=10)
label_widget_text.place(y=400)


label_widget_3 = tkinter.Label(text="ENTER YOUR MASTER KEYWORD")
label_widget_3.config(font="Bold", background="#c6c6be")
label_widget_3.place(x=40, y=580)


label_widget_4 = tkinter.Label(text="THAT WILL ENCRYPT YOUR INFO")
label_widget_4.config(font="Bold", background="#c6c6be")
label_widget_4.place(x=40, y=600)


entry_widget_2 = tkinter.Entry()
entry_widget_2.config(show="*")
entry_widget_2.place(x=10, y=620, width=330)

def generate_fernet_key(password):

    hashed_password = hashlib.sha256(password.encode()).digest()
    fernet_key = base64.urlsafe_b64encode(hashed_password)
    return fernet_key

def encrypt_string():
    your_key = entry_widget_2.get()
    try:
        fernet_key = generate_fernet_key(your_key)
        fernet_crypt = Fernet(fernet_key)
        get_text_to_crypt = label_widget_text.get("1.0", "end-1c")
        encrypted_text = fernet_crypt.encrypt(get_text_to_crypt.encode())
        encrypted_out_of_function = encrypted_text.decode()
        #print(f"Şifrelenmiş Metin: {encrypted_text.decode()}")
        return encrypted_out_of_function
    except Exception as e:
        messagebox.showinfo("Oops !","Wrong Key Type")

def decrypt_string():
    your_key = entry_widget_2.get()
    try:
        fernet_key = generate_fernet_key(your_key)
        fernet_crypt = Fernet(fernet_key)
        get_text_to_decrypt = label_widget_text.get("1.0", "end-1c")
        decrypted_text = fernet_crypt.decrypt(get_text_to_decrypt.encode()).decode()
        label_widget_text.delete("1.0",tkinter.END)
        label_widget_text.insert("1.0",decrypted_text)

    except Exception as e:
        messagebox.showinfo("Oops !","Wrong Key or Wrong String")


def title_save():
    if not entry_widget_1.get() or not entry_widget_2.get():
        messagebox.showinfo("Oops !","Please Enter Your Key, Your Title and String")

    else:

        file_name = "data_file"
        try:
            with open(file_name, "r"):
                with open(file_name, "a") as stored_file:
                    stored_file.write(entry_widget_1.get()+"\n")
                    encrypted_string = encrypt_string()
                    stored_file.write(encrypted_string + "\n")

        except FileNotFoundError:
            with open(file_name, "w") as stored_file:
                stored_file.write(entry_widget_1.get()+"\n")
                encrypted_string = encrypt_string()
                stored_file.write(encrypted_string + "\n")


def clear_all():
    entry_widget_1.delete(first=0, last=tkinter.END)
    label_widget_text.delete("1.0","end-1c")
    entry_widget_2.delete(first=0, last=tkinter.END)


encrypt_button = tkinter.Button()
encrypt_button.config(text="Encrypt And Save", command=title_save)
encrypt_button.place(x=10, y=650, width=160)


decrypt_button = tkinter.Button()
decrypt_button.config(text="Decrypt", command=decrypt_string)
decrypt_button.place(x=180, y=650, width=160)

clear_button = tkinter.Button()
clear_button.config(text="CLEAR ALL", command=clear_all)
clear_button.place(x=10, y=690, width=330)



main_window.mainloop()
