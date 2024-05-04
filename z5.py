import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
restaurant_data = pd.read_csv('zomato.csv')

# Count the number of restaurants in each location
location_counts = restaurant_data['location'].value_counts()

# Identify the best location with the highest count
best_location = location_counts.idxmax()

# Plotting
plt.figure(figsize=(12, 6))

# Bar chart
location_counts.plot.bar(color='skyblue')

# Highlight the best location
plt.annotate('Best Location', xy=(location_counts.index.get_loc(best_location), location_counts.max()), xytext=(location_counts.index.get_loc(best_location), location_counts.max() + 20),
             arrowprops=dict(facecolor='black', shrink=0.05))

# Labels and title
plt.xlabel('Location')
plt.ylabel('Number of Restaurants')
plt.title('Number of Restaurants in Each Location')

# Adjust x-axis ticks
plt.xticks(range(len(location_counts)), location_counts.index, rotation=45, ha='right')

plt.tight_layout()
plt.show()
