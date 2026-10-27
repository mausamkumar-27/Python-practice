status_code=int(input("Enter HTTP Status code: "))
match status_code:
    case 200:
        print("OK:Request was successful.")
    case 201:
        print("Created:New resources created successfully.")
    case 400|401|404:
        print("Client Error:Check your request!")
    case 500|502:
        print("Server Error:Something went wrong on the server.")    
    case _:
        print("Unknown status code!")