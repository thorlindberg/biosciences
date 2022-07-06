def parents_with_multiple_partners(directory, database):
    
    '''
    Counts the amount of parents with multiple partners in a given dictionary
    representing people from a database file, and saves the result to a file.

    Parameters:
    directory (string): A full path to the destination folder.
    database (dictionary): A variable assigned to a dictionary of people.
    '''

    parents = []
    for key, value in database.items():

        if 'Children' in value:

            children = []

            for child in value['Children']:
                for subkey, subvalue in database.items():
                    if 'Children' in subvalue and subkey != key:
                        if child in subvalue['Children']:
                            children.append(subkey)

            for child in children:
                if child != children[0]:
                    parents.append(key)

    output = []
    output.append(
        ['How many parents have children with more than one person?', len(parents)])
    save_csv(output, directory, 'results')