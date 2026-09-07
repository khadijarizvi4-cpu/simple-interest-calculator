def calculate_simple_interest(principal, rate, time):
    """
    Calculate simple interest.

    Formula: SI = (P * R * T) / 100

    Parameters:
        principal (float): The initial amount of money (P)
        rate (float): The annual interest rate in percent (R)
        time (float): The time period in years (T)

    Returns:
        tuple: (simple_interest, total_amount)
    """
    simple_interest = (principal * rate * time) / 100
    total_amount = principal + simple_interest
    return simple_interest, total_amount


def main():
    print("=== Simple Interest Calculator ===")
    try:
        principal = float(input("Enter principal amount: "))
        rate = float(input("Enter annual interest rate (%): "))
        time = float(input("Enter time period (years): "))
    except ValueError:
        print("Please enter valid numbers.")
        return

    interest, total = calculate_simple_interest(principal, rate, time)

    print(f"\nSimple Interest: {interest:.2f}")
    print(f"Total Amount (Principal + Interest): {total:.2f}")


if __name__ == "__main__":
    main()
