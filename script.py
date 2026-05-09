def check_device(status):
    if status == "active":
        return "Device already onboarded"
    elif status == "pending":
        return "Proceed with onboarding"
    else:
        return "Check error"

print(check_device("pending"))
