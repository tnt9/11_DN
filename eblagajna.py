def price(item):
    price1 = items[item]
    print "Price of selected item is %.2f EUR" % price1
    return price1

items = {"mleko": 1.90, "kruh": 1.00, "sladoled": 3.20, "kis": 1.50, "olje": 8.75,
         "sok": 2.00, "sladkor": 0.99, "sir": 1.65}

def main():
    item = raw_input("Please, select item in the store: ")
    if item in items:
        price(item)
    else:
        print "Item is not in the store"

if __name__ == "__main__":
    main()