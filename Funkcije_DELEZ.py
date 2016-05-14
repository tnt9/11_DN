
def percentage(num1, num2):
    percentages = float(num1 / num2) * 100
    return percentages

cities = {"Ljubljana":
              {"vsi": 1000.0,
               "mladi": 550},
          "Kamnik":
              {"vsi": 86.0,
               "mladi": 50},
          "Kranj":
              {"vsi": 800.0,
               "mladi": 420},
          "Maribor":
              {"vsi": 950.0,
               "mladi": 587},
          "Izola":
              {"vsi": 120.0,
               "mladi": 30},
          "Celje":
              {"vsi": 600.0,
               "mladi": 50},
          "Novo Mesto":
              {"vsi": 635.0,
               "mladi": 120}}

def main():
    part = percentage(30.0, 120)
    print"Percentage of young people is", part

    for city in cities:
        vsi = cities[city]["vsi"]
        mladi = cities[city]["mladi"]
        delez = percentage(mladi,vsi)
        print("Percentage of young people in %s is %f" % (city, delez))

if __name__ == "__main__":
    main()