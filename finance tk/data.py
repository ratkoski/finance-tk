import json
from datetime import datetime

class Data:
    @staticmethod
    def add_finances_to_json(description, amount, action, expense):
        print("Adding")
        time = datetime.now().strftime("%Y-%m-%d %H:%M")

        finance_info = {
            "description": description,
            "amount": amount,
            "action": action,
            "expense": expense,
            "time": time
        }
        try:
            with open("finances.json", "r") as f:
                data = json.load(f)
        except FileNotFoundError:
            data = []

        data.append(finance_info)

        with open("finances.json", "w") as f:
            json.dump(data, f, indent=4)

        print("Finances added successfully.")
