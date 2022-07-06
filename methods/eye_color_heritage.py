def eye_color_heritage(directory, database):
    
    '''
    Creates a table showing people with light eyes (grey or blue) who have
    parents who both have light eyes, and the colors of their parents' eyes,
    and saves the result to a file.

    Parameters:
    directory (string): A full path to the destination folder.
    database (dictionary): A variable assigned to a dictionary of people.
    '''

    output = []
    output.append(['Child', 'Eye color', 'Parent color', 'Parent color'])

    for key, value in database.items():

        line = []
        parents = []

        for parentvalue in database.values():
            if 'Children' in parentvalue and parentvalue['Color'] in ['Grey', 'Blue']:
                if key in parentvalue['Children']:
                    parents.append(parentvalue['Color'])

        if value['Color'] not in ['Grey', 'Blue'] and len(parents) == 2:
            line.append(value['Name'])
            line.append(value['Color'])
            line.append(parents[0])
            line.append(parents[1])

        if line != []:
            output.append(line)

    save_csv(output, directory, 'eye_color_heritage')