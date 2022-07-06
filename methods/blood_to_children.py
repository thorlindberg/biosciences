def blood_to_children(directory, database):
    
    '''
    Creates a table showing parents and their blood type, and their children who
    can receive blood from them, and saves the result to a file.

    Parameters:
    directory (string): A full path to the destination folder.
    database (dictionary): A variable assigned to a dictionary of people.
    '''

    chart = {
        'O+': ['O+', 'A+', 'B+', 'AB+'],
        'A+': ['A+', 'AB+'],
        'B+': ['B+', 'AB+'],
        'AB+': ['AB+'],
        'O-': ['O+', 'A+', 'B+', 'AB+', 'O-', 'A-', 'B-', 'AB-'],
        'A-': ['A-', 'A+', 'AB-', 'AB+'],
        'B-': ['B-', 'B+', 'AB-', 'AB+'],
        'AB-': ['AB-', 'AB+']
    }

    donators = {}
    for key, value in database.items():

        children = []
        if 'Children' in value:
            for child in value['Children']:
                if database[child]['Type'] in chart[value['Type']]:
                    children.append(child)

        if children != []:
            donators[key] = children

    output = []
    count = max([len(index) for index in donators.values()])
    output.append(['Parent', 'Type'] + ['Child', 'Type'] * count)

    for key, value in donators.items():
        line = []
        line.append(database[key]['Name'])
        line.append(database[key]['Type'])
        for child in value:
            line.append(database[child]['Name'])
            line.append(database[child]['Type'])
        output.append(line)

    save_csv(output, directory, 'blood_to_children')