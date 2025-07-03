print("Customer:- what is the price of 1kg apples")
appleprice = input("Shopkeeper:- Price of this 1kg apples is ")
b = int(appleprice)
budget = int(200)
if(budget - b >= 100 ):
 print("okay please pack 1 kg apple")
elif(budget - b >= 50):
 print("okay please pack 500 grams")
elif(budget - b >= 25):
 print("okay please pack 250 grams")
else:
 print("Sorry this is not in my budget")
print("Bye Bye")