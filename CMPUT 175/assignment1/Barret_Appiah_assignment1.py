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

            code = parts[1]
            counts[code] = counts.get(code, 0) + 1


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
    # Dict of each pid, and how many countries produce it
    pid_countries = {}
    with open('product_country.txt', 'r') as file:
        lines = file.read().splitlines()
        for line in lines[1:]:
            parts = [x.strip() for x in line.split(',')]

            pid = parts[0]
            code = parts[1]

            # Quicker way to assign values to key, or make a key and assign a value
            pid_countries.setdefault(pid, set()).add(code)

    # Count countries per PID, PID : canada, usa, mexico --> PID: 3
    pid_counts = {pid: len(cset) for pid, cset in pid_countries.items()}

   
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
        print('| ' + name + (' ' * (sizeOne - len(name))) + ' |  ' + (' ' * (sizeTwo - len(str(count)))) + str(count) + ' |')
    print(bar)

# Section C
def load_country_codes_to_names():
    d = {}
    with open('country.txt', 'r') as f:
        for line in f.read().splitlines()[1:]:
            parts = [x.strip() for x in line.split(',')]
            d[parts[0]] = parts[1]
    return d

def load_tariffs():
    # returns dict code -> dict industry -> percentage
    tariffs = {}
    with open('tariff.txt', 'r') as f:
        for line in f.read().splitlines()[1:]:
            parts = [x.strip() for x in line.split(',')]
            code, industry, perc = parts[0], parts[1], parts[2]

            p = float(perc)

            tariffs.setdefault(code, {})[industry] = p
    return tariffs

def outrageous_tariff_countries():
    tariffs = load_tariffs()
    code_to_name = load_country_codes_to_names()
    codes = [code for code, inds in tariffs.items() if any(v > 50 for v in inds.values())]
    names = [code_to_name.get(c) for c in codes]
    names.sort()
    return names

def tariff_free_countries():
    code_to_name = load_country_codes_to_names()
    tariffs = load_tariffs()
    tariff_codes = set(tariffs.keys())
    free = [name for code, name in code_to_name.items() if code not in tariff_codes]
    free.sort()
    return free

def selective_tariff_countries():
    # industries universe (same as used elsewhere)
    all_industries = {'Agriculture', 'Food', 'Manufacturing', 'Pharmacy', 'Tech'}
    code_to_name = load_country_codes_to_names()
    tariffs = load_tariffs()

    results = []
    for code, name in code_to_name.items():
        present = set(tariffs.get(code, {}).keys())
        # must have some tariffs but not all
        if 0 < len(present) < len(all_industries):
            missing = sorted(all_industries - present)
            for industry in missing:
                results.append([name, industry])

    # sort by country then industry
    results.sort(key=lambda x: (x[0], x[1]))
    return results

def table_maker_c(outrageous, tariff_free, selective):
    print('\n\n--------------------- SECTION C ---------------------\n')

    # 1. Outrageous Tariffs
    titleOne = 'Country'
    sizeOne = 40
    title = '| ' + titleOne + (' ' * (sizeOne - len(titleOne))) + ' |'
    bar = '-' * len(title)

    print(bar)
    print(title)
    print(bar)
    for country in outrageous:
        print('| ' + country + (' ' * (sizeOne - len(country))) + ' |')
    print(bar)

    # 2. Tariff-Free Countries
    titleOne = 'Country'
    sizeOne = 40
    title = '| ' + titleOne + (' ' * (sizeOne - len(titleOne))) + ' |'
    bar = '-' * len(title)

    print('\n' + bar)
    print(title)
    print(bar)
    for country in tariff_free:
        print('| ' + country + (' ' * (sizeOne - len(country))) + ' |')
    print(bar)

    # 3. Selective Tariff Countries
    titleOne = 'Country'
    titleTwo = 'Industry'
    sizeOne = 27
    sizeTwo = 20
    title = '| ' + titleOne + (' ' * (sizeOne - len(titleOne))) + ' | ' + titleTwo + (' ' * (sizeTwo - len(titleTwo))) + ' |'
    bar = '-' * len(title)

    print('\n' + bar)
    print(title)
    print(bar)
    for country, industry in selective:
        print('| ' + country + (' ' * (sizeOne - len(country))) + ' | ' + industry + (' ' * (sizeTwo - len(industry))) + ' |')
    print(bar)

# Section D
def cheapest_import_strategy(home_code='US'):
    # load helpers
    code_to_name = load_country_codes_to_names()
    tariffs = load_tariffs()

    # load product metadata
    pid_to_name = {}
    pid_to_industry = {}
    with open('product.txt', 'r') as f:
        for line in f.read().splitlines()[1:]:
            parts = [x.strip() for x in line.split(',')]
            if len(parts) >= 3:
                pid_to_name[parts[0]] = parts[2]
                pid_to_industry[parts[0]] = parts[1].strip()

    # load producers and prices
    pid_producers = {}
    with open('product_country.txt', 'r') as f:
        for line in f.read().splitlines()[1:]:
            parts = [x.strip() for x in line.split(',')]

            pid, code, price = parts[0], parts[1], parts[2]

            p = float(price)

            pid_producers.setdefault(pid, []).append((code, p))

    # read shopping list (order matters)
    with open('shopping_list.txt', 'r') as f:
        shopping = [line.strip() for line in f.read().splitlines() if line.strip()]

    rows = []
    total_actual = 0.0
    total_tariff = 0.0

    home_tariffs = tariffs.get(home_code, {})

    for pid in shopping:
        name = pid_to_name.get(pid, pid)
        industry = pid_to_industry.get(pid, '')
        producers = pid_producers.get(pid, [])


        best = None
        best_country_name = ''
        best_price = 0.0
        best_tariff_pct = 0.0
        best_tariff_val = 0.0
        best_total = 0.0

        for code, price in producers:
            tariff_pct = home_tariffs.get(industry, 0.0)
            tariff_val = price * (tariff_pct / 100.0)
            total = price + tariff_val
            cname = code_to_name.get(code, code)
            candidate = (total, cname, price, tariff_pct, tariff_val)
            if best is None or (candidate[0] < best[0]) or (candidate[0] == best[0] and candidate[1] < best[1]):
                best = candidate
                best_country_name = cname
                best_price = price
                best_tariff_pct = tariff_pct
                best_tariff_val = tariff_val
                best_total = total

        rows.append([name, len(producers), best_country_name, best_price, best_tariff_pct, best_tariff_val, best_total])
        total_actual += best_price
        total_tariff += best_tariff_val

    grand_total = total_actual + total_tariff
    return rows, total_actual, total_tariff, grand_total

def table_maker_d(rows, total_actual, total_tariff, grand_total):
    print('\n\n--------------------- SECTION D ---------------------\n')

    titleOne = 'Product Name'
    titleTwo = 'Countries'
    titleThree = 'Best Country'
    titleFour = 'Actual Cost'
    titleFive = 'Tariff %'
    titleSix = 'Tariff Val'
    titleSeven = 'Total Cost'

    sizeOne = 30
    sizeTwo = 9
    sizeThree = 18
    sizeFour = 14
    sizeFive = 9
    sizeSix = 14
    sizeSeven = 14

    # product name and best country: left-justify; numeric columns: right-justify
    title = ('| ' + titleOne + (' ' * (sizeOne - len(titleOne))) +
             ' | ' + (' ' * (sizeTwo - len(titleTwo))) + titleTwo +
             ' | ' + titleThree + (' ' * (sizeThree - len(titleThree))) +
             ' | ' + (' ' * (sizeFour - len(titleFour))) + titleFour +
             ' | ' + (' ' * (sizeFive - len(titleFive))) + titleFive +
             ' | ' + (' ' * (sizeSix - len(titleSix))) + titleSix +
             ' | ' + (' ' * (sizeSeven - len(titleSeven))) + titleSeven + ' |')
    bar = '-' * len(title)

    print(bar)
    print(title)
    print(bar)

    for r in rows:
        name, countries, best_country, actual, pct, tval, total = r
        actual_s = f"{actual:,.2f}"
        tval_s = f"{tval:,.2f}"
        total_s = f"{total:,.2f}"
        pct_s = f"{pct:.1f}%"

        # left-justify text fields, right-justify numeric fields
        print('| ' + name + (' ' * (sizeOne - len(name))) +
            ' | ' + (' ' * (sizeTwo - len(str(countries)))) + str(countries) +
            ' | ' + best_country + (' ' * (sizeThree - len(best_country))) +
            ' | ' + '$' + (' ' * (sizeFour - len(actual_s) - 1)) + actual_s +
            ' | ' + (' ' * (sizeFive - len(pct_s))) + pct_s +
            ' | ' + '$' + (' ' * (sizeSix - len(tval_s) - 1)) + tval_s +
            ' | ' + '$' + (' ' * (sizeSeven - len(total_s) - 1)) + total_s + ' |')

    print(bar)
    print(f"Cost Before Tariff: $ {total_actual:,.2f}")
    print(f"Total Tariff Paid: $ {total_tariff:,.2f}")
    print(f"Grand Total: $ {grand_total:,.2f}")
    
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

    # Section C: analyzing government's tariff decisions
    outrageous = outrageous_tariff_countries()
    tariff_free = tariff_free_countries()
    selective = selective_tariff_countries()
    table_maker_c(outrageous, tariff_free, selective)

    # Section D: Shopping list cost breakdown (default home country = 'US')
    rows, total_actual, total_tariff, grand_total = cheapest_import_strategy('US')
    table_maker_d(rows, total_actual, total_tariff, grand_total)

main()