class Train:
    def __init__(self, name, fare, seats):
        self.name = name
        self.fare = fare
        self.seats = seats

    def get_status(self):
        """Prints the number of available seats."""
        print(f"Train Name: {self.name}")
        print(f"Available Seats: {self.seats}")

    def get_fare_info(self):
        """Prints the ticket price."""
        print(f"Ticket Fare: ₹{self.fare}")

    def book_ticket(self):
        """Books a ticket if seats are available."""
        if self.seats > 0:
            print(f"Ticket booked successfully! Seat Number: {self.seats}")
            self.seats -= 1
        else:
            print("Booking failed. No seats available!")

# --- Example Usage ---
# Create a train instance with Name, Fare (in ₹), and Total Seats
rajdhani = Train("Rajdhani Express (12301)", 1200, 2)

# Check status and fare
rajdhani.get_status()
rajdhani.get_fare_info()

# Attempt to book tickets
rajdhani.book_ticket()  # Successfully books seat 2
rajdhani.book_ticket()  # Successfully books seat 1
rajdhani.book_ticket()  # Fails because seats are empty
