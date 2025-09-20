# %% [markdown]
# Data Preprocessing

# %% [markdown]
# Import the Libraries

# %%
import pandas as pd

# %% [markdown]
# Load the data

# %%
df = pd.read_csv("tourism.csv")

# %% [markdown]
# Display the first few rows and information about the dataframe

# %%
print(df.head().to_markdown())
print(df.info())

# %% [markdown]
# Check for duplicate rows

# %%
initial_rows = len(df)
df.drop_duplicates(inplace=True)
final_rows = len(df)
print(f"Number of rows before removing duplicates: {initial_rows}")
print(f"Number of rows after removing duplicates: {final_rows}")
print(f"Number of duplicates rows found and removed: {initial_rows - final_rows}")

# %% [markdown]
# Convert String Columns to Lists of Integers

# %%
# Define a function to convert the string to a list of integers
def convert_to_int_list(route_str):
    try:
        return [int(item) for item in route_str.split('->')]
    except (AttributeError, ValueError):
        return None

# Apply the function to the "Sesquence" and "Optimal_Route_Preference" columns
df["Sequence"] = df["Sequence"].apply(convert_to_int_list)
df["Optimal_Route_Preference"] = df["Optimal_Route_Preference"].apply(convert_to_int_list)

# Display the data types and a few rows to show the change
print("Data Types after conversion")
print(df.info())

print("\nFirst 5 rows of the converted columns:")
print(df[['Sequence', 'Optimal_Route_Preference']].head())

# %% [markdown]
# Check for inconsistent Entries in Categorical Columns

# %%
# Check unique values in key categorical columns
print("Unique values in 'Weather' column:")
print(df['Weather'].unique())

print("\nUnique values in 'Traffic_Level' column:")
print(df['Traffic_Level'].unique())

print("\nUnique values in 'Gender' column:")
print(df['Gender'].unique())

print("\nUnique values in 'Nationality' column:")
print(df['Nationality'].unique())

print("\nUnique values in 'Preferred_Theme' column:")
print(df['Preferred_Theme'].unique())

print("\nUnique values in 'Preferred_Transport' column:")
print(df['Preferred_Transport'].unique())

# %% [markdown]
# Rename the columns for Clarity and Consistency

# %%
df.rename(columns={
    "Route_ID":"route_id",
    "User_ID":"user_id",
    "Sequence":"sequence",
    "Total_Duration":"total_duration",
    "Total_Cost":"total_cost",
    "Weather":"weather",
    "Traffic_Level":"traffic_level",
    "Crowd_Density":"crowd_density",
    "Event_Impact":"event_impact",
    "Optimal_Route_Preference":"optimal_route_preference",
    "Satisfaction_Score":"satisfaction_score",
    "Age":"age",
    "Gender":"gender",
    "Nationality":"nationality",
    "Travel_Companions":"travel_companions",
    "Budget_Category":"budget_category",
    "Preferred_Theme":"preferred_theme",
    "Preferred_Transport":"preferred_transport",
},inplace=True)

# %%
print(df.to_markdown())

# %% [markdown]
# Save the cleaned data

# %%
df.to_csv("tourism_cleaned.csv",index=False)
print("Saved Successfully")


