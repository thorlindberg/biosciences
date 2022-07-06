def count_children(directory, database):
    
    '''
    Counts the amount of children in a given dictionary representing people from
    a database file, and saves the result to a file.

    Parameters:
    directory (string): A full path to the destination folder.
    database (dictionary): A variable assigned to a dictionary of people.
    '''

    children = []
    for value in database.values():
        if 'Children' in value:
            for child in value['Children']:
                if child not in children:
                    children.append(child)

    output = []
    output.append(['How many children are in the database?', len(children)])
    save_csv(output, directory, 'results')