signal=input("Enter color:")
match signal:
    case "Red":
        print("Stop! The light is Red.")
    case "Yellow":
        print("Get Ready! The light is Yellow.")
    case "Green":
        print("Go! The light is Green.")
    case _ :
        print("Invalid signal color!")
        