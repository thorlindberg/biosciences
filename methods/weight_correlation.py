def weight_correlation(directory, database):
    
    '''
    Creates a table showing the correlation between weight and having children
    for a given dictionary representing people from a database file,
    and saves the result to a file.

    Parameters:
    directory (string): A full path to the destination folder.
    database (dictionary): A variable assigned to a dictionary of people.
    '''

    weights = []
    for value in database.values():
        weights.append(value['Weight'])

    output = []
    output.append(['Weight (kg)', '% with children', '% without children'])

    for index in range(min(weights), max(weights), 10):

        with_children = []
        without_children = []
        for value in database.values():
            if value['Weight'] in range(index, index + 10):
                if 'Children' in value:
                    with_children.append(value['Weight'])
                if 'Children' not in value:
                    without_children.append(value['Weight'])

        line = []
        line.append(str(index) + '-' + str(index + 10))
        line.append(len(with_children) /
                    len(with_children + without_children) * 100)
        line.append(len(without_children) /
                    len(with_children + without_children) * 100)
        output.append(line)

    save_csv(output, directory, 'weight_correlation')