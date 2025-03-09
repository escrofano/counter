import time
import sys

# Earnings rate: $0.00761 per second (based on $20,000/month)
earnings_per_second = 0.00761

# Initial total earnings
total_dollars = 0.0

# Welcome message
print("Welcome to your Earnings Counter!")
print(f"Earnings rate: ${earnings_per_second:.5f} per second")
print("Press Ctrl+C at any time to stop the counter.\n")

# Main counter loop
try:
    while True:
        # Increment total by earnings per second
        total_dollars += earnings_per_second
        # Display the current total with formatting
        print(f"Current earnings: ${total_dollars:,.5f}", end="\r")
        # Wait 1 second before next update
        time.sleep(1)
except KeyboardInterrupt:
    # Handle manual stop with Ctrl+C
    print(f"\n\nCounter stopped!")
    print(f"Final earnings: ${total_dollars:,.2f}")
    print("Thanks for using the Earnings Counter!")
    sys.exit(0)
