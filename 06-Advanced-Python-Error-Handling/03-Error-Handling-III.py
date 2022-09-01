while True:
    try:
        age = int(input("Enter your age: "))
        10 / age

    except ValueError:
        print("Please enter a number")
        continue
    except ZeroDivisionError:
        print("Please enter a number higher than 0")
        break
    else:
        print("Thank You!")
        # break
    finally:
        print("Ok! I am finally done")
    print("Can you hear me?")
