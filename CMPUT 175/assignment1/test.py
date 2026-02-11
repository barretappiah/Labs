from collections import defaultdict

def count_exclusive_products(filename="product_country.txt"):
    pid_countries = defaultdict(set)

    with open(filename, "r") as f:
        lines = f.read().splitlines()

    for line in lines[1:]:  # skip header
        pid, country, price = [x.strip() for x in line.split(",")]
        pid_countries[pid].add(country)

    # exclusive = produced by exactly 1 country
    exclusive_count = sum(1 for countries in pid_countries.values() if len(countries) == 1)
    return exclusive_count

print(count_exclusive_products())