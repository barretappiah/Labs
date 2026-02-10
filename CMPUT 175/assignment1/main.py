
def countries_deficit():
    deficit = []

    # Gets country import export data
    with open('country.txt', 'r') as file:
        countries = file.read().splitlines()

        # Removes titles
        countries.pop(0)

        # Appends each countries deficit
        for country in countries:
            country = country.split(',')
            deficit.append([float(country[2]) - float(country[3]), country[1]])
    
    # Sorts by greatest deficit
    deficit.sort(key=lambda row: row[0], reverse=True)
    return deficit
              
def table_maker_a(deficit):
    titleOne = 'Country'
    titleTwo = 'Trade Deficit (Billions USD)'
    sizeOne = 34
    sizeTwo = 28

    top_five = deficit[:5]
    top_five_deficits = {country: value for value, country in top_five}

    # Formatting
    title = '| ' + titleOne + (' ' * (sizeOne - len(titleOne) - 1)) + ' | ' + titleTwo + (' ' * (sizeTwo - len(titleTwo))) + ' |'
    bar = '-' * len(title)

    # Display
    print(bar)
    print(title)
    print(bar)

    for country in top_five_deficits:
        print('| ' + country + (' ' * (sizeOne - len(country) - 1)) + ' | $' + (' ' * (sizeTwo - len(str(top_five_deficits[country])) - 1)) + str(top_five_deficits[country]) + ' |')
    
    print(bar)

def main():
    # Section A: countries with highest trade deficits

    deficit = countries_deficit()
    table_maker_a(deficit)

main()