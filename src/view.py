import tkinter as tk
from tkinter import ttk


class View(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)


        my_game = ttk.Treeview(self)
        my_game['columns'] = ('player_id', 'player_name', 'player_Rank', 'player_states', 'player_city')

        my_game.column("#0", width=0,  stretch=tk.NO)
        my_game.column("player_id",anchor=tk.CENTER, width=80)
        my_game.column("player_name",anchor=tk.CENTER,width=80)
        my_game.column("player_Rank",anchor=tk.CENTER,width=80)
        my_game.column("player_states",anchor=tk.CENTER,width=80)
        my_game.column("player_city",anchor=tk.CENTER,width=80)

        my_game.heading("#0",text="",anchor=tk.CENTER)
        my_game.heading("player_id",text="Id",anchor=tk.CENTER)
        my_game.heading("player_name",text="Name",anchor=tk.CENTER)
        my_game.heading("player_Rank",text="Rank",anchor=tk.CENTER)
        my_game.heading("player_states",text="States",anchor=tk.CENTER)
        my_game.heading("player_city",text="States",anchor=tk.CENTER)
        my_game.pack()

        # set the controller
        self.controller = None

    def set_controller(self, controller):
        """
        Set the controller
        :param controller:
        :return:
        """
        self.controller = controller

    def save_button_clicked(self):
        """
        Handle button click event
        :return:
        """
        if self.controller:
            self.controller.save(self.email_var.get())

    def show_error(self, message):
        """
        Show an error message
        :param message:
        :return:
        """
        self.message_label['text'] = message
        self.message_label['foreground'] = 'red'
        self.message_label.after(3000, self.hide_message)
        self.email_entry['foreground'] = 'red'

    def show_success(self, message):
        """
        Show a success message
        :param message:
        :return:
        """
        self.message_label['text'] = message
        self.message_label['foreground'] = 'green'
        self.message_label.after(3000, self.hide_message)

        # reset the form
        self.email_entry['foreground'] = 'black'
        self.email_var.set('')

    def hide_message(self):
        """
        Hide the message
        :return:
        """
        self.message_label['text'] = ''
