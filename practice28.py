signal=input("Enter color:")
match signal:
    case "Red":
        print("Stop! The light is Red.",signal)
    case "Yellow":
        print("Get Ready! The light is Yellow.",signal)
    case "Green":
        print("Go! The light is Green.",signal)
    case _ :
        print("Invalid signal color!",signal)
        