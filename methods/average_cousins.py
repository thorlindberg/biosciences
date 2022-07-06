def average_cousins(directory, database):
    
    '''
    Counts the average amount of cousins for people with cousins in a given
    dictionary representing people from a database file, and saves the result
    to a file.

    Parameters:
    directory (string): A full path to the destination folder.
    database (dictionary): A variable assigned to a dictionary of people.
    '''

    cousins = {}
    for key, value in database.items():

        cousin = []
        for parent_key, parent_value in database.items():
            if 'Children' in parent_value and key in parent_value['Children']:
                for grandparent_key, grandparent_value in database.items():
                    if 'Children' in grandparent_value and parent_key in grandparent_value['Children']:
                        for parent in grandparent_value['Children']:
                            if parent != parent_key and 'Children' in database[parent]:
                                for child in database[parent]['Children']:
                                    if child not in cousin:
                                        cousin.append(child)

        if cousin != []:
            cousins[key] = cousin

    cousins = [len(index) for index in cousins.values()]

    output = []
    output.append(['What is the average amount of cousins for people with cousins?', sum(
        cousins) / len(cousins)])
    save_csv(output, directory, 'results')