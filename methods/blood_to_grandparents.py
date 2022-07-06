def blood_to_grandparents(directory, database):
    
    '''
    Creates a table showing grandparents and their blood type, and their
    grandchildren who can donate blood to them, and saves the result to a file.

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

        grandchildren = []
        if 'Children' in value:
            for child in value['Children']:
                if 'Children' in database[child]:
                    for grandchild in database[child]['Children']:
                        if database[key]['Type'] in chart[database[grandchild]['Type']]:
                            grandchildren.append(grandchild)

        if grandchildren != []:
            donators[key] = grandchildren

    output = []
    count = max([len(index) for index in donators.values()])
    output.append(['Grandparent', 'Type'] + ['Grandchild', 'Type'] * count)

    for key, value in donators.items():
        line = []
        line.append(database[key]['Name'])
        line.append(database[key]['Type'])
        for grandchild in value:
            line.append(database[grandchild]['Name'])
            line.append(database[grandchild]['Type'])
        output.append(line)

    save_csv(output, directory, 'blood_to_grandparents')