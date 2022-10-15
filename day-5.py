# STOCK TRANSACTION PROGRAM
shares_purchased = 2000
shares_amount = shares_purchased * 40.00
stockbroker_buy_commission = 3/100 * shares_amount
shares_price = shares_purchased * 42.75
stockbroker_sell_commission = 3/100 * shares_price
print(f"The amount of money Joe paid for the stock is {shares_amount}")
print(f"The amount of commission Joe paid his broker when he bought the stock is {stockbroker_buy_commission}")
print(f"The amount for which Joe sold the stock is {shares_price}")
print(f"The amount of commission Joe paid his broker when he sold the stock is {stockbroker_sell_commission}")
print(f"The amount of money that Joe had left when he sold the stock and paid his broker (both times) is {shares_price - stockbroker_buy_commission - stockbroker_sell_commission}")

# INGREDIENT ADJUSTER
cookies = int(input("How many cookies do you want: "))

sugar = (1.5 * cookies) / 48
butter = (1 * cookies) / 48
flour = (2.75 * cookies) / 48

print(f"The number of cups of each ingredient needed for {cookies} cookies are: \nSugar: {round(sugar, 2)} \nButter: {round(butter, 2)} \nFlour: {round(flour, 2)}")