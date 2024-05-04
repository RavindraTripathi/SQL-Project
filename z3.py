import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
restaurant_data = pd.read_csv('zomato.csv')

# Convert 'rating' column to numeric
restaurant_data['rating'] = pd.to_numeric(restaurant_data['rating'], errors='coerce')

# Filter restaurants with table booking and calculate average rating
table_booking_ratings = restaurant_data[restaurant_data['book_table'] == 'Yes']['rating'].mean()

# Filter restaurants with valid ratings and calculate overall average rating
overall_rating = restaurant_data['rating'].mean()

# Plotting
plt.figure(figsize=(8, 6))

# Scatter plot
plt.bar(overall_rating, table_booking_ratings, color='blue', label='Table Booking Rate vs Overall Rate')

# Plotting the mean lines
plt.axvline(x=overall_rating, color='red', linestyle='--', label='Overall Rating Mean')
plt.axhline(y=table_booking_ratings, color='green', linestyle='--', label='Table Booking Rating Mean')

# Labels and title
plt.xlabel('Overall Rating')
plt.ylabel('Table Booking Rating')
plt.title('Table Booking Rate vs Overall Rate')
plt.legend()

plt.show()
