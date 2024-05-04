import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
restaurant_data = pd.read_csv('zomato.csv')

# Convert 'rating' column to numeric
restaurant_data['rating'] = pd.to_numeric(restaurant_data['rating'], errors='coerce')

# 1. Relation between Location and Rating
location_rating = restaurant_data.groupby('location')['rating'].mean().sort_values()
plt.figure(figsize=(12, 6))
location_rating.plot(kind='bar', color='skyblue')
plt.title('Average Rating by Location')
plt.xlabel('Location')
plt.ylabel('Average Rating')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()

# 2. Restaurant Type
restaurant_type_counts = restaurant_data['rest_type'].value_counts()
plt.figure(figsize=(12, 6))
restaurant_type_counts.plot(kind='bar', color='lightgreen')
plt.title('Number of Restaurants by Type')
plt.xlabel('Restaurant Type')
plt.ylabel('Count')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()

# 3. Gaussian Restaurant Type and Rating
restaurant_type_ratings = restaurant_data.groupby('rest_type')['rating'].agg(['mean', 'std'])
plt.figure(figsize=(12, 6))
sns.barplot(x=restaurant_type_ratings.index, y='mean', data=restaurant_type_ratings, color='orange', ci='sd')
plt.title('Mean Rating by Restaurant Type')
plt.xlabel('Restaurant Type')
plt.ylabel('Mean Rating')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()

# 4. Types of Services
services_counts = restaurant_data[['online_order', 'book_table']].apply(pd.Series.value_counts)
plt.figure(figsize=(8, 6))
services_counts.plot(kind='bar', stacked=True)
plt.title('Types of Services')
plt.xlabel('Service Type')
plt.ylabel('Count')
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()

# 5. Relation between Type and Rating
service_rating = restaurant_data.groupby('online_order')['rating'].mean()
plt.figure(figsize=(8, 6))
service_rating.plot(kind='bar', color='lightblue')
plt.title('Average Rating by Service Type')
plt.xlabel('Service Type')
plt.ylabel('Average Rating')
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()

# 6. Cost of Restaurant
plt.figure(figsize=(8, 6))
sns.histplot(restaurant_data['approx_cost(for two people)'].dropna(), kde=True, color='salmon')
plt.title('Distribution of Restaurant Costs')
plt.xlabel('Approximate Cost for Two People')
plt.ylabel('Frequency')
plt.tight_layout()
plt.show()

# 7. Number of Restaurants in a Location
restaurant_count_by_location = restaurant_data['location'].value_counts()
plt.figure(figsize=(12, 6))
restaurant_count_by_location.plot(kind='bar', color='lightcoral')
plt.title('Number of Restaurants in Each Location')
plt.xlabel('Location')
plt.ylabel('Number of Restaurants')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()
