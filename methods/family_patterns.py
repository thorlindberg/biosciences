def family_patterns(directory, database):
    
    '''
    Creates a line plot showing the evolution in the average amount of offspring
    over a period of time, and saves the result to a file.

    Parameters:
    directory (string): A full path to the destination folder.
    database (dictionary): A variable assigned to a dictionary of people.
    '''

    ages = []
    for value in database.values():
        if 'Children' in value:
            ages.append(value['Age'])

    y = []
    x = []

    for index in range(min(ages), max(ages), 10):

        children = []
        for value in database.values():
            if 'Children' in value and value['Age'] in range(index, index + 10):
                children.append(len(value['Children']))

        y.append(str(2000 - index - 10) + '-' + str(2000 - index))
        x.append(sum(children) / len(children))

    y.reverse()
    x.reverse()

    import matplotlib.pyplot as plt
    plot = plt.figure(figsize=(15, 5))
    plt.plot(y, x)
    plt.ylabel('Average amount of offspring')
    plt.xlabel('Year')
    plt.ylim(bottom=1)
    plt.grid(axis='both')
    save_plot(plot, directory, 'family_patterns')