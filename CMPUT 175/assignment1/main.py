# Section A
def countries_deficit():
    deficit = []

    # Gets country import export data
    with open('country.txt', 'r') as file:
        countries = file.read().splitlines()

        # Removes titles
        countries.pop(0)

        # Appends each countries deficit
        for country in countries:
            country = country.strip().split(',')
            deficit.append([float(country[2]) - float(country[3]), country[1]])
    
    # Sorts by greatest deficit
    deficit.sort(key=lambda row: row[0], reverse=True)
    return deficit
              
def table_maker_a(deficit):
    titleOne = 'Country'
    titleTwo = 'Trade Deficit (Billions USD)'
    sizeOne = 34
    sizeTwo = 27

    top_five = deficit[:5]
    top_five_deficits = {country: value for value, country in top_five}

    # Formatting
    title = '| ' + titleOne + (' ' * (sizeOne - len(titleOne))) + ' | ' + titleTwo + (' ' * (sizeTwo - len(titleTwo))) + ' |'
    bar = '-' * len(title)

    # Display
    print(bar)
    print(title)
    print(bar)

    for country in top_five_deficits:
        print('| ' + country + (' ' * (sizeOne - len(country))) + ' | $' + (' ' * (sizeTwo - len(str(top_five_deficits[country])))) + str(top_five_deficits[country]) + ' |')
    
    print(bar)

# Section B
def industry_products():
    industries = {'Agriculture': 0, 'Food': 0, 'Manufacturing': 0, 'Pharmacy': 0, 'Tech': 0}

    with open('product.txt', 'r') as file:
        products = file.read().splitlines()
        
        for product in products:
            product = product.strip().split(',')
            
            if product[1].strip() == 'Agriculture':
                industries['Agriculture'] += 1
            elif product[1].strip() == 'Food':
                industries['Food'] += 1
            elif product[1].strip() == 'Manufacturing':
                industries['Manufacturing'] += 1
            elif product[1].strip() == 'Pharmacy':
                industries['Pharmacy'] += 1
            elif product[1].strip() == 'Tech':
                industries['Tech'] += 1
    
    return industries

def exlusive_products():
    with open('product.txt', 'r') as file:
        products = file.read().splitlines()

        for product in products:
            product = product.strip().split(',')
            print(product)


def table_maker_b(industries, products):

    # ----------
    # INDUSTRIES
    # ----------
    titleOne = 'Industry'
    titleTwo = 'Number of Products'
    sizeOne = 14
    sizeTwo = 18

    # Formatting
    title = '| ' + titleOne + (' ' * (sizeOne - len(titleOne))) + ' | ' + titleTwo + (' ' * (sizeTwo - len(titleTwo))) + ' |'
    bar = '-' * len(title)

    # Output
    print(bar)
    print(title)
    print(bar)
    for industry in industries:
        print('| ' + industry + (' ' * (sizeOne - len(industry))) + ' | ' + (' ' * (sizeTwo - len(str(industries[industry])))) + str(industries[industry]) + ' |')
    print(bar)

    # ----------
    # EXCLUSIVES
    # ----------

    titleOne = 'PID'
    titleTwo = 'Product Name'
    titleThree = 'Producing Country'
    sizeOne = 9
    sizeTwo = 15
    sizeThree = 35

    # Formatting
    title = '| ' + titleOne + (' ' * (sizeOne - len(titleOne))) + ' | ' + titleTwo + (' ' * (sizeTwo - len(titleTwo))) + ' | '+ titleThree + (' ' * (sizeThree - len(titleThree))) + ' |'
    bar = '-' * len(title)

    # Output
    print(bar)
    print(title)
    print(bar)

    for product in products:
        print('| ' + products[product][1] + (' ' * (sizeOne - len(products[product][1]))) + ' | ' + product + (' ' * (sizeTwo - len(product))) + ' | '+ products[product][0] + (' ' * (sizeThree - len(products[product][0]))) + ' |')
    
    print(bar)

def main():
    # Section A: countries with highest trade deficits
    deficit = countries_deficit()
    table_maker_a(deficit)

    # Section B: understanding product availability
    industries = industry_products()
    products = exlusive_products()
    products = {'GoPro HERO11': ['Niger (the)', 'MKS009'], 'Television': ['Canada', 'MKDFS922']}
    table_maker_b(industries, products)

main()