filename = 'my_first_file,txt'

file = open(filename,mode='a')

movies = ['Scream', 'IT', 'The nun', 'Anabelle', 'Jason']

for movie in  movies:
    file.write(movie)
    file.write('\n')
