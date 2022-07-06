def first_time_mother(directory, database):
    
    '''
    Creates a pie plot of first-time motherhood, where each slice represents
    an age range, saving it to a file, and determines the average age for
    first-time motherhood, saving it to a separate file.

    Parameters:
    directory (string): A full path to the destination folder.
    database (dictionary): A variable assigned to a dictionary of people.
    '''

    ages = []
    for value in database.values():
        if 'Children' in value and value['Gender'] == 'Woman':
            children = []
            for child in value['Children']:
                children.append(database[child]['Age'])
            ages.append(value['Age'] - max(children))

    y = []
    x = []

    for index in range(min(ages), max(ages), 3):

        firsts = []
        for age in ages:
            if age in range(index, index + 3):
                firsts.append(age)

        y.append(str(index) + '-' + str(index + 3))
        x.append(len(firsts) / len(ages) * 100)

    import matplotlib.pyplot as plt
    plot = plt.figure(figsize=(5, 5))
    plt.pie(x, labels=y)
    plt.title('First-time motherhood ages')
    save_plot(plot, directory, 'first_time_mother')

    output = []
    output.append(
        ['What is the average age for first-time motherhood?', sum(ages) / len(ages)])
    save_csv(output, directory, 'results')