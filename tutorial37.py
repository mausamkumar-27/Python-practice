def check_execution():
    try:
        print("Executing try block...")
        return 1
    except Exception:
        return 0
    finally:
        print("I will always execute,even after the return statment!")
    print("This standard print statement will never run")
val=check_execution()
print("Function returned: ",val)
