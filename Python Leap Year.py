# Pierce Brooks
# This program informs the user of leap years
# The reult is displayed in a label
# on the main window.

# Frames allow you to break your window into subwindows
# Widgets can be displayed in different frames

import tkinter

class CheckLeapYearGUI:
    def __init__(self):

        # Create the main window.
        self.main_window = tkinter.Tk()

        # Create three frames to group widgets.
        self.top_frame = tkinter.Frame()
        self.mid_frame = tkinter.Frame()
        self.bottom_frame = tkinter.Frame()

        # Create the widgets for the top frame.
        self.prompt_label = tkinter.Label(self.top_frame,
                    text='Enter a year check:')
        self.year_entry = tkinter.Entry(self.top_frame,
                                        width=10)

        # Pack the top frame's widgets.
        self.prompt_label.pack(side='left')
        self.year_entry.pack(side='left')

        # Create the widgets for the middle frame.
        self.descr_label = tkinter.Label(self.mid_frame,
                                         text="Is it a leap year?")
        
        # We need a StringVar object to associate with
        # an output label. Use the object's set method
        # to store a string of blank characters.
        self.value = tkinter.StringVar()

        # Create a label and associate it with the
        # StringVar object. Any value stored in the
        # StringVar object will automatically be displayed
        # in the label.
        self.year_label = tkinter.Label(self.mid_frame,
                                         textvariable=self.value)

        # Pack the middle frame's widgets.
        self.descr_label.pack(side='left')
        self.year_label.pack(side='left')

        # Create the button widgets for the bottom frame.
        self.calc_button = tkinter.Button(self.bottom_frame,
                                          text='Check Year',
                                          command=self.is_leap_year)
        self.quit_button = tkinter.Button(self.bottom_frame,
                                          text='Quit',
                                          command=self.main_window.destroy)

        # Pack the buttons.
        self.calc_button.pack(side='left')
        self.quit_button.pack(side='left')

        # Pack the frames - will display stacked in the order packed - defaults to side='top'.
        self.top_frame.pack()
        self.mid_frame.pack()
        self.bottom_frame.pack()

        # Enter the tkinter main loop.
        tkinter.mainloop()

    # The convert method is a callback function for
    # the Calculate button.
    
    def is_leap_year(self):
        # Get the value entered by the user into the
        # year_entry widget.
        year = int(self.year_entry.get())

        # Calcualates the leap year.
        if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
            self.value.set("It's a leap year!")
        else:
            self.value.set("It's not a leap year!")

        

# Create an instance of the CheckLeapYearGUI class.
Year_conv = CheckLeapYearGUI()
