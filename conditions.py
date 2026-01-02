browser = "chrome"

if browser == "chrome":
    print("Launch Chrome")
elif browser == "firefox":
    print("Mozilla browser")
else:
    print("Unsupported browser")

# Print numbers 1–20
trgt_int = 13

# for i in range(1, 21):
#     if i % 2 != 0:
#         print(i)

#     if i == trgt_int:
#         print(f"the target {trgt_int} is found")
#         break
# else:
#     print(f"target {trgt_int} not found")


i = 0
while i < 20:
    i = i+1
    #print(i)
    
    if i % 2 != 0:
        print(i)
    
    if i == trgt_int:
        print(f"{trgt_int} is found form while loop also")
        break
else:
    print(f"{trgt_int} not found form while loop")
