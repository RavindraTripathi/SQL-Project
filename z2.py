import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset from the provided URL

restaurant_data = pd.read_csv("zomato.csv")

# Data Preprocessing (if needed)

# Define the formula to check if a restaurant allows table booking
def allows_table_booking(booking_status):
    return "Allows Booking" if booking_status == "Yes" else "Doesn't Allow Booking"

# Apply the formula to create a new column indicating table booking status
restaurant_data['booking_status'] = restaurant_data['book_table'].apply(allows_table_booking)

# Count the number of restaurants allowing and not allowing table booking
booking_counts = restaurant_data['booking_status'].value_counts()

# Plotting the chart
booking_counts.plot(kind='bar', color=['blue', 'orange'])
plt.title('Restaurant Table Booking Availability')
plt.xlabel('Table Booking Status')
plt.ylabel('Number of Restaurants')
plt.xticks(rotation=0)
plt.show()
