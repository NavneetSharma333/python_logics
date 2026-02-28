
data_list = [
            {"test_name":"login_test", "status":"pass"},
            {"test_name":"signup_test", "status":"pass"},
            {"test_name":"checkout_test", "status":"fail"},
            {"test_name":"Logout_test", "status":"in_progress"},
            {"test_name":"stripe_payment", "status":"this_feature_is_not_developed_yet"}
]

passed_test = 0
failed_test = 0
in_progress = 0

for k in data_list:
    print(f"Test_name is: {k['test_name']}, Status is: {k['status']}")
    test_name = k["test_name"]
    status = k["status"]
    
    # if k['status'] == "pass":
    #     passed_test += 1
    # elif k["status"] == "fail":
    #     failed_test += 1
    # elif k["status"] == "in_progress":
    #     in_progress += 1
    # else:
    #     print("nothing here")

    if status == "pass":
        passed_test += 1
    elif status == "fail":
        failed_test += 1
    elif status == "in_progress":
        in_progress += 1
    else:
        print(f"Unknown_test_status: {status}")

print(f"Summary: {passed_test} passed, {failed_test} failed, {in_progress} in-progress")
    
