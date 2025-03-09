import time
import sys
import os

# Function to clear the console (works on Windows and Unix-based systems)
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# Function to get valid numeric input from the user
def get_monthly_income():
    while True:
        try:
            income = input("Enter your monthly take-home pay (e.g., 20000): $")
            income = float(income.replace(',', ''))  # Handle commas, e.g., "20,000"
            if income <= 0:
                print("Please enter a positive amount.")
                continue
            return income
        except ValueError:
            print("Invalid input. Please enter a number (e.g., 20000 or 20,000).")

# Function to format elapsed time into a human-readable string
def format_elapsed_time(seconds):
    hours, remainder = divmod(seconds, 3600)
    minutes, seconds = divmod(remainder, 60)
    return f"{int(hours)} hour{'s' if hours != 1 else ''}, {int(minutes)} minute{'s' if minutes != 1 else ''}, {int(seconds)} second{'s' if seconds != 1 else ''}"

# Get user's monthly income
print("Welcome to your Earnings Counter!")
monthly_income = get_monthly_income()

# Calculate the number of seconds in an average month
days_per_month = 365 / 12
seconds_per_month = days_per_month * 24 * 60 * 60

# Calculate precise per-second earning rate
per_second = monthly_income / seconds_per_month

# Initialize total earnings and start time
total_dollars = 0.0
start_time = None

# Display setup info
print(f"\nYour monthly take-home pay: ${monthly_income:,.2f}")
print(f"Earnings rate: ${per_second:.7f} per second")
input("Press Enter to start counting...\n")  # Clear instruction to press Enter

# Record the start time
start_time = time.time()

# Main counter loop
try:
    while True:
        # Calculate elapsed time
        elapsed_time = time.time() - start_time
        # Add earnings per second to the total
        total_dollars += per_second
        # Clear the screen for a fresh display
        clear_screen()
        # Display the dashboard
        print("Earnings Dashboard")
        print("==================")
        print(f"  Total earnings:   ${total_dollars:,.5f}")
        print(f"  Per second rate:  ${per_second:.7f}")
        print(f"  Time elapsed:     {format_elapsed_time(elapsed_time)}")
        print("\nPress Ctrl+C to stop the counter.")
        # Wait 1 second before the next update
        time.sleep(1)
except KeyboardInterrupt:
    # Handle manual stop with Ctrl+C
    print(f"\n\nCounter stopped!")
    print(f"Final earnings: ${total_dollars:,.2f}")
    print("Thanks for using the Earnings Counter!")
    sys.exit(0)