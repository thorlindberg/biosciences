def height_evolution(directory, database):
    
    '''
    Creates a line plot showing the evolution of the average height over time,
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

        heights = []
        for value in database.values():
            if value['Age'] in range(index, index + 10):
                heights.append(value['Height'])

        y.append(str(2000 - index - 10) + '-' + str(2000 - index))
        x.append(sum(heights) / len(heights))

    y.reverse()
    x.reverse()

    import matplotlib.pyplot as plt
    plot = plt.figure(figsize=(15, 5))
    plt.plot(y, x)
    plt.ylabel('Average height (cm)')
    plt.xlabel('Year')
    plt.grid(axis='both')
    save_plot(plot, directory, 'height_evolution')