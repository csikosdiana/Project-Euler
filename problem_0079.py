'''
Passcode derivation

A common security method used for online banking is to ask the user for three random characters from a passcode.
For example, if the passcode was 531278, they may ask for the 2nd, 3rd, and 5th characters; the expected reply would be: 317.

The text file, keylog.txt, contains fifty successful login attempts.

Given that the three characters are always asked for in order, analyse the file so as to determine the shortest possible
secret passcode of unknown length.
'''


def passcode_derivation(filename):
    routes = {0: [], 1: [], 2: [], 3: [], 4: [], 5: [], 6: [], 7: [], 8: [], 9: []}
    routes_length = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0}

    seen_numbers = []

    for line in open(filename):
        password_chars = list(map(int, line.rstrip()))

        seen_numbers += [n for n in password_chars if n not in seen_numbers]

        if password_chars[1] not in routes[password_chars[0]]:
            routes[password_chars[0]].append(password_chars[1])
            routes_length[password_chars[0]] += 1
        if password_chars[2] not in routes[password_chars[1]]:
            routes[password_chars[1]].append(password_chars[2])
            routes_length[password_chars[1]] += 1

    value_with_0_lenght = None

    for n in range(0, 10):
        if n not in seen_numbers:
            del routes[n]
            del routes_length[n]
        else:
            if routes_length[n] == 0:
                value_with_0_lenght = n

    passcode = ''

    while len(routes):
        passcode = str(value_with_0_lenght) + passcode
        del routes_length[value_with_0_lenght]
        del routes[value_with_0_lenght]

        new_routes = {}
        for key, value in routes.items():
            new_value = [v for v in value if v != value_with_0_lenght]
            if value_with_0_lenght in value:
                routes_length[key] -= 1
                if routes_length[key] == 0:
                    new_value_with_0_lenght = key

            new_routes[key] = new_value
        routes = new_routes
        value_with_0_lenght = new_value_with_0_lenght

    return passcode
        


print(passcode_derivation("problem_0079.txt"))  # 73162890
