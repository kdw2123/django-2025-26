price = [120,45,300,85,150]
def get_expensive_price(price):
  expensive = []

  for i in price:
    if i >= 100:
      
      expensive.append(i)
      
  return expensive 
print(get_expensive_price(price))

    
      
