#list of dictionaries
data_list = [
            {"test_name":"login_test", "status":"pass"},
            {"test_name":"signup_test", "status":"pass"},
            {"test_name":"checkout_test", "status":"fail"},
            {"test_name":"Logout_test", "status":"in_progress"}
]

#loop and print test name and their status
for key in data_list:
    print(f"Test_name is: {key['test_name']}, Status is: {key['status']}")