import os
import pandas as pd
from datetime import datetime


class Storage:

    def __init__(self):
        self.data_folder = "data"
        self.history_file = os.path.join(self.data_folder, "history.csv")

        os.makedirs(self.data_folder, exist_ok=True)

        if not os.path.exists(self.history_file):
            df = pd.DataFrame(columns=[
                "date",
                "fund",
                "price",
                "fund_size",
                "investor_count",
                "daily_return"
            ])
            df.to_csv(self.history_file, index=False)

    def save(self, fund_data):

        df = pd.read_csv(self.history_file)

        today = datetime.now().strftime("%Y-%m-%d")

        for item in fund_data:

            row = {
                "date": today,
                "fund": item.get("fund"),
                "price": item.get("price"),
                "fund_size": item.get("fund_size"),
                "investor_count": item.get("investor_count"),
                "daily_return": item.get("daily_return")
            }

            df.loc[len(df)] = row

        df.to_csv(self.history_file, index=False)

    def history(self):
        return pd.read_csv(self.history_file)
