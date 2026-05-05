# ----------------------------------------
# Pandas DataFrame Creation and Filtering
# ----------------------------------------

import pandas as pd

# Creating data
data = {
    "Name": ["Mary", "Jon", "Lucy", "Jon", "Sue", "Mary", "Lucy"],
    "Position": ["Manager", "Programmer", "Manager", "Programmer", "Programmer", "Manager", "Manager"],
    "City": ["Boston", "Chicago", "Los Angeles", "Chicago", "Boston", "Boston", "Chicago"],
    "Gender": ["F", "M", "F", "M", "F", "F", "F"],
    "Age": [35, 37, 40, 29, 31, 26, 28],
    "Salary": [45000, 54000, 35000, 54000, 42000, 45000, 35000]
}

# Create DataFrame
df = pd.DataFrame(data)

# Set index from 1 to 7
df.index = range(1, 8)

print("Original DataFrame:\n")
print(df)


# ----------------------------------------
# Filter using loc
# Condition:
# City = Boston AND Salary >= 45000
# ----------------------------------------

filtered_df = df.loc[(df["City"] == "Boston") & (df["Salary"] >= 45000)]

print("\nEmployees from Boston with Salary >= 45000:\n")
print(filtered_df)


# ----------------------------------------
# End of Program
# ----------------------------------------