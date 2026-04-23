def greet(first, last="", gender="", style="friendly"):
    full = f"{gender} {first} {last}".strip()
    gender = gender.casefold()
    if gender == "male":
        re:
    style = style.lower()
    if style == "friendly":
        return f"Hey, {first}! Great to see you. Try to calculate your tip"
    if style == "formal":
        name = f"Mr./Ms. {last}" if last else first
        return f"Good day, {name}. Welcome. Please Calculate your tip"
    if style == "excited":
        return f"WOW, {full.upper()}!! So glad you're here! Ensure to calculate your tip!"
    return f"Hello, {full}!"

def calculate_tip(bill, tip_pct, split=1):
    if bill < 0:
        raise ValueError("Bill amount cannot be negative.")
    if tip_pct < 0:
        raise ValueError("Tip percentage cannot be negative.")
    if split < 1:
        raise ValueError("Split must be at least 1.")
    tip_amount  = bill * tip_pct / 100
    total       = bill + tip_amount
    per_person  = total / split
    return {"tip": tip_amount, "total": total, "per_person": per_person}

def main():
    print("=== Name Greeter & Tip Converter ===")
    while True:
        try:
            first = input("First name       : ").strip()
            last  = input("Last name (opt.) : ").strip()
            print("Styles: friendly | formal | excited")
            style = input("Style            : ").strip() or "friendly"
            print("\n" + greet(first, last, style) + "\n")
            bill    = float(input("Bill total ($)       : "))
            tip_pct = float(input("Tip percentage (%)   : "))
            split   = int(input("Split between (people): "))
            r = calculate_tip(bill, tip_pct, split)
            print(f"\n  Tip amount : {r['tip']:.2f}")
            print(f"  Total bill : ${r['total']:.2f}")
            print(f"  Per person : ${r['per_person']:.2f}\n")
        except ValueError as e:
            print(f"Error: {e}\n")
        again = input("Calculate again? (y/n): ").strip().lower()
        if again != 'y':
            break
    print("Goodbye!")

if __name__ == "__main__":
    main()
    


def to_celsius(value, unit):
    unit = unit.upper()
    if unit == 'C':  return value
    if unit == 'F':  return (value - 32) * 5 / 9
    if unit == 'K':  return value - 273.15
    raise ValueError(f"Unknown unit '{unit}'. Use C, F, or K.")

def from_celsius(celsius):
    return {
        "C": celsius,
        "F": celsius * 9 / 5 + 32,
        "K": celsius + 273.15,
    }

def convert_two_cities():
    print("\n=== Two Cities Temperature Conversion ===")
    city1 = input("Enter first city name: ")
    val1 = float(input(f"{city1} temperature value: "))
    unit1 = input(f"{city1} unit (C/F/K): ").strip().upper()
    
    city2 = input("\nEnter second city name: ")
    val2 = float(input(f"{city2} temperature value: "))
    unit2 = input(f"{city2} unit (C/F/K): ").strip().upper()
    
    c1 = to_celsius(val1, unit1)
    c2 = to_celsius(val2, unit2)
    
    r1 = from_celsius(c1)
    r2 = from_celsius(c2)
    
    print(f"\n--- {city1} ---")
    print(f"C: {r1['C']:.2f} °C | F: {r1['F']:.2f} °F | K: {r1['K']:.2f} K")
    print(f"\n--- {city2} ---")
    print(f"C: {r2['C']:.2f} °C | F: {r2['F']:.2f} °F | K: {r2['K']:.2f} K")
    return c1, c2

def average_temperature(c1, c2):
    avg_c = (c1 + c2) / 2
    result = from_celsius(avg_c)
    
    print("\n=== Average Temperature ===")
    print(f"Celsius    : {result['C']:.2f} °C")
    print(f"Fahrenheit : {result['F']:.2f} °F")
    print(f"Kelvin     : {result['K']:.2f} K\n")

def main():
    print("=== Temperature Converter ===")
    while True:
        choice = input("\nChoose option:\n"
                       "1. Single temperature conversion\n"
                       "2. Two cities + average\n"
                       "Enter choice (1/2): ").strip()
        try:
            if choice == '1':
                value = float(input("Temperature value   : "))
                unit  = input("From unit (C/F/K)   : ").strip().upper()
                c     = to_celsius(value, unit)
                result = from_celsius(c)
                print(f"\n  Celsius    : {result['C']:.2f} °C")
                print(f"  Fahrenheit : {result['F']:.2f} °F")
                print(f"  Kelvin     : {result['K']:.2f} K\n")
                if result['K'] < 0:
                    print("  Warning: temperature is below absolute zero (0 K).\n")

            elif choice == '2':
                c1, c2 = convert_two_cities()
                average_temperature(c1, c2)

            else:
                print("Invalid choice.\n")

        except ValueError as e:
            print(f"Error: {e}\n")   

        again = input("Continue? (y/n): ").strip().lower()
        if again != 'y':
            break

    print("Goodbye!")

if __name__ == "__main__":
    main()