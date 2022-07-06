def height_correlation(directory, database):
    
    '''
    Creates a table showing the correlation between height and having children
    for a given dictionary representing people from a database file,
    and saves the result to a file.

    Parameters:
    directory (string): A full path to the destination folder.
    database (dictionary): A variable assigned to a dictionary of people.
    '''

    heights = []
    for value in database.values():
        heights.append(value['Height'])

    output = []
    output.append(['Height (cm)', '% with children', '% without children'])

    for index in range(min(heights), max(heights), 10):

        with_children = []
        without_children = []
        for value in database.values():
            if value['Height'] in range(index, index + 10):
                if 'Children' in value:
                    with_children.append(value['Height'])
                if 'Children' not in value:
                    without_children.append(value['Height'])

        line = []
        line.append(str(index) + '-' + str(index + 10))
        line.append(len(with_children) /
                    len(with_children + without_children) * 100)
        line.append(len(without_children) /
                    len(with_children + without_children) * 100)
        output.append(line)

    save_csv(output, directory, 'height_correlation')