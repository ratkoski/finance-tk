import tkinter as tk
import os
import json
from tkinter import StringVar
from datetime import datetime
import customtkinter as ck
from colors import *
from data import Data
from functions import Functions

ck.set_appearance_mode("dark")
ck.set_default_color_theme("dark-blue")


class App(ck.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("370x620")
        self.title("Finance Tracker")

        PATH = os.path.dirname(os.path.realpath(__file__))
        self.json_file_path = os.path.join(PATH, "finances.json")
        self.IncomeValueLabel = None
        self.ExpensesValueLabel = None
        self.total_income = 0
        self.total_expenses = 0
        '''Creating a StringVar objects to store data'''
        self.balance_var = StringVar()
        self.income_var = tk.StringVar()
        self.expenses_var = tk.StringVar()

        self.insertbutton = ck.CTkButton(
            self,
            text="+",
            text_color="#ffffff",
            fg_color=BACKGROUND_COLOR,
            corner_radius=30,
            font=("Ubuntu", 25, "bold"),
            width=40,
            height=40,
            hover=False,
        )
        self.insertbutton.place(anchor="n", relx=0.5, rely=0.9)
        self.insertbutton.configure(command=self.add_finances_to_json)


        '''Space above the button'''
        self.space = ck.CTkFrame(self, fg_color="#fa0000", height=1)
        self.space.pack(side=tk.BOTTOM, fill=tk.X, expand=False, padx=40)

        '''Border spaces'''
        self.space = ck.CTkFrame(self, fg_color=BACKGROUND_COLOR, width=25, corner_radius=0)
        self.space.pack(side=tk.LEFT, fill=tk.Y, expand=False)

        self.space = ck.CTkFrame(self, fg_color=BACKGROUND_COLOR, width=25, corner_radius=0)
        self.space.pack(side=tk.RIGHT, fill=tk.Y, expand=False)

        self.space = ck.CTkFrame(
            self, fg_color=BACKGROUND_COLOR, height=15, corner_radius=0)
        self.space.pack(side=tk.TOP, fill=tk.Y, expand=False)

        '''Title at the top'''
        self.FrameName = ck.CTkFrame(self, fg_color="")
        self.FrameName.pack(side=tk.TOP, fill=tk.X, expand=False)

        self.LabelName = tk.Label(
            self.FrameName,
            text="Your Finances" + " 💸",
            bg=BACKGROUND_COLOR,
            fg="#ffffff",
            justify=tk.LEFT,
            font=("Ubuntu", 25, "bold"),
        )
        self.LabelName.pack(side=tk.LEFT, fill=tk.BOTH, expand=False)

        self.space = ck.CTkFrame(self, fg_color=BACKGROUND_COLOR, height=15, corner_radius=0)
        self.space.pack(side=tk.TOP, fill=tk.X)

        '''Main frame'''
        self.TopFrame = ck.CTkFrame(self, fg_color=MAIN_COLOR, corner_radius=10)
        self.TopFrame.pack(side=tk.TOP, fill=tk.BOTH, expand=False)

        self.space = ck.CTkFrame(self.TopFrame, fg_color=MAIN_COLOR, height=10)
        self.space.pack(side=ck.TOP, fill=tk.X, pady=3, padx=3)

        '''Main frame titles and subtitles, structure'''
        self.TitleFrame = ck.CTkFrame(self.TopFrame, width=40, height=40, fg_color=MAIN_COLOR)
        self.TitleFrame.pack(side=tk.TOP, fill=tk.X, padx=10)

        self.Title = tk.Label(
            self.TitleFrame,
            text="BALANCE",
            font=("Ubuntu", 14, "bold"),
            bg=MAIN_COLOR,
            fg=LETTERS_COLOR,
        )
        self.Title.pack(side=tk.LEFT, padx=5)

        self.BalanceFrame = ck.CTkFrame(
            self.TopFrame, width=30, height=30, fg_color=MAIN_COLOR)
        self.BalanceFrame.pack(side=tk.TOP, fill=tk.X, padx=8)

        self.Balance = tk.Label(
            self.BalanceFrame,
            textvariable=self.balance_var,
            bg=MAIN_COLOR,
            fg=NUMBERS_COLOR,
            font=("Oswald", 15, "bold"),
        )
        self.update_balance_label()
        self.insertbutton.configure(command=self.add_finances_to_json)

        self.Balance.pack(side=tk.LEFT, padx=14)

        self.space = ck.CTkFrame(self.TopFrame, fg_color=MAIN_COLOR, height=5)
        self.space.pack(side=ck.TOP, fill=tk.X)

        self.space = ck.CTkFrame(self.TopFrame, fg_color=MAIN_COLOR, height=20)
        self.space.pack(side=tk.BOTTOM, fill=tk.X, expand=False)

        self.ExpandFrame = ck.CTkFrame(
            self.TopFrame,
            width=0,
            height=40,
            fg_color=MAIN_COLOR,
        )
        self.ExpandFrame.pack(side=tk.LEFT, fill=tk.X, expand=False, padx=10)

        '''Setting up income label'''
        self.IncomeLabel = tk.Label(
            self.ExpandFrame,
            text="INCOME",
            bg=MAIN_COLOR,
            justify="left",
            font=LETTERS_FONT,
            fg=LETTERS_COLOR,
        )
        self.IncomeLabel.pack(side=tk.TOP, fill=tk.X, expand=False, anchor="w", padx=6)

        self.IncomeValueLabel = tk.Label(
            self.ExpandFrame,
            textvariable=self.income_var,
            bg=MAIN_COLOR,
            fg=NUMBERS_COLOR,
            font=NUMBERS_FONT,
            justify="left",
        )
        self.IncomeValueLabel.pack(
            side=tk.TOP, fill=tk.X, expand=True, anchor="w", padx=10
        )
        self.update_balance_label()

        '''Splitting top frame in half'''
        self.ExpandFrameOut = ck.CTkFrame(self.TopFrame, width=0, height=60, fg_color=MAIN_COLOR)
        self.ExpandFrameOut.pack(side=tk.LEFT, fill=tk.X, expand=False, padx=10)

        '''Setting up expenses label'''
        self.ExpensesLabel = tk.Label(
            self.ExpandFrameOut,
            text="EXPENSES",
            bg=MAIN_COLOR,
            fg=LETTERS_COLOR,
            justify="left",
            font=LETTERS_FONT,
        )
        self.ExpensesLabel.pack(
            side=tk.TOP, fill=tk.X, expand=False, anchor="w", padx=40)

        self.ExpensesValueLabel = tk.Label(
            self.ExpandFrameOut,
            textvariable=self.expenses_var,
            bg=MAIN_COLOR,
            fg=NUMBERS_COLOR,
            font=NUMBERS_FONT,
            justify="left",
        )
        self.ExpensesValueLabel.pack(
            side=tk.TOP, fill=tk.X, expand=True, anchor="w", padx=20)
        self.update_balance_label()

        self.space = ck.CTkFrame(self, fg_color=BACKGROUND_COLOR, height=20)
        self.space.pack(side=tk.TOP, fill=tk.X, expand=False)

        '''Creating tabs for financies and adding transactions'''
        self.Tabs = ck.CTkTabview(
            self,
            fg_color=BACKGROUND_COLOR,
            segmented_button_fg_color=BACKGROUND_COLOR,
            segmented_button_selected_color=LETTERS_COLOR,
        )
        self.Tabs.pack(pady=10, padx=10)
        '''Setting the add financies tab'''
        self.AddFinTab = self.Tabs.add("Add Finances")

        self.add_finances_frame = ck.CTkFrame(self.AddFinTab, fg_color=BACKGROUND_COLOR)
        self.add_finances_frame.pack(fill=tk.BOTH)

        '''Label and entry for description'''
        self.description_label = tk.Label(
            self.add_finances_frame,
            text="Description:",
            font=LETTERS_FONT_TABS,
            bg=BACKGROUND_COLOR,
            fg=NUMBERS_COLOR,
        )
        self.description_label.pack()
        self.description_entry = ck.CTkEntry(self.add_finances_frame)
        self.description_entry.pack()

        '''Label and entry for amount'''
        self.amount_label = tk.Label(
            self.add_finances_frame,
            text="Amount:",
            font=LETTERS_FONT_TABS,
            bg=BACKGROUND_COLOR,
            fg=NUMBERS_COLOR,
        )
        self.amount_label.pack()
        self.amount_entry = ck.CTkEntry(self.add_finances_frame)
        self.amount_entry.pack()

        '''ComboBox for type of action'''
        self.action_label = tk.Label(
            self.add_finances_frame,
            text="Type of Action:",
            font=LETTERS_FONT_TABS,
            bg=BACKGROUND_COLOR,
            fg=NUMBERS_COLOR,
        )
        self.action_label.pack()
        self.action_combobox = ck.CTkComboBox(
            self.add_finances_frame, values=["Spent", "Income"]
        )
        self.action_combobox.pack()
        self.action_combobox.set("Select type..")

        '''ComboBox for type of expense'''
        self.expense_label = tk.Label(
            self.add_finances_frame,
            text="Type of Expense:",
            font=LETTERS_FONT_TABS,
            bg=BACKGROUND_COLOR,
            fg=NUMBERS_COLOR,
        )
        self.expense_label.pack()
        self.expense_combobox = ck.CTkComboBox(
            self.add_finances_frame,
            values=[
                "Food and Drink",
                "Entertainment",
                "Utilities",
                "Finances",
                "Income",
            ],
        )
        self.expense_combobox.pack()
        self.expense_combobox.set("Select expense..")

        '''Setting the add transactions tab'''
        self.AddTransactionsTab = self.Tabs.add("Transactions")

        self.transactions_frame = ck.CTkScrollableFrame(self.AddTransactionsTab)
        self.transactions_frame.pack(fill=tk.BOTH, expand=True)


    def display_transactions(self):
        Functions.display_transactions(self.json_file_path, self.transactions_frame)


    def add_finances_to_json(self):
        description = self.description_entry.get()
        amount = self.amount_entry.get()
        action = self.action_combobox.get()
        expense = self.expense_combobox.get()
        Data.add_finances_to_json(description, amount, action, expense)

        self.display_transactions()
        self.update_balance_label()
        self.Balance.configure(textvariable=self.balance_var)

        self.description_entry.delete(0, tk.END)
        self.amount_entry.delete(0, tk.END)

    def update_balance_label(self):
        Functions.update_balance_label(self.json_file_path, self.balance_var, self.income_var, self.expenses_var)

    def exit(self):
        self.destroy()

    def start(self):
        self.mainloop()


if __name__ == "__main__":
    app = App()
    app.display_transactions()
    app.start()
