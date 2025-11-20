import tkinter as tk
import random
import string


WIDTH = 800
HEIGHT = 635

...
def hex_to_dec(hex_str):
    dec = int(hex_str,16)
    return str(dec).zfill(6)


def generate_key():
    hex_input = entry_hex.get().upper()
    if len(hex_input) != 5 or not all(c in string.hexdigits for c in hex_input):
        key_label.config(text="请重新输入有效的5位十六进制数")
        return
    dec = hex_to_dec(hex_input)

    block1 = dec[0] + "".join(random.sample(string.ascii_uppercase + string.digits, 4))
    block2 = dec[1] + "".join(random.sample(string.ascii_uppercase + string.digits, 4))
    block3 = dec[2] + "".join(random.sample(string.ascii_uppercase + string.digits, 4)) + " " + dec[4:]
    key = f"{block1}-{block2}-{block3}"
    key_label.config(text=key)



root = tk.Tk()
root.title("变体3 密钥生成器")
root.geometry(f"{WIDTH}x{HEIGHT}")

bg_photo = tk.PhotoImage(file="bg.png")
canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT)
canvas.pack(fill="both", expand=True)
canvas.create_image(0, 0, image=bg_photo, anchor="nw")

entry_hex = tk.Entry(root, width=10, font=("Arial", 14))
entry_hex.place(relx=0.3, rely=0.2, anchor="center")

generate_button = tk.Button(root,text="生成密钥",command=generate_key,font=("Arial", 14))
generate_button.place(relx=0.7, rely=0.2, anchor="center")

key_label = tk.Label(root,text="请输入5位十六进制数并点击生成", font=("Arial", 14))
key_label.place(relx=0.5, rely=0.5, anchor="center")

root.mainloop()
