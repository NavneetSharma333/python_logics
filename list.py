# list of browsers
browsers = ["chrome", "firefox", "edge", "Safari", "opera"]
print(browsers)

# Adding 2 more browsers in the above list
browsers_list_2 = ("brave", "tor", "onion")
browsers.extend(browsers_list_2)
print(browsers)

remained_items = browsers.pop()
print(f"removed value is {remained_items},  remained list is  {browsers}")

new_list = []
for i in browsers:
    updated_dataset = i.upper()
    new_list.append(updated_dataset)

print(f"now list with uppercases : {new_list}")