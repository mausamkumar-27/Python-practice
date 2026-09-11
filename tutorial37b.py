file=None
try:
    file=open("sample-data.txt","r")
    content=file.read()
    data=int(content)
except FileNotFoundError:
    print("File not found on disk.")
except ValueError:
    print("content could not be parsed to integer.")
finally:
    if file:
        file.close()
        print("File stream safely closed.")