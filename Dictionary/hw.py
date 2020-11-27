productList = []

while True:
    print('what do you want to get?')
    product = input()
    if product == '':
        break

    print('how many you buy?')
    number = int(input())

    productList.append((product, number))

print(productList)

priceTable = {'apple': 25,
              'milk': 70,
              'cheese': 150,
              'cheese cake': 200,
              'cookies': 60,
              'banana': 10,
              'beef': 99,
              'pencil': 8,
              'pork': 88,
              'chicken': 80}

def cashier(products):
    total = 0
    for p in products:
        price = priceTable.get(p[0], 0)
        number = p[1]
        oneProductTotal = price * number
        total = total + oneProductTotal
    return total


print('You spent {} on these products'.format(cashier(productList)))