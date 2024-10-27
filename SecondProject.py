import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load the data from the CSV file
df = pd.read_csv('historical_events.csv')

# Extract years and convert them to integers
df['Year'] = df['Year'].apply(lambda x: int(x.split()[0]) if x.isdigit() else np.nan)

# Drop rows with NaN values in the Year column
df.dropna(subset=['Year'], inplace=True)

# Create a new column for century
df['Century'] = (df['Year'] // 100) * 100

# Count the number of events per century
century_counts = df['Century'].value_counts().sort_index()

# Plotting
plt.figure(figsize=(12, 6))
plt.bar(century_counts.index, century_counts.values, width=80, color='skyblue')
plt.xlabel('Century')
plt.ylabel('Number of Events')
plt.title('Number of Historical Events per Century')
plt.xticks(century_counts.index, rotation=45)
plt.grid(axis='y')

# Show the plot
plt.tight_layout()
plt.savefig('historical_events_per_century.png')  # Save the figure
plt.show()
