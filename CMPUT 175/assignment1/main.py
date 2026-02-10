


def table_maker_a(countries, size, titles):
    # Formatting
    title = '| ' + titles[0] + (' ' * (size[0] - len(titles[0]) - 1)) + ' | ' + titles[1] + (' ' * (size[1] - len(titles[1]))) + ' |'
    bar = '-' * len(title)

    # Display
    print(bar)
    print(title)
    print(bar)

    for country in countries:
        print('| ' + country + (' ' * (size[0] - len(country) - 1)) + ' | $' + (' ' * (size[1] - len(str(countries[country])) - 1)) + str(countries[country]) + ' |')

def main():
    # Section A: countries with highest trade deficits
    size = [14, 18]
    countries = {'Belgium':2 , 'Canada':3}
    titles = ['Industry', 'Number of Products']

    table_maker_a(countries, size, titles)

main()