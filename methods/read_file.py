def read_file(directory, filename):
    
    '''
    Reads the given filename in the given directory line-by-line, adding the data
    from each line to a dictionary, if the line contains the correct descriptive
    string for the respective type of data.

    Parameters:
    directory (string): A full path to the folder containing the file.
    filename (string): A name for the file being read, including file format.

    Returns:
    dictionary: A dictionary of people with CPR numbers as keys, and dictionaries
    of attributes as values.
    '''

    people = {}
    person = {}
    CPR = ''

    for line in open(directory + filename):

        if len(line) == 1 and CPR != '':

            person['Age'] = 2000 - (int(CPR[4:6]) + 1900)

            if int(CPR[-1]) % 2 == 0:
                person['Gender'] = 'Woman'

            if int(CPR[-1]) % 2 == 1:
                person['Gender'] = 'Man'

            people[CPR] = person
            person = {}

        if line.startswith('CPR'):
            CPR = line[line.find(':') + 2:].rstrip('\n')

        if line.startswith('First'):
            name = line[line.find(':') + 2:].rstrip('\n')

        if line.startswith('Last'):
            person['Name'] = name + ' ' + \
                line[line.find(':') + 2:].rstrip('\n')

        if line.startswith('Height'):
            person['Height'] = int(line[line.find(':') + 2:].rstrip('\n'))

        if line.startswith('Weight'):
            person['Weight'] = int(line[line.find(':') + 2:].rstrip('\n'))

        if line.startswith('Eye'):
            person['Color'] = line[line.find(':') + 2:].rstrip('\n')

        if line.startswith('Blood'):
            person['Type'] = line[line.find(':') + 2:].rstrip('\n')

        if line.startswith('Children'):
            person['Children'] = line[line.find(
                ':') + 2:].rstrip('\n').split(' ')

    return people