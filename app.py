from tefas import TefasClient
from config import FUNDS


def main():
    client = TefasClient()

    print("=" * 50)
    print("TEFAS Fon Takip Sistemi")
    print("=" * 50)

    result = client.check_connection()

    if result["success"]:
        print("✅ TEFAS bağlantısı başarılı.")
        print(f"Takip edilen fonlar: {', '.join(FUNDS)}")
    else:
        print("❌ TEFAS bağlantısı başarısız.")
        print(result)


if __name__ == "__main__":
    main()
