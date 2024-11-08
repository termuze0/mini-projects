def length_converter():
    meters = float(input("Enter length in meters: "))
    kilometers = meters / 1000
    print(f"{meters} meters is {kilometers} kilometers.\n")

def weight_converter():
    kilograms = float(input("Enter weight in kilograms: "))
    pounds = kilograms * 2.20462
    print(f"{kilograms} kg is {pounds} pounds.\n")

def temperature_converter():
    celsius = float(input("Enter temperature in Celsius: "))
    fahrenheit = (celsius * 9/5) + 32
    print(f"{celsius}°C is {fahrenheit}°F.\n")

def main():
    while True:
        print("Choose the type of conversion:")
        print("1. Length (Meters to Kilometers)")
        print("2. Weight (Kilograms to Pounds)")
        print("3. Temperature (Celsius to Fahrenheit)")
        print("4. Exit")
        
        choice = input("Enter choice (1/2/3/4): ")

        if choice == '1':
            length_converter()
        elif choice == '2':
            weight_converter()
        elif choice == '3':
            temperature_converter()
        elif choice == '4':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.\n")

if __name__ == "__main__":
    main()
