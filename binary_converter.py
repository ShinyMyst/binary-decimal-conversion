import tkinter as tk 

def convert_binary(binary):
    """Converts a single binary string to decimal"""
    output = 0
    pos = 0
    for digit in reversed(str(binary)):
        if digit == '1':
            output += 2**pos
        pos += 1
    return output

def convert_decimal(decimal):
    output = ''
    while decimal != 0:
        output += str(decimal % 2)
        decimal //= 2
    output = output[::-1]
    return output

convert_decimal(172)

class App:
    root = None
    
    def __init__(self, input_root):
        App.root = input_root
        App.root.geometry("350x200")
        App.root.title("Binary-Decimal Converter")
        self.prepare_widgets()


    def prepare_widgets(self):
        """Creates and packs all widgets for app."""
        # Create Widgets
        box_label = tk.Label(App.root, text="Input number:")
        self.input_box = tk.Entry(App.root, font=(50))  
        self.output_label = tk.Label(root, text="", font=(50))
        button_frame = tk.Frame(root)
        binary_button = tk.Button(button_frame, text="Binary", command= lambda:self.convert_input("binary"))
        decimal_button = tk.Button(button_frame, text="Decimal", command= lambda:self.convert_input("decimal"))    
        
        # Pack Widgets
        box_label.pack()
        self.input_box.pack()
        button_frame.pack(pady=10)
        binary_button.pack(side="left", padx=10)
        decimal_button.pack(side="left", padx=10)
        self.output_label.pack()


    def convert_input(self, type):
        value = self.input_box.get()
        if value.isdigit():
            if type == "binary":
                output = convert_binary(int(value))
            elif type == "decimal":
                output = convert_decimal(int(value))
        else:
            output = "Error: Invalid Input"
        
        self.output_label.config(text=output)
        


if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()