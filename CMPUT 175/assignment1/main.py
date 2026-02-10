
def countries_deficit():
    with open('country.txt', 'r') as file:
        countries = file.read().splitlines()
        for country in countries:
            country = country.join(',')
    print(countries)

def table_maker_a(countries):
    titleOne = 'Country'
    titleTwo = 'Trade Deficit (Billions USD)'
    sizeOne = 34
    sizeTwo = 28

    # Formatting
    title = '| ' + titleOne + (' ' * (sizeOne - len(titleOne) - 1)) + ' | ' + titleTwo + (' ' * (sizeTwo - len(titleTwo))) + ' |'
    bar = '-' * len(title)

    # Display
    print(bar)
    print(title)
    print(bar)

    for country in countries:
        print('| ' + country + (' ' * (sizeOne - len(country) - 1)) + ' | $' + (' ' * (sizeTwo - len(str(countries[country])) - 1)) + str(countries[country]) + ' |')
    
    print(bar)

def main():
    # Section A: countries with highest trade deficits
    countries = {'Belgium':2 , 'Canada':3}
    countries = countries_deficit()
    table_maker_a(countries)

main()