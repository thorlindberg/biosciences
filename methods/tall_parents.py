def tall_parents(directory, database):
    
    '''
    Creates a table showing parents with a height above
    the average for their age and gender, the percentage of their children
    with a height above the average for their age and gender, and the percentage
    of their children with a height at or below the average
    for their age and gender, and saves the result to a file.

    Parameters:
    directory (string): A full path to the destination folder.
    database (dictionary): A variable assigned to a dictionary of people.
    '''

    tall = {
        0: {'Man': 50, 'Woman': 50},
        1: {'Man': 77, 'Woman': 75},
        2: {'Man': 88, 'Woman': 87},
        3: {'Man': 97, 'Woman': 95},
        4: {'Man': 105, 'Woman': 104},
        5: {'Man': 112, 'Woman': 111},
        6: {'Man': 119, 'Woman': 118},
        7: {'Man': 126, 'Woman': 124},
        8: {'Man': 132, 'Woman': 130},
        9: {'Man': 137, 'Woman': 136},
        10: {'Man': 143, 'Woman': 142},
        11: {'Man': 149, 'Woman': 148},
        12: {'Man': 153, 'Woman': 153},
        13: {'Man': 161, 'Woman': 158},
        14: {'Man': 167, 'Woman': 162},
        15: {'Man': 172, 'Woman': 165},
        16: {'Man': 176, 'Woman': 167},
        17: {'Man': 178, 'Woman': 168},
        18: {'Man': 180, 'Woman': 169},
        19: {'Man': 181, 'Woman': 170},
        20: {'Man': 182, 'Woman': 170}
    }

    parents = []
    for value in database.values():
        if 'Children' in value:
            if value['Height'] > tall.get(value['Age'], tall[max(tall.keys())])[value['Gender']]:
                parents.append(value['Height'])

    output = []
    output.append(['Height of parents (cm)', '% of children with height above average',
                  '% of children with height of average or below'])

    for index in range(min(parents), max(parents), 5):

        over = []
        under = []
        for value in database.values():
            if 'Children' in value:
                if value['Height'] in range(index, index + 5):
                    if value['Height'] > tall.get(value['Age'], tall[max(tall.keys())])[value['Gender']]:
                        for child in value['Children']:
                            if database[child]['Height'] > tall.get(database[child]['Age'], tall[max(tall.keys())])[database[child]['Gender']]:
                                over.append(database[child]['Height'])
                            if database[child]['Height'] <= tall.get(database[child]['Age'], tall[max(tall.keys())])[database[child]['Gender']]:
                                under.append(database[child]['Height'])

        line = []
        line.append(str(index) + '-' + str(index + 5))
        line.append(len(over) / len(over + under) * 100)
        line.append(len(under) / len(over + under) * 100)
        output.append(line)

    save_csv(output, directory, 'tall_parents')