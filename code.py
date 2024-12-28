# Develop a simulator for a Turing machine that allows users to input

# a Turing machine description and an input string, then simulates the

# execution of the Turing machine on that input. This project can deepen

# understanding of Turing machines and computational complexity.



import tkinter as tk

from tkinter import messagebox



class TuringMachineSimulator(tk.Tk):



    def __init__(self):

        super().__init__()

        self.title("Turing Machine Simulator")

        self.geometry("600x500")

        self.create_welcome_page()



    def create_welcome_page(self):

        self.configure(bg="#1E90FF")  # Set background color to blue



        tk.Label(self, text="Turing Machine Simulator", bg="#1E90FF",

                 fg="white", font=('Helvetica', 32, "bold")).pack(pady=50)



        tk.Button(self, text="Get Started", bg="#FFFACD", font=(

            'sans-serif', 22, "bold"),

            command=self.create_options_page).pack(pady=50)



    def create_options_page(self):

        for widget in self.winfo_children():

            widget.destroy()  # Clear the current page

        self.configure(bg="#ADD8E6")  # Set background color to light blue



        tk.Label(self, text="Select an option:", bg="#ADD8E6",

                 font=('Verdana', 16)).pack(pady=20)



        options = [

            ("String should accept odd one's and even zero's", 0),

            ("String should accept even one's and odd zero's", 1),

            ("String should accept even one's and even zero's", 2),

            ("String should accept odd one's and odd zero's", 3)]

        self.selected_option = tk.IntVar()



        for option, value in options:

            tk.Radiobutton(self, text=option, bg="#ADD8E6", font=(

                'Verdana', 12),

                variable=self.selected_option, value=value).pack(pady=10)



        tk.Button(self, text="Next", bg="#FFFACD", font=(

            'sans-serif', 12),

            command=self.create_input_page).pack(pady=30)



    def create_input_page(self):

        for widget in self.winfo_children():

            widget.destroy()  # Clear the current page



        self.configure(bg="#90EE90")  # Set background color to light green

        tk.Label(self, text="Enter a string:", bg="#90EE90",

                 font=('Verdana', 16)).pack(pady=20)



        self.string_input = tk.Entry(self, font=("Calibri", 14))

        self.string_input.pack(pady=10)



        tk.Button(self, text="Check", bg="#FFFACD", font=(

            'sans-serif', 12),

            command=self.check_string).pack(pady=30)



    def check_string(self):

        string = self.string_input.get()

        option = self.selected_option.get()



        # Use a dictionary to map options to functions for better readability

        option_functions = {

            0: self.accepts_odd_ones_even_zeros,

            1: self.accepts_even_ones_odd_zeros,

            2: self.accepts_even_ones_even_zeros,

            3: self.accepts_odd_ones_odd_zeros

        }



        if option in option_functions:

            result = option_functions[option](string)  # Call the appropriate function

            if result:

                messagebox.showinfo(

                    "Result", f"The string '{string}' is accepted.")

            else:

                messagebox.showinfo(

                    "Result", f"The string '{string}' is not accepted.")



        restart_button = tk.Button(self, text='Restart', font=(

            'sans-serif', 12), command=self.restart)

        restart_button.pack(side="left", padx=115, pady=30)



        exit_button = tk.Button(self, text='Exit', padx=10, font=(

            'sans-serif', 12), command=self.exit)

        exit_button.pack(side="left", padx=125, pady=30)



    def accepts_odd_ones_even_zeros(self, string):

        state = 0

        for symbol in string:

            if state == 0:

                if symbol == '0':

                    state = 2

                elif symbol == '1':

                    state = 1

                else:

                    return False

            elif state == 1:

                if symbol == '0':

                    state = 3

                elif symbol == '1':

                    state = 0

                else:

                    return False

            elif state == 2:

                if symbol == '0':

                    state = 0

                elif symbol == '1':

                    state = 3

                else:

                    return False

            elif state == 3:

                if symbol == '0':

                    state = 1

                elif symbol == '1':

                    state = 2

                else:

                    return False

        return state == 1



    def accepts_even_ones_odd_zeros(self, string):

        state = 0

        for symbol in string:

            if state == 0:

                if symbol == '0':

                    state = 2

                elif symbol == '1':

                    state = 1

                else:

                    return False

            elif state == 1:

                if symbol == '0':

                    state = 3

                elif symbol == '1':

                    state = 0

                else:

                    return False

            elif state == 2:

                if symbol == '0':

                    state = 0

                elif symbol == '1':

                    state = 3

                else:

                    return False

            elif state == 3:

                if symbol == '0':

                    state = 1

                elif symbol == '1':

                    state = 2

                else:

                    return False

        return state == 2



    def accepts_even_ones_even_zeros(self, string):

        state = 0

        for symbol in string:

            if state == 0:

                if symbol == '0':

                    state = 1

                elif symbol == '1':

                    state = 2

                else:

                    return False

            elif state == 1:

                if symbol == '0':

                    state = 0

                elif symbol == '1':

                    state = 3

                else:

                    return False

            elif state == 2:

                if symbol == '0':

                    state = 3

                elif symbol == '1':

                    state = 0

                else:

                    return False

            elif state == 3:

                if symbol == '0':

                    state = 2

                elif symbol == '1':

                    state = 1

                else:

                    return False

        return state == 0



    def accepts_odd_ones_odd_zeros(self, string):

        state = 0

        for symbol in string:

            if state == 0:

                if symbol == '0':

                    state = 2

                elif symbol == '1':

                    state = 1

                else:

                    return False

            elif state == 1:

                if symbol == '0':

                    state = 3

                elif symbol == '1':

                    state = 0

                else:

                    return False

            elif state == 2:

                if symbol == '0':

                    state = 0

                elif symbol == '1':

                    state = 3

                else:

                    return False

            elif state == 3:

                if symbol == '0':

                    state = 1

                elif symbol == '1':

                    state = 2

                else:

                    return False

        return state == 3



    def restart(self):

        for widget in self.winfo_children():

            widget.destroy()  # Clear the current page

        self.create_welcome_page()  # Go back to the welcome page



    def exit(self):

        self.destroy()  # Close the application



if __name__ == '__main__':

    app = TuringMachineSimulator()

    app.mainloop() also this was my project in autoomata to develop simple turing machine


