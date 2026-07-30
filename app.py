from tefas import TefasClient
from storage import Storage
from analyzer import Analyzer
from report import Report
from logger import Logger


def main():

    logger = Logger()

    logger.info("TEFAS veri çekme başladı.")

    client = TefasClient()

    data = client.get_funds()

    logger.info(f"{len(data)} fon bulundu.")

    storage = Storage()
    storage.save(data)

    history = storage.history()

    analyzer = Analyzer()

    analysis = analyzer.analyze(history)

    report = Report()

    report_text = report.create(analysis)

    report_file = report.save(report_text)

    logger.info(f"Rapor oluşturuldu: {report_file}")

    print(report_text)


if __name__ == "__main__":
    main()
