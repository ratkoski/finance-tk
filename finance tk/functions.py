import json
from datetime import datetime
from colors import *
import tkinter as tk

class Functions:
    @staticmethod
    def display_transactions(json_file_path, transactions_frame):
        try:
            with open(json_file_path, "r") as f:
                data = json.load(f)
        except FileNotFoundError:
            data = []

        for widget in transactions_frame.winfo_children():
            widget.destroy()

        '''Iterateing over data and display each transaction'''
        for i, finance_info in enumerate(data, start=1):
            amount = finance_info["amount"]
            expense = finance_info["expense"]
            transaction_time = finance_info.get("time")

            format_time = datetime.strptime(transaction_time, "%Y-%m-%d %H:%M").strftime("%Y-%m-%d %H:%M")

            transaction_label = tk.Label(
                transactions_frame,
                text=f"{i}.${amount}, Type: {expense}, {format_time}",
                bg=BACKGROUND_COLOR,
                fg=NUMBERS_COLOR,
                font=LETTERS_FONT_TRAN,
                anchor="w"
            )
            transaction_label.pack(fill=tk.X, padx=2, pady=2)


    @staticmethod
    def update_balance_label(json_file_path, balance_var, income_var, expenses_var):
        try:
            with open(json_file_path, "r") as f:
                data = json.load(f)
        except FileNotFoundError:
            data = []

        total_income = 0
        total_expenses = 0
        '''Calculate total income and expenses from the data'''
        for finance_info in data:
            if finance_info["action"] == "Income":
                total_income += float(finance_info["amount"])
            elif finance_info["action"] == "Spent":
                total_expenses += float(finance_info["amount"])

        balance = total_income - total_expenses
        balance_var.set(f"${balance:.2f}")
        income_var.set(f"+${total_income:.2f}")
        expenses_var.set(f"-${total_expenses:.2f}")
