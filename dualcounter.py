import time
import sys
import os

# Function to clear the console
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# Function to get valid numeric input from the user
def get_monthly_income(prompt):
    while True:
        try:
            income = input(prompt)
            income = float(income.replace(',', ''))  # Handle commas, e.g., "20,000"
            if income <= 0:
                print("Please enter a positive amount.")
                continue
            return income
        except ValueError:
            print("Invalid input. Please enter a number (e.g., 20000 or 20,000).")

# Function to format elapsed time into years, months, weeks, days, hours, minutes, seconds
def format_elapsed_time(seconds):
    time_units = [
        ("year", 365 * 24 * 60 * 60),
        ("month", 30 * 24 * 60 * 60),  # Approximate month length
        ("week", 7 * 24 * 60 * 60),
        ("day", 24 * 60 * 60),
        ("hour", 60 * 60),
        ("minute", 60),
        ("second", 1),
    ]
    parts = []
    for unit, seconds_per_unit in time_units:
        if seconds >= seconds_per_unit:
            count = int(seconds // seconds_per_unit)
            seconds %= seconds_per_unit
            parts.append(f"{count} {unit}{'s' if count != 1 else ''}")
    return ", ".join(parts) if parts else "0 seconds"

# Get two monthly incomes from the user
print("Welcome to your Dual Earnings Counter!")
print("Please enter two separate monthly take-home incomes to compare.\n")
income1 = get_monthly_income("Enter first monthly take-home pay (e.g., 20000): $")
income2 = get_monthly_income("Enter second monthly take-home pay (e.g., 25000): $")

# Calculate the number of seconds in an average month
days_per_month = 365 / 12
seconds_per_month = days_per_month * 24 * 60 * 60

# Calculate precise per-second earning rates for both incomes
per_second1 = income1 / seconds_per_month
per_second2 = income2 / seconds_per_month

# Initialize total earnings for both
total_dollars1 = 0.0
total_dollars2 = 0.0

# Display setup info
print(f"\nFirst income: ${income1:,.2f}/month → ${per_second1:.7f}/second")
print(f"Second income: ${income2:,.2f}/month → ${per_second2:.7f}/second")
input("Press Enter to start counting...\n")  # Wait for user to press Enter

# Record the start time
start_time = time.time()

# Main counter loop
try:
    while True:
        # Calculate elapsed time
        elapsed_time = time.time() - start_time
        # Add earnings per second to both totals
        total_dollars1 += per_second1
        total_dollars2 += per_second2
        # Clear the screen for a fresh display
        clear_screen()
        # Display the dashboard
        print("Earnings Dashboard")
        print("===============")
        print(f"Total earnings: ${total_dollars1:,.2f}")
        print(f"Per second rate: ${per_second1:.7f}")
        print("")
        print(f"Total earnings: ${total_dollars2:,.2f}")
        print(f"Per second rate: ${per_second2:.7f}")
        print("")
        print(f"Time elapsed: {format_elapsed_time(elapsed_time)}")
        print("\nPress Ctrl+C to stop the counter.")
        # Wait 1 second before the next update
        time.sleep(1)
except KeyboardInterrupt:
    # Handle manual stop with Ctrl+C
    print(f"\n\nCounter stopped!")
    print(f"Final earnings (Income 1): ${total_dollars1:,.2f}")
    print(f"Final earnings (Income 2): ${total_dollars2:,.2f}")
    print("Thanks for using the Dual Earnings Counter!")
    sys.exit(0)