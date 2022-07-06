def overweight_parents(directory, database):
    
    '''
    Creates a table showing parents with a BMI of 25 or above (overweight),
    the percentage of their children with a BMI of 25 or above, and the
    percentage of their children with a BMI under 25, and saves it to a file.

    Parameters:
    directory (string): A full path to the destination folder.
    database (dictionary): A variable assigned to a dictionary of people.
    '''

    parents = []
    for value in database.values():
        if 'Children' in value and value['Weight'] / ((value['Height'] / 100) ** 2) >= 25:
            parents.append(
                int(value['Weight'] / ((value['Height'] / 100) ** 2)))

    output = []
    output.append(['BMI of parents', '% of children with BMI of 25 or over in range',
                  '% of children with BMI under 25 in range'])

    for index in range(min(parents), max(parents), 5):

        over = []
        under = []
        for value in database.values():
            if 'Children' in value:
                if int(value['Weight'] / ((value['Height'] / 100) ** 2)) in range(index, index + 5):
                    for child in value['Children']:
                        if database[child]['Weight'] / ((database[child]['Height'] / 100) ** 2) >= 25:
                            over.append(
                                database[child]['Weight'] / ((database[child]['Height'] / 100) ** 2))
                        if database[child]['Weight'] / ((database[child]['Height'] / 100) ** 2) < 25:
                            under.append(
                                database[child]['Weight'] / ((database[child]['Height'] / 100) ** 2))

        line = []
        line.append(str(index) + '-' + str(index + 5))
        line.append(len(over) / len(over + under) * 100)
        line.append(len(under) / len(over + under) * 100)
        output.append(line)

    save_csv(output, directory, 'overweight_parents')