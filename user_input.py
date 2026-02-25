
supported_browsers_list = ["chrome", "safari", "firefox", "edge"]

browser = input("Enter your browser name: ").strip().lower()

if browser in supported_browsers_list:
    print("This browser is supported, launching shortly")
else:
    print("your browser not supported, unable to launch")
    print("supported browsers are:") #.join(supported_browsers_list))
    
    for list in supported_browsers_list:
        print(">", list)