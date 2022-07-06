def age_gender_distribution(directory, database):
    
    '''
    Creates a table of the distribution of age and gender in a given dictionary
    representing people from a database file, and saves the result to a file.

    Parameters:
    directory (string): A full path to the destination folder.
    database (dictionary): A variable assigned to a dictionary of people.
    '''

    ages = []
    for value in database.values():
        ages.append(value['Age'])

    output = []
    output.append(
        ['Age', '% of all', '% of women in range', '% of men in range'])

    women_ages = []
    men_ages = []
    for index in range(min(ages), max(ages), 20):

        women = []
        men = []
        for value in database.values():
            if value['Age'] in range(index, index + 20):

                if value['Gender'] == 'Woman':
                    women.append(value['Age'])
                    women_ages.append(value['Age'])

                if value['Gender'] == 'Man':
                    men.append(value['Age'])
                    men_ages.append(value['Age'])

        line = []
        line.append(str(index) + '-' + str(index + 20))
        line.append(len(women + men) / len(ages) * 100)
        line.append(len(women) / len(women + men) * 100)
        line.append(len(men) / len(women + men) * 100)
        output.append(line)

    output.append(['Average age', sum(ages) / len(ages)])
    output.append(['Average age for women', sum(women_ages) / len(women_ages)])
    output.append(['Average age for men', sum(men_ages) / len(men_ages)])
    save_csv(output, directory, 'age_gender_distribution')