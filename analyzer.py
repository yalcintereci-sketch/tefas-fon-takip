from datetime import datetime


class FundAnalyzer:

    def analyze(self, fund_name, old_size, new_size):
        diff = new_size - old_size

        if diff > 0:
            direction = "Giriş"
        elif diff < 0:
            direction = "Çıkış"
        else:
            direction = "Değişmedi"

        return {
            "fon": fund_name,
            "eski": old_size,
            "yeni": new_size,
            "fark": diff,
            "durum": direction,
            "tarih": datetime.now().strftime("%d.%m.%Y")
        }


if __name__ == "__main__":
    analyzer = FundAnalyzer()

    result = analyzer.analyze(
        "PHE",
        72000000000,
        73150000000
    )

    print(result)
