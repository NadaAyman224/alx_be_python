from datetime import datetime, timedelta

# Display the Current Date and Time:
def display_current_datetime():
    current_date = datetime.now()
    print(f"Current date and time: {current_date.strftime("%Y-%m-%d %H:%M:%S")}" )

display_current_datetime()

# Calculate a Future Date:
no_of_days = int(input("Enter the number of days to add to the current date: "))

def calculate_future_date(days):
    current_date = datetime.now()
    future_date = current_date + timedelta(days=days)
    print(f"Future date: {future_date.strftime("%Y-%m-%d")}")

    
calculate_future_date(no_of_days)