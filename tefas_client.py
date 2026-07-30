from datetime import datetime

from tefas import Crawler

from config import FUNDS


class TefasClient:

    def __init__(self):
        self.crawler = Crawler()

    def get_funds(self):

        today = datetime.today().strftime("%Y-%m-%d")

        funds = []

        for code in FUNDS:

            try:

                df = self.crawler.fetch(
                    start=today,
                    end=today,
                    name=code,
                    columns=[
                        "code",
                        "date",
                        "price"
                    ]
                )

                if len(df) == 0:
                    continue

                row = df.iloc[-1]

                funds.append(
                    {
                        "fund": row["code"],
                        "price": row["price"],
                        "fund_size": None,
                        "investor_count": None,
                        "daily_return": None
                    }
                )

  except Exception as e:
    import traceback
    traceback.print_exc()
