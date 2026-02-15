# store environment in tuple and try modifying them
env = ("dev","qc","prod")
env[1] = "newdev"

# create list with duplicates browsers and convert list to set
list_of_browsers = ["chrome","ff","safari","edge","ff","opera","tor","safari"]
distinct_browsers = set(list_of_browsers)
print(distinct_browsers)

# accessing the element via index after converting the set into list
list_browsers = list(distinct_browsers)
print(list_browsers[0])