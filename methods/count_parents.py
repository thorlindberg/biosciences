def count_parents(directory, database):
    
    '''
    Counts the amount of parents in a given dictionary representing people from
    a database file, and saves the result to a file.

    Parameters:
    directory (string): A full path to the destination folder.
    database (dictionary): A variable assigned to a dictionary of people.
    '''

    parents = []
    for key, value in database.items():
        if 'Children' in value:
            parents.append(key)

    output = []
    output.append(['How many parents are in the database?', len(parents)])
    save_csv(output, directory, 'results')