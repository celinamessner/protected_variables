class Employee:
    def __init__(self, name, location, total_leave_days):
        # unprotected variables
        self.name = name

        # protected variable
        self.location = location
        self._leave_balance = total_leave_days

    def display_details(self):
        print(f"Employee Name: {self.name}")
        print(f"location: {self.location}")
        print(f"Leave Days Remaining: {self._leave_balance}")

    def book_leave(self, days_requested):
        if days_requested <= 0:
            print("Error. Please enter a positive number of days.")
            return

        if days_requested <= self._leave_balance:
            self._leave_balance -= days_requested
            print(f"Leave approved for {days_requested} days.")
            print(f"Updated leave balance: {self._leave_balance}")
        else:
            print("Error. Not enough leave available.")

# Example usage
def main():
    # Create an employee instance
    employee1 = Employee("Anna Mayer", "Berlin", 20)

    # Display employee details
    employee1.display_details()

    # Book 5 days of leave
    print("\nRequesting 5 days of leave...")
    employee1.book_leave(5)

    # Attempt to book more leave than available
    print("\nRequesting 18 days of leave...")
    employee1.book_leave(18)

    # Accessing a protected variable directly
    print(f"\nLeave balance: {employee1._leave_balance} day(s)")

if __name__ == "__main__":
    main()
