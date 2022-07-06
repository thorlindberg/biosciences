def save_csv(output, directory, filename):
    
    '''
    Appends the given output to the given filename in the given directory.

    Parameters:
    output (list): A list comprised of lists, where each list represents a line.
    directory (string): A full path to the destination folder.
    filename (string): A name for the file being saved to, excluding file format.
    '''

    for line in output:
        open(directory + filename + '.csv', 'a').write(','.join(line) + '\n')

    print('Output saved to', filename + '.csv', 'in', directory)