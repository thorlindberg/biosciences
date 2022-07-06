def weight_evolution(directory, database):
    
    '''
    Creates a line plot showing the evolution of the average weight over time,
    for people from a database file, and saves the result to a file.

    Parameters:
    directory (string): A full path to the destination folder.
    database (dictionary): A variable assigned to a dictionary of people.
    '''

    ages = []
    for value in database.values():
        ages.append(value['Age'])

    y = []
    x = []

    for index in range(min(ages), max(ages), 10):

        weights = []
        for value in database.values():
            if value['Age'] in range(index, index + 10):
                weights.append(value['Weight'])

        y.append(str(2000 - index - 10) + '-' + str(2000 - index))
        x.append(sum(weights) / len(weights))

    y.reverse()
    x.reverse()

    import matplotlib.pyplot as plt
    plot = plt.figure(figsize=(15, 5))
    plt.plot(y, x)
    plt.ylabel('Average weight (kg)')
    plt.xlabel('Year')
    plt.grid(axis='both')
    save_plot(plot, directory, 'weight_evolution')