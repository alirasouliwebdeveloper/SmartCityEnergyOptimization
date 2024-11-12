import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime, timedelta

# Set the seed for reproducibility
np.random.seed(42)

# Generate data for one month (30 days)
date_range = pd.date_range(datetime.now() - timedelta(days=30), periods=30, freq='D')

# Simulating energy consumption and production data for residential, industrial, and commercial
residential_consumption = np.random.normal(500, 50, size=30)  # kWh
industrial_consumption = np.random.normal(1000, 150, size=30)  # kWh
commercial_consumption = np.random.normal(700, 100, size=30)  # kWh

# Simulating renewable energy production (in percentage of total consumption)
renewable_production_percentage = np.random.uniform(30, 60, size=30)  # percentage

# Simulating network losses
network_losses = np.random.normal(5, 1.5, size=30)  # percentage

# Energy pricing (in CHF per kWh)
energy_price = np.random.uniform(0.1, 0.2, size=30)  # CHF

# Simulating demographic behavior (e.g., average household size and work behavior)
average_household_size = np.random.randint(2, 5, size=30)  # number of people

# Creating a DataFrame
data = {
    'Date': date_range,
    'Residential Consumption (kWh)': residential_consumption,
    'Industrial Consumption (kWh)': industrial_consumption,
    'Commercial Consumption (kWh)': commercial_consumption,
    'Renewable Energy Production (%)': renewable_production_percentage,
    'Network Losses (%)': network_losses,
    'Energy Price (CHF/kWh)': energy_price,
    'Average Household Size': average_household_size
}

df = pd.DataFrame(data)

# Calculate total consumption per day (sum of all sectors)
df['Total Consumption (kWh)'] = df[['Residential Consumption (kWh)', 'Industrial Consumption (kWh)', 'Commercial Consumption (kWh)']].sum(axis=1)

# Calculate total renewable energy production (kWh)
df['Renewable Energy Production (kWh)'] = df['Renewable Energy Production (%)'] / 100 * df['Total Consumption (kWh)']

# Plotting
plt.figure(figsize=(14, 10))

# Subplot 1: Energy consumption over the month
plt.subplot(2, 2, 1)
plt.plot(df['Date'], df['Residential Consumption (kWh)'], label='Residential', marker='o')
plt.plot(df['Date'], df['Industrial Consumption (kWh)'], label='Industrial', marker='o')
plt.plot(df['Date'], df['Commercial Consumption (kWh)'], label='Commercial', marker='o')
plt.title('Energy Consumption (kWh) over the Last 30 Days')
plt.xlabel('Date')
plt.ylabel('Consumption (kWh)')
plt.xticks(rotation=45)
plt.legend()

# Subplot 2: Renewable energy production vs total consumption
plt.subplot(2, 2, 2)
plt.plot(df['Date'], df['Renewable Energy Production (kWh)'], label='Renewable Energy', marker='o')
plt.plot(df['Date'], df['Total Consumption (kWh)'], label='Total Consumption', linestyle='--', color='red')
plt.title('Renewable Energy Production vs Total Consumption (kWh)')
plt.xlabel('Date')
plt.ylabel('Energy (kWh)')
plt.xticks(rotation=45)
plt.legend()

# Subplot 3: Energy price over time
plt.subplot(2, 2, 3)
plt.plot(df['Date'], df['Energy Price (CHF/kWh)'], label='Energy Price (CHF/kWh)', marker='o', color='green')
plt.title('Energy Price Over the Last 30 Days')
plt.xlabel('Date')
plt.ylabel('Price (CHF/kWh)')
plt.xticks(rotation=45)
plt.legend()

# Subplot 4: Network losses
plt.subplot(2, 2, 4)
plt.plot(df['Date'], df['Network Losses (%)'], label='Network Losses (%)', marker='o', color='purple')
plt.title('Network Losses (%) Over the Last 30 Days')
plt.xlabel('Date')
plt.ylabel('Losses (%)')
plt.xticks(rotation=45)
plt.legend()

plt.tight_layout()
plt.show()
