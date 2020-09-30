import tkinter
from tkinter import ttk
from .character import Character

class PartyTime:
    def __init__(self):
        self.party = []
        self.rations = 0

        self.window = tkinter.Tk()
        self.window.title('Party Time')
        self.window.geometry('350x200')
        
        pwin = ttk.PanedWindow(self.window, orient='vertical')
        self.status_frame = ttk.LabelFrame(pwin, text='Status', height='100')
        self.party_frame = ttk.LabelFrame(pwin, text='Members', height='100')
        pwin.add(self.status_frame)
        pwin.add(self.party_frame)
        pwin.pack(expand=1, fill='both')
        add_char_btn = ttk.Button(self.window, text='Add Character', command=self.add_char)
        add_char_btn.pack()

        self.fill_status_frame()
        self.fill_party_frame()

    def start(self):
        self.window.mainloop()

    def add_char(self):
        char_name = tkinter.StringVar()
        char_con_mod = tkinter.StringVar()

        win = tkinter.Toplevel()
        win.title('Add Character')
        win.geometry('50x100')

        name_lbl = ttk.Label(win, text='Name')
        name_lbl.grid(row=0, sticky='E')

        con_mod_lbl = ttk.Label(win, text='Con Modifier')
        con_mod_lbl.grid(row=1, sticky='E')

        name_fld = ttk.Entry(win, text='Name', textvariable=char_name)
        name_fld.grid(row=0, column=1, padx=5, pady=5)

        con_mod_fld = ttk.Entry(win, text='Con Modifier', textvariable=char_con_mod)
        con_mod_fld.grid(row=1, column=1, padx=5, pady=5)

        ok_btn = ttk.Button(win, text='Okay', command=lambda: self.add_char_ok_click(char_name.get(), char_con_mod.get(), win))
        ok_btn.grid(row=3, column=0, padx=5, pady=5)

        cancel_btn = ttk.Button(win, text='Cancel', command=win.destroy)
        cancel_btn.grid(row=3, column=1, padx=5, pady=5)

    def add_char_ok_click(self, name, con_mod, window):
        self.party.append(Character(name, con_mod))
        window.destroy()
        self.fill_status_frame()
        self.fill_party_frame()

    def clear_frame(self, frame):
        for widget in frame.winfo_children():
            widget.destroy()

    def fill_status_frame(self):
        self.clear_frame(self.status_frame)

        name_col_lbl = ttk.Label(self.status_frame, text='Name', font='TkHeadingFont')
        name_col_lbl.grid(row=0, column=0, padx=5, pady=5, sticky='W')

        no_food_col_lbl = ttk.Label(self.status_frame, text='Days Without Food', font='TkHeadingFont')
        no_food_col_lbl.grid(row=0, column=1, padx=5, pady=5, sticky='W')

        ration_lbl = ttk.Label(self.status_frame, text='Ration', font='TkHeadingFont')
        ration_lbl.grid(row=0, column=2, padx=5, pady=5, sticky='W')

        exh_lvl_lbl = ttk.Label(self.status_frame, text='Exhaustion Level', font='TkHeadingFont')
        exh_lvl_lbl.grid(row=0, column=3, padx=5, pady=5, sticky='W')

        for i, char in enumerate(self.party):
            char_name_lbl = ttk.Label(self.status_frame, text=char.name)
            char_name_lbl.grid(row=i+1, column=0, padx=5, pady=5, sticky='W')

            char_no_food_bar = ttk.Progressbar(self.status_frame, length=char.char_days_no_food()*15, mode='determinate')
            char_no_food_bar.maximum = char.char_days_no_food()
            char_no_food_bar.value = char.days_without_food
            char_no_food_bar.grid(row=i+1, column=1, padx=5, pady=5, sticky='W')

            char_ration_lbl = ttk.Label(self.status_frame, text=char.ration)
            char_ration_lbl.grid(row=i+1, column=2, padx=5, pady=5)

            char_exh_lvl_lbl = ttk.Label(self.status_frame, text=char.exhaustion_level)
            char_exh_lvl_lbl.grid(row=i+1, column=3, padx=5, pady=5)

    def fill_party_frame(self):
        self.clear_frame(self.party_frame)

        name_col_lbl = ttk.Label(self.party_frame, text='Name', font='TkHeadingFont')
        name_col_lbl.grid(row=0, column=0, padx=5, pady=5, sticky='W')

        name_con_mod_lbl = ttk.Label(self.party_frame, text='CON Mod', font='TkHeadingFont')
        name_con_mod_lbl.grid(row=0, column=1, padx=5, pady=5, sticky='W')

        name_ration_lbl = ttk.Label(self.party_frame, text='Ration', font='TkHeadingFont')
        name_ration_lbl.grid(row=0, column=2, padx=5, pady=5, sticky='W')

        for i, char in enumerate(self.party):
            char_name_lbl = ttk.Label(self.party_frame, text=char.name)
            char_name_lbl.grid(row=i+1, column=0, padx=5, pady=5, sticky='W')

            ration = tkinter.StringVar()
            char_ration_sbx = ttk.Spinbox(self.party_frame, values=['Full', 'Half', 'None'], textvariable=ration, command=lambda: self.update_ration(i, ration))
            char_ration_sbx.grid(row=i+1, column=2, padx=5, pady=5, sticky='W')

    def update_ration(self, idx, ration):
        pass

if __name__ == '__main__':
    app = PartyTime()
    app.start()