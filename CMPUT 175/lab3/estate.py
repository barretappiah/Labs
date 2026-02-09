
# Retrieves chosen company details along with their propertiess
def retrieve_firm_data(chosen_firm):
    # Finds firm ID, along with founding date
    with open('ownership.txt', 'r') as file_ownership:
        data = file_ownership.read().splitlines()
        data = data[1:]
        firm_data = []

        for firm in data:
            firm = firm.strip().split(',')

            if firm[1] == chosen_firm:
                firm_data = firm

        firm_id = firm_data[0]

        # Finds which properties are related to the firm id found above
        with open('properties.txt', 'r') as file_properties:
            property_data = file_properties.read().splitlines()
            property_data = property_data[1:]
            
            firm_properties = []

            for select_property in property_data:
                select_property = select_property.strip().split(',')

                if select_property[3] == firm_id:
                    firm_properties.append(select_property)

        return firm_data, firm_properties

def main():
    chosen_firm = 'Nest Properties'
    data, properties = retrieve_firm_data(chosen_firm)
    print(data)
    print(properties)

main()