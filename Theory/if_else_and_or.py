def age_check(age):
    print (f"you are {age}")
    # formating method.
    if age < 18:
        print("you can't drink.")
    elif age == 18:
        print("you are new do this.")
    else:
        print("enjoy your drink.")

age_check(19)