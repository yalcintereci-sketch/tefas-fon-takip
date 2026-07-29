import requests


class TefasClient:

    def __init__(self):
        self.session = requests.Session()
        self.base_url = "https://www.tefas.gov.tr"

    def check_connection(self):
        r = self.session.get(self.base_url, timeout=20)

        return {
            "status": r.status_code,
            "success": r.ok
        }


if __name__ == "__main__":
    client = TefasClient()

    print(client.check_connection())
