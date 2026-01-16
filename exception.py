def file_handling(file_name):
    try:
        # with open(file_name, "a") as file:
        #     # content = file.read()
        #     # print(content)
        #     file.write("My age is 22")
        with open(file_name, "r") as file:
            content = file.read()
            print(content)    
        
    except FileNotFoundError:
        print("File does not exist.")

file_handling("hello.txt")