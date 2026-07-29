from datetime import datetime


class Report:

    def __init__(self):
        pass

    def create(self, fund_data):

        lines = []

        lines.append("=" * 50)
        lines.append("TEFAS GÜNLÜK RAPOR")
        lines.append(datetime.now().strftime("%d.%m.%Y %H:%M"))
        lines.append("=" * 50)
        lines.append("")

        if not fund_data:
            lines.append("Bugün veri bulunamadı.")
            return "\n".join(lines)

        for fund in fund_data:

            lines.append(f"Fon: {fund.get('fund', '-')}")
            lines.append(f"Fiyat: {fund.get('price', '-')}")
            lines.append(f"Fon Büyüklüğü: {fund.get('fund_size', '-')}")
            lines.append(f"Yatırımcı Sayısı: {fund.get('investor_count', '-')}")
            lines.append(f"Günlük Getiri: {fund.get('daily_return', '-')}")
            lines.append("-" * 50)

        return "\n".join(lines)

    def save(self, report_text):

        filename = datetime.now().strftime(
            "data/reports/report_%Y%m%d.txt"
        )

        import os

        os.makedirs("data/reports", exist_ok=True)

        with open(filename, "w", encoding="utf-8") as file:
            file.write(report_text)

        return filename
