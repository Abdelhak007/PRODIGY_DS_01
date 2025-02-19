import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
data = pd.read_excel(r"C:\Users\PC\Downloads\API_SP.POP.TOTL_DS2_en_excel_v2_287.xls", skiprows=3)

# Get the latest year dynamically (last column before metadata)
latest_year = data.columns[-1] 

# Select relevant columns and clean data
df = data[['Country Name', latest_year]].dropna(subset=[latest_year])  # Drop rows where population is NaN
df[latest_year] = pd.to_numeric(df[latest_year], errors='coerce')  # Convert to numeric

# Sort top 10 countries by population
df = df.sort_values(by=latest_year, ascending=False).head(10)

# Plot bar chart for top 10 populated countries
plt.figure(figsize=(12, 6))
sns.barplot(x=df[latest_year], y=df['Country Name'], palette="viridis")

# Labels and title
plt.xlabel("Total Population", fontsize=12)
plt.ylabel("Country", fontsize=12)
plt.title(f"Top 10 Most Populated Countries ({latest_year})", fontsize=14)
plt.xticks(rotation=45)

# Adjust layout and show
plt.tight_layout()
plt.show()

# Plot histogram for population distribution
plt.figure(figsize=(12, 6))
sns.histplot(data=df, x=latest_year, bins=20, kde=True)

# Labels and title
plt.xlabel("Population (Billions)", fontsize=12)
plt.ylabel("Number of Countries", fontsize=12)
plt.title(f"Distribution of Country Populations ({latest_year})", fontsize=14)

# Adjust layout and show
plt.tight_layout()
plt.show()
