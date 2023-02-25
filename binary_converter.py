import tkinter as tk 
import os
os.system('Xvfb :1 -screen 0 1600x1200x16  &')    # create virtual display with size 1600x1200 and 16 bit color. Color can be changed to 24 or 8
os.environ['DISPLAY']=':1.0'    # tell X clients to use our virtual DISPLAY :1.0.

if os.environ.get('DISPLAY','') == '':
    print('no display found. Using :0.0')
    os.environ.__setitem__('DISPLAY', ':0.0')

def convert_binary(binary):
    """Converts a single binary string to decimal"""
    output = 0
    pos = 0
    for digit in reversed(str(binary)):
        if digit == '1':
            output += 2**pos
        pos += 1
    print(output)
    return output

def convert_decimal(decimal):
    output = ''
    while decimal != 0:
        output += str(decimal % 2)
        decimal //= 2
    output = output[::-1]
    print(output)
    return output

convert_decimal(172)

class App:
    root = None
    
    def __init__(self, input_root):
        App.root = input_root
        App.root.geometry("350x200")
        App.root.title("Binary-Decimal Converter")
        box_label = tk.Label(App.root, text="Input number:")
        self.input_box = tk.Entry(App.root, font=(50))
        convert_decimal_button = tk.Button(App.root, text="Convert_Decimal", command= lambda:self.print_conversion())
        box_label.pack()
        self.input_box.pack()
        convert_decimal_button.pack()

    def print_conversion(self):
        value = self.input_box.get()
        value = convert_decimal(int(value))
        print(value)
        


if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()