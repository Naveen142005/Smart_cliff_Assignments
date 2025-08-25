class TemperatureConverter:

    def celsiusToFahrenheit(self, c):
        return (9/5) * c + 32

    def fahrenheitToCelsius(self, f):
        return (5/9) * (f - 32)


def main():
    convert = TemperatureConverter()

    c = int(input("Enter Celsius: "))
    f = int(input("Enter Fahrenheit: "))

    print("Celsius to Fahrenheit:", convert.celsiusToFahrenheit(c))
    print("Fahrenheit to Celsius:", convert.fahrenheitToCelsius(f))


if __name__ == "__main__":
    main()
