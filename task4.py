def read_sales_file(file_name):
    with open("sales.txt","r")as file:
        lines = file.readlines()
    sales =[]
    for line in lines :
        line =line.strip()
        try:
            number = int(line)
            sales.append(number)
        except ValueError:
            print(f"invlaid sales entry found and skipped : '{line}'")
    return sales 
sales_list = read_sales_file("sales.txt")
total_sales = sum(sales_list)
print("vlaid sales numbe r: ", sales_list)
print("Total sales: ", total_sales)