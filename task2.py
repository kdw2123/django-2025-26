
with open("log.txt", "a")as file:
    file.write("uesr loged in\n")
with open("log.txt", "r")as file:
    content= file.read()
    print(content)