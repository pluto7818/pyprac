# ----------------------------------------
# List Operations on Games
# ----------------------------------------

# 1. Create an empty list
games = []

# Insert elements manually (without using append)
games = games + ["Cricket"]
games = games + ["Hockey"]
games = games + ["Football"]
games = games + ["Tennis"]
games = games + ["Badminton"]
games = games + ["KhoKho"]
games = games + ["Rugby"]

print("Original List:")
print(games)


# ----------------------------------------
# (a) Reverse the list (without built-in)
# ----------------------------------------
reversed_list = []
for i in range(len(games) - 1, -1, -1):
    reversed_list = reversed_list + [games[i]]

print("\n(a) Reversed List:")
print(reversed_list)


# ----------------------------------------
# (b) Sorting in Ascending Order (manual)
# ----------------------------------------
asc_list = games[:]

for i in range(len(asc_list)):
    for j in range(i + 1, len(asc_list)):
        if asc_list[i] > asc_list[j]:
            temp = asc_list[i]
            asc_list[i] = asc_list[j]
            asc_list[j] = temp

print("\n(b) Ascending Order:")
print(asc_list)


# ----------------------------------------
# (c) Sorting in Descending Order (manual)
# ----------------------------------------
desc_list = games[:]

for i in range(len(desc_list)):
    for j in range(i + 1, len(desc_list)):
        if desc_list[i] < desc_list[j]:
            temp = desc_list[i]
            desc_list[i] = desc_list[j]
            desc_list[j] = temp

print("\n(c) Descending Order:")
print(desc_list)


# ----------------------------------------
# (d) Create another list and merge
# ----------------------------------------
country = ["India", "USA", "Japan", "Australia", "Russia", "France", "Romania"]

# Add all elements of games into country (without extend)
for item in games:
    country = country + [item]

print("\n(d) Country List after adding Games:")
print(country)


# ----------------------------------------
# End of Program
# ----------------------------------------