def count_people(directory, database):
    
    '''
    Counts the amount of people in a given dictionary representing people from
    a database file, and saves the result to a file.

    Parameters:
    directory (string): A full path to the destination folder.
    database (dictionary): A variable assigned to a dictionary of people.
    '''

    output = []
    output.append(['How many people are in the database?', len(database)])
    save_csv(output, directory, 'results')
