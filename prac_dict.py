# ----------------------------------------
# Dictionary Operations on India Data
# ----------------------------------------

# 1. Create dictionary
india = {
    "Delhi": "New Delhi",
    "Maharashtra": "Mumbai",
    "U.P": "Lucknow",
    "Karnataka": "Bangalore",
    "Rajasthan": "Jaipur",
    "M.P": "Lucknow",
    "Punjab": "Chandigarh"
}

print("Original Dictionary:")
print(india)


# ----------------------------------------
# (a) Display all values
# ----------------------------------------
print("\n(a) All Capitals:")
print(list(india.values()))


# ----------------------------------------
# (b) Update MP capital to Bhopal
# ----------------------------------------
india["M.P"] = "Bhopal"
print("\n(b) After Updating M.P Capital:")
print(india)


# ----------------------------------------
# (c) Insert Bihar - Patna
# ----------------------------------------
india["Bihar"] = "Patna"
print("\n(c) After Adding Bihar:")
print(india)


# ----------------------------------------
# (d) Delete Karnataka - Bangalore
# ----------------------------------------
del india["Karnataka"]
print("\n(d) After Deleting Karnataka:")
print(india)


# ----------------------------------------
# (e) fromkeys() Function Explanation
# ----------------------------------------

print("\n(e) Demonstrating fromkeys()")

country = ["India", "USA", "UK", "Russia", "Japan", "China", "France", "Germany"]
colour = ["red", "blue", "yellow", "black", "green"]

# Example 1: Default single value
dict1 = dict.fromkeys(country, "No Color Assigned")
print("\nDictionary with default value:")
print(dict1)

# Example 2: Assign same list to all keys
dict2 = dict.fromkeys(country, colour)
print("\nDictionary with same list of colors:")
print(dict2)


# ----------------------------------------
# End of Program
# ----------------------------------------