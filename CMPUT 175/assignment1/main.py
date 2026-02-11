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
    exclusivity = {}

    for product in exclusive_products:
        country = product[0]

        if country not in exclusivity:
            exclusivity[country] = 0
        exclusivity[country] += 1
    
    exclusive_country = max(exclusivity, key=exclusivity.get)

    return [exclusive_country, exclusivity[exclusive_country]]

def least_exclusive(exclusive_products):

    with open('product.txt', 'r') as file:
        products = file.read().splitlines()
        industries = {'Agriculture': 0, 'Food': 0, 'Manufacturing': 0, 'Pharmacy': 0, 'Tech': 0}

        for exclusive in exclusive_products:
            for product in products:
                product = product.strip().split(',')
                if exclusive[1] == product[0]:
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

    least_exclusive_industry = [min(industries), industries[min(industries)]]
    return least_exclusive_industry

def most_productive_countries():
    # Count number of products produced by each country code
    counts = {}
    with open('product_country.txt', 'r') as file:
        lines = file.read().splitlines()
        for line in lines[1:]:
            parts = [x.strip() for x in line.split(',')]
            if len(parts) < 2:
                continue
            code = parts[1]
            counts[code] = counts.get(code, 0) + 1

    if not counts:
        return [[], 0]

    max_count = max(counts.values())
    # all country codes that have the max count
    top_codes = [code for code, c in counts.items() if c == max_count]

    # map codes to country names
    code_to_name = {}
    with open('country.txt', 'r') as file:
        for line in file.read().splitlines()[1:]:
            parts = [x.strip() for x in line.split(',')]
            if len(parts) >= 2:
                code_to_name[parts[0]] = parts[1]

    names = [code_to_name.get(code, code) for code in top_codes]
    names.sort()
    return [names, max_count]

def most_widespread_products():
    # Build set of producing countries per PID
    pid_countries = {}
    with open('product_country.txt', 'r') as file:
        lines = file.read().splitlines()
        for line in lines[1:]:
            parts = [x.strip() for x in line.split(',')]
            if len(parts) < 2:
                continue
            pid = parts[0]
            code = parts[1]
            pid_countries.setdefault(pid, set()).add(code)

    # Count countries per PID
    pid_counts = {pid: len(cset) for pid, cset in pid_countries.items()}
    if not pid_counts:
        return []

    # Top three distinct counts
    unique_counts = sorted(set(pid_counts.values()), reverse=True)
    top_values = unique_counts[:3]

    # Select PIDs whose count is in top_values
    selected = [(pid, pid_counts[pid]) for pid in pid_counts if pid_counts[pid] in top_values]

    # Map PID to product name
    pid_to_name = {}
    with open('product.txt', 'r') as file:
        for line in file.read().splitlines()[1:]:
            parts = [x.strip() for x in line.split(',')]
            if len(parts) >= 3:
                pid_to_name[parts[0]] = parts[2]

    results = []
    for pid, cnt in selected:
        name = pid_to_name.get(pid, pid)
        results.append([name, cnt])

    # Sort by number of countries (desc), then product name (asc)
    results.sort(key=lambda x: (-x[1], x[0]))
    return results
        
def table_maker_b(industries, products, exclusive_country, inclusive_industry, most_productive, most_widespread):
    print('\n\n--------------------- SECTION B ---------------------\n')

    # ----------
    # INDUSTRIES 1.
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
    # EXCLUSIVES 2.
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

    # --------------
    # Most Exclusive 3.
    # --------------

    titleOne = 'Country'
    titleTwo = 'No. of Exclusive Products'
    sizeOne = 13
    sizeTwo = 26

    # Formatting
    title = '| ' + titleOne + (' ' * (sizeOne - len(titleOne))) + ' | ' + titleTwo + (' ' * (sizeTwo - len(titleTwo))) + ' |'
    bar = '-' * len(title)

    # Output
    print(bar)
    print(title)
    print(bar)
    print('| ' + str(exclusive_country[0]) + (' ' * (sizeOne - len(str(exclusive_country[0])))) + ' | ' + (' ' * (sizeTwo - len(str(exclusive_country[1])))) + str(exclusive_country[1]) + ' |')
    print(bar)

    # ---------------
    # Least Exclusive 4.
    # ---------------

    titleOne = 'Industry'
    titleTwo = 'No. of Exclusive Products'
    sizeOne = 13
    sizeTwo = 26

    # Formatting
    title = '| ' + titleOne + (' ' * (sizeOne - len(titleOne))) + ' | ' + titleTwo + (' ' * (sizeTwo - len(titleTwo))) + ' |'
    bar = '-' * len(title)

    # Output
    print(bar)
    print(title)
    print(bar)
    print('| ' + inclusive_industry[0] + (' ' * (sizeOne - len(str(inclusive_industry[0])))) + ' | ' + (' ' * (sizeTwo - len(str(inclusive_industry[1])))) + str(inclusive_industry[1]) + ' |')
    print(bar)

    # ---------------
    # Most Productive 5.
    # ---------------

    titleOne = 'Country'
    titleTwo = 'Number of Products'
    sizeOne = 13
    sizeTwo = 26

    # Formatting
    title = '| ' + titleOne + (' ' * (sizeOne - len(titleOne))) + ' | ' + titleTwo + (' ' * (sizeTwo - len(titleTwo))) + ' |'
    bar = '-' * len(title)

    # Output
    print(bar)
    print(title)
    print(bar)
    # most_productive: [list_of_country_names, count]
    if most_productive and most_productive[0]:
        countries = ', '.join(most_productive[0])
        count = most_productive[1]
    else:
        countries = ''
        count = 0

    print('| ' + countries + (' ' * (sizeOne - len(str(countries)))) + ' | ' + (' ' * (sizeTwo - len(str(count)))) + str(count) + ' |')
    print(bar)

    # ---------------
    # Most Widespread 6.
    # ---------------

    titleOne = 'Product Name'
    titleTwo = 'Number of Countries'
    sizeOne = 45
    sizeTwo = 18

    title = '| ' + titleOne + (' ' * (sizeOne - len(titleOne))) + ' | ' + titleTwo + (' ' * (sizeTwo - len(titleTwo))) + ' |'
    bar = '-' * len(title)

    print(bar)
    print(title)
    print(bar)
    for item in most_widespread:
        name = item[0]
        count = item[1]
        print('| ' + name + (' ' * (sizeOne - len(name))) + ' | ' + (' ' * (sizeTwo - len(str(count)))) + str(count) + ' |')
    print(bar)


def main():
    # Section A: countries with highest trade deficits
    deficit = countries_deficit()
    table_maker_a(deficit)

    # Section B: understanding product availability
    industries = industry_products()
    products = exlusive_products()
    most_exclusive_country = most_exclusive(products)
    least_exclusive_industry = least_exclusive(products)
    most_productive = most_productive_countries()
    most_widespread = most_widespread_products()
    table_maker_b(industries, products, most_exclusive_country, least_exclusive_industry, most_productive, most_widespread)

main()