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

def volume_converter():
    liters = float(input("Enter volume in liters: "))
    gallons = liters * 0.264172
    print(f"{liters} liters is {gallons} gallons.\n")

def time_converter():
    minutes = float(input("Enter time in minutes: "))
    hours = minutes / 60
    print(f"{minutes} minutes is {hours} hours.\n")

def speed_converter():
    kph = float(input("Enter speed in kilometers per hour: "))
    mph = kph * 0.621371
    print(f"{kph} km/h is {mph} mph.\n")

def main():
    while True:
        print("Choose the type of conversion:")
        print("1. Length (Meters to Kilometers)")
        print("2. Weight (Kilograms to Pounds)")
        print("3. Temperature (Celsius to Fahrenheit)")
        print("4. Volume (Liters to Gallons)")
        print("5. Time (Minutes to Hours)")
        print("6. Speed (Kilometers per Hour to Miles per Hour)")
        print("7. Exit")
        
        choice = input("Enter choice (1/2/3/4/5/6/7): ")

        if choice == '1':
            length_converter()
        elif choice == '2':
            weight_converter()
        elif choice == '3':
            temperature_converter()
        elif choice == '4':
            volume_converter()
        elif choice == '5':
            time_converter()
        elif choice == '6':
            speed_converter()
        elif choice == '7':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.\n")

if __name__ == "__main__":
    main()
