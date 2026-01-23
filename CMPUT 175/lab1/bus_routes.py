# Barret Appiah
# CMPUT 175
# Lab 1

# Loads code ID from station name
def name_to_code(location):
    with open("codes.txt", 'r') as file:
        code_locations = file.read().splitlines()

        for area in code_locations:
            code_name = area.split(',')
            
            if code_name[1].lower() == location.lower():
                return code_name[0]

# Loads station name from code ID          
def code_to_name(code):
    with open("codes.txt", 'r') as file:
        code_locations = file.read().splitlines()

        for area in code_locations:
            code_name = area.split(',')
            
            if code in code_name:
                return code_name[1]
            
# Returns string for entire route
def display_route(route):
    for i in range(1, len(route)):
        route[i] = code_to_name(route[i])

    your_route = ' -> '.join(route)
    return your_route

# Looks through all routes to find either one or two routes that can take you from start to stop  
def find_routes(starting_code, departing_code):
    with open("routes.txt", 'r')as file:
        routes = file.read().splitlines()

        # Direct Route
        for route in routes:
            route_list = route.split(',')
            if starting_code in route_list and departing_code in route_list:

                print(f'\nDirect route found: {display_route(route_list)}')
                return
            
        # Transfer Route
        starting_routes = []
        departing_routes = []

        # Fill in all routes with either start or depart locations
        for route in routes:
            route_list = route.split(',')
            if starting_code in route_list:
                starting_routes.append(route_list)
            if departing_code in route_list:
                departing_routes.append(route_list)

        # Find a common stop and display the entire route
        for start_route in starting_routes:
            for depart_route in departing_routes:
                for i in range(1, len(start_route)):
                    if start_route[i] in depart_route:
                        transfer_name = code_to_name(start_route[i])
                        print('\nTransfer option found:')
                        print(f'\nTake route {start_route[0]} and get off at {transfer_name}.\nThen take route {depart_route[0]} to your destination.\n')

                        print(f'Route {display_route(start_route)}')
                        print(f'Route {display_route(depart_route)}')
                        return
        
        print('No routes serving that start point and end point')
        

def main():
    start = input('Enter Starting Point: ')
    depart = input('Enter Destination: ')

    starting_code = name_to_code(start)
    departing_code = name_to_code(depart)

    find_routes(starting_code, departing_code)

main()