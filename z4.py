import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
restaurant_data = pd.read_csv('zomato.csv')

# Best Location
best_location = restaurant_data['location'].value_counts().idxmax()

# Relation between Location and Rating
location_rating = restaurant_data.groupby('location')['rating'].mean().sort_values(ascending=False)

# Restaurant Type
restaurant_type_counts = restaurant_data['rest_type'].value_counts()

# Gaussian Restaurant Type and Rating
restaurant_type_ratings = restaurant_data.groupby('rest_type')['rating'].agg(['mean', 'std'])

# Types of Services
services_counts = restaurant_data[['online_order', 'book_table']].apply(pd.Series.value_counts)

# Relation between Type and Rating
service_rating = restaurant_data.groupby('online_order')['rating'].mean()

# Cost of Restaurant
cost_stats = restaurant_data['approx_cost(for two people)'].describe()

# Number of Restaurants in a Location
restaurant_count_by_location = restaurant_data['location'].value_counts()

# Plotting
plt.figure(figsize=(12, 8))

# Plot 1: Relation between Location and Rating
plt.subplot(2, 2, 1)
location_rating.plot(kind='bar')
plt.title('Average Rating by Location')
plt.xlabel('Location')
plt.ylabel('Average Rating')

# Plot 2: Restaurant Type
plt.subplot(2, 2, 2)
restaurant_type_counts.plot(kind='bar')
plt.title('Number of Restaurants by Type')
plt.xlabel('Restaurant Type')
plt.ylabel('Count')

# Plot 3: Types of Services
plt.subplot(2, 2, 3)
services_counts.plot(kind='bar', stacked=True)
plt.title('Types of Services')
plt.xlabel('Service Type')
plt.ylabel('Count')

# Plot 4: Number of Restaurants in a Location
plt.subplot(2, 2, 4)
restaurant_count_by_location.plot(kind='bar')
plt.title('Number of Restaurants in Each Location')
plt.xlabel('Location')
plt.ylabel('Number of Restaurants')

plt.tight_layout()
plt.show()
