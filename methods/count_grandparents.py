def count_grandparents(directory, database):
    
    '''
    Counts the amount of grandparents in a given dictionary representing people
    from a database file, and saves the result to a file.

    Parameters:
    directory (string): A full path to the destination folder.
    database (dictionary): A variable assigned to a dictionary of people.
    '''

    grandparents = []
    for key, value in database.items():
        if 'Children' in value:
            for child in value['Children']:
                if 'Children' in database[child]:
                    if key not in grandparents:
                        grandparents.append(key)

    output = []
    output.append(
        ['How many grandparents are in the database?', len(grandparents)])
    save_csv(output, directory, 'results')