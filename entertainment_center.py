from media import Movie
from fresh_tomatoes import open_movies_page

# Creating six movie instances
titanic_two = Movie(
    'Titanic Two',
    'On the 100th anniversary of the original'
    ' voyage, a modern luxury liner christened "Titanic 2,"'
    ' follows the path of its namesake. But when a tsunami'
    ' hurls an ice berg into the new ship\'s path, the'
    ' passengers and crew must fight to avoid a similar fate.',
    'https://images-na.ssl-images-amazon.com/images/M/MV5BMTMxMjQ1MjA5Ml5BMl5BanBnXkFtZTcwNjIzNjg1Mw@@._V1_.jpg',
    'https://www.youtube.com/watch?v=UT44DYhGOnM')

howard_the_duck = Movie(
    'Howard The Duck',
    'A sarcastic humanoid duck is pulled'
    ' from his homeworld to Earth where he must stop a hellish'
    ' alien invasion with the help of a nerdy scientist'
    ' and a cute struggling female rock singer who fancies him.',
    'https://s-media-cache-ak0.pinimg.com/originals/c5/a5/f4/c5a5f49b3cc72855d55c565c8539b6d5.jpg',
    'https://www.youtube.com/watch?v=SzI-ZbcK_sw')

batman_and_robin = Movie(
    'Batman & Robin',
    'Batman and Robin try to keep their'
    ' relationship together even as they must stop Mr. Freeze'
    ' and Poison Ivy from freezing Gotham City.',
    'https://images-na.ssl-images-amazon.com/images/M/MV5BMGQ5YTM1NmMtYmIxYy00N2VmLWJhZTYtN2EwYTY3MWFhOTczXkEyXkFqcGdeQXVyNTA2NTI0MTY@._V1_UX182_CR0,0,182,268_AL_.jpg',
    'https://www.youtube.com/watch?v=4RBXypX4qWI')

glitter = Movie(
    'Glitter',
    'A young singer dates a disc jockey who helps her'
    ' get into the music business, but their relationship become'
    ' complicated as she ascends to super stardom.',
    'https://images-na.ssl-images-amazon.com/images/M/MV5BMGJkN2IxNTYtZDE1OS00MWJhLWFhNzItNTZkMjM4OGUzMTE2L2ltYWdlXkEyXkFqcGdeQXVyNTg3MTc4ODY@._V1_UX182_CR0,0,182,268_AL_.jpg',
    'https://www.youtube.com/watch?v=QaKxGrajnzY')

the_room = Movie(
    'The Room',
    'Johnny is a successful banker who lives happily'
    ' in a San Francisco townhouse with his fiancée, Lisa. One day,'
    ' inexplicably, she gets bored with him and decides to seduce his'
    ' best friend, Mark. From there, nothing will be the same again.',
    'https://images-na.ssl-images-amazon.com/images/M/MV5BMTg4MTU1MzgwOV5BMl5BanBnXkFtZTcwNjM1MTAwMQ@@._V1_UY268_CR12,0,182,268_AL_.jpg',
    'https://www.youtube.com/watch?v=9-dIdFXeFhs')

jack_and_jill = Movie(
    'Jack and Jill',
    'Family guy Jack Sadelstein prepares'
    ' for the annual event he dreads: the Thanksgiving visit'
    ' of his twin sister, the needy and passive-aggressive Jill,'
    ' who then refuses to leave.',
    'https://images-na.ssl-images-amazon.com/images/M/MV5BNjczMTU5OTUyMl5BMl5BanBnXkFtZTcwODEzNjc3Ng@@._V1_UX182_CR0,0,182,268_AL_.jpg',
    'https://www.youtube.com/watch?v=oJVv3PBoPMc')

# Add movie instances to an array
movies = [titanic_two, howard_the_duck, batman_and_robin,
          glitter, the_room, jack_and_jill]

# Call open_movies_page method from fresh_tomatoes.py passing in the movies array
open_movies_page(movies)
