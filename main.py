print('Please specify the path to the folder containing the database file.')
print('Example of a folder path: /User/Desktop/Folder/')

while True:
  try:
    directory = input('Input: ') 
    database = read_file(directory, 'data.db')
    break
  except:
    print('You have entered an invalid file path. Please try again.')

count_people(directory, database)
count_parents(directory, database)
count_children(directory, database)
parents_with_multiple_partners(directory, database)
count_grandparents(directory, database)
average_cousins(directory, database)
first_time_father(directory, database)
first_time_mother(directory, database)
age_gender_distribution(directory, database)
family_patterns(directory, database)
height_correlation(directory, database)
weight_correlation(directory, database)
tall_parents(directory, database)
overweight_parents(directory, database)
blood_to_children(directory, database)
blood_to_grandparents(directory, database)
eye_color_heritage(directory, database)
height_evolution(directory, database)
weight_evolution(directory, database)