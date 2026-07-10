import requests


API_KEY = "57094190e56d4e2c90794403261007"


def get_weather(city):

    url = "https://api.weatherapi.com/v1/current.json"

    params = {
        "key": API_KEY,
        "q": city,
        "aqi": "yes"
    }

    try:

        response = requests.get(
            url,
            params=params,
            timeout=10
        )

        response.raise_for_status()

        data = response.json()

        if "error" in data:

            print("\n❌ Error:", data["error"]["message"])
            return

        print("\n" + "=" * 40)
        print("🌦️        WEATHER REPORT")
        print("=" * 40)

        print(f"🏙️  City        : {data['location']['name']}")
        print(f"🌍 Country     : {data['location']['country']}")
        print(f"🕒 Local Time  : {data['location']['localtime']}")
        print(f"🌡️ Temperature : {data['current']['temp_c']} °C")
        print(f"🤒 Feels Like  : {data['current']['feelslike_c']} °C")
        print(f"☁️ Condition   : {data['current']['condition']['text']}")
        print(f"💧 Humidity    : {data['current']['humidity']} %")
        print(f"🌬️ Wind Speed  : {data['current']['wind_kph']} km/h")
        print(f"🧭 Wind Dir.   : {data['current']['wind_dir']}")
        print(f"👁️ Visibility  : {data['current']['vis_km']} km")
        print(f"ضغط Pressure   : {data['current']['pressure_mb']} mb")
        print(f"🌞 UV Index    : {data['current']['uv']}")

        print("=" * 40)

    except requests.exceptions.ConnectionError:
        print("\n❌ No Internet Connection.")

    except requests.exceptions.Timeout:
        print("\n❌ Request Timed Out.")

    except requests.exceptions.HTTPError as e:
        print("\n❌ HTTP Error:", e)

    except Exception as e:
        print("\n❌ Unexpected Error:", e)


def main():

    print("=" * 40)
    print("🌦️ Welcome to Python Weather App")
    print("=" * 40)

    while True:

        city = input("\nEnter City Name (or 'exit'): ").strip()

        if city.lower() == "exit":
            print("\n👋 Thank you for using Weather App.")
            break

        if city == "":
            print("⚠️ City name cannot be empty.")
            continue

        get_weather(city)


if __name__ == "__main__":
    main()