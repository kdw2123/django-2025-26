try :
    with open ("data.txt","r")as file:
        content = file.read()
        print (content)
except:
    with open ("data.txt ","w" )as file:
        content= file.write("hi ther ")
        print (content)