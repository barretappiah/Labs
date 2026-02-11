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
    print('\n\n--------------------- SECTION A ---------------------\n')

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
    pid_countries = {}

    with open('product_country.txt', 'r') as file:
        products = file.read().splitlines()

    for line in products[1:]:
        pid, country, price = [x.strip() for x in line.split(',')]

        if pid not in pid_countries:
            pid_countries[pid] = set()
        pid_countries[pid].add(country)

    exclusive_pids = {}

    for pid in pid_countries:
        if len(pid_countries[pid]) == 1:
            exclusive_pids[pid] = pid_countries[pid]

    exclusive_pids_titled = []
    with open('product.txt', 'r') as file:
        products = file.read().splitlines()

    for pid in exclusive_pids:
        for product in products:
            product = product.strip().split(',')

            if product[0] == str(pid):
                exclusive_pids_titled.append(product)

    with open('country.txt', 'r') as file:
        countries = file.read().splitlines()

    exclusive_products = []

    for i in range(len(exclusive_pids_titled)):
        exclusive_products.append([list(exclusive_pids[exclusive_pids_titled[i][0]])[0], exclusive_pids_titled[i][0], exclusive_pids_titled[i][2]])

    filtered_products = []

    for product in exclusive_products:
        for country in countries:
            country = country.strip().split(',')

            coded = product[0]
            if country[0] == product[0]:
                product[0] = country[1]
            if product[0] != coded:
                filtered_products.append(product)

    return filtered_products

def most_exclusive(exclusive_products):
    return exclusive_products

def table_maker_b(industries, products):
    print('\n\n--------------------- SECTION B ---------------------\n')

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
    sizeTwo = 35
    sizeThree = 40

    # Formatting
    title = '| ' + titleOne + (' ' * (sizeOne - len(titleOne))) + ' | ' + titleTwo + (' ' * (sizeTwo - len(titleTwo))) + ' | '+ titleThree + (' ' * (sizeThree - len(titleThree))) + ' |'
    bar = '-' * len(title)

    # Output
    print(bar)
    print(title)
    print(bar)

    for product in products:
        print('| ' + product[1] + (' ' * (sizeOne - len(product[1]))) + ' | ' + product[0] + (' ' * (sizeTwo - len(product[0]))) + ' | '+ product[2] + (' ' * (sizeThree - len(product[2]))) + ' |')
    
    print(bar)

def main():
    # Section A: countries with highest trade deficits
    deficit = countries_deficit()
    table_maker_a(deficit)

    # Section B: understanding product availability
    industries = industry_products()
    products = exlusive_products()
    most_exclusive_country = most_exclusive(products)
    print(most_exclusive_country)
    table_maker_b(industries, products)

main()