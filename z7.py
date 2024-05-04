import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
restaurant_data = pd.read_csv('zomato.csv')

# Restaurant Type
restaurant_type_counts = restaurant_data['rest_type'].value_counts()

# Most famous restaurant chains in Bengaluru
# Group by restaurant name and count the occurrences
restaurant_chains = restaurant_data[restaurant_data['listed_in(city)'] == 'BTM']['name'].value_counts().head(10)

# Plotting
plt.figure(figsize=(12, 6))

# Plot for restaurant types
plt.subplot(1, 2, 1)
restaurant_type_counts.plot(kind='bar', color='lightgreen')
plt.title('Number of Restaurants by Type')
plt.ylabel('Count')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()

# Plot for most famous restaurant chains
plt.subplot(1, 2, 2)
restaurant_chains.plot(kind='bar', color='skyblue')
plt.title('Top 10 Most Famous Restaurant Chains in Bengaluru (BTM Area)')
plt.xlabel('Restaurant Chain')
plt.ylabel('Number of Restaurants')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()

plt.show()
