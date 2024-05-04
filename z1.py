import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset

restaurant_data = pd.read_csv("Zomato.csv")

# Filter restaurants offering online ordering
online_delivery_restaurants = restaurant_data[restaurant_data['online_order'] == 'Yes']

# Count the number of restaurants delivering online or not
delivery_counts = online_delivery_restaurants['address'].groupby(online_delivery_restaurants['online_order']).count()

# Plot the chart
plt.figure(figsize=(8, 6))
delivery_counts.plot(kind='bar', color=['blue', 'green'])
plt.title('Restaurant Delivery Options')
plt.xlabel('Online Delivery')
plt.ylabel('Number of Restaurants')
plt.xticks(rotation=0)
plt.show()
