city_country1 = {"VIENNA": "AUSTRIA", "BRUSSELS": "BELGIUM", "SOFIA": "BULGARIA",
                 "NICOSIA": "CYPRUS", "PRAGUE": "CZECH ReEPUBLIC", "COPENHAGEN": "DENMARK",
                 "TALLINN": "ESTONIA", "HELSINKI": "FINLAND", "PARIS": "FRANCE",
                 "ATHENS": "GREECE", "ZAGREB": "CROATIA", "DUBLIN": "IRELAND",
                 "ROME": "ITALY", "RIGA": "LATVIA", "VILNIUS": "LITHUANIA",
                 "LUXEMBOURG": "LUXEMBOURG", "BUDAPEST": "HUNGARY",
                 "VALLETTA": "MALTA", "BERLIN": "GERMANY", "AMSTERDAM": "NETHERLANDS",
                 "WARSAW": "POLAND", "LISBON": "PORTUGAL", "BUCHAREST":
                 "ROMANIA", "BRATISLAVA": "SLOVAKIA", "LJUBLJANA": "SLOVENIA",
                 "MADRID": "SPAIN", "STOCKHOLM": "SWEDEN", "LONDON": "UNITED KINGDOM"}

keys = city_country1.keys()


def country_city(country):
    for key in keys:
        if country == city_country1[key]:
            print "This is EU country!"
            city1 = key
            print "The capital city of %s is %s" % (country, city1)
            return city1
    print "This is not an EU country"


def state_capital(cap_city, eu_state):
    for key in keys:
        if eu_state == city_country1[key]:
            print "The capital city is correct."
            return
    print "The capital is not correct"


state = raw_input("Please, select EU country: ")
capital = raw_input("The capital of the selected EU country is: ")
state = state.upper()
capital = capital.upper()
city = country_city(state)
state_capital(capital, state)

