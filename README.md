# Fresh Tomatoes
#### Deliciously Entertainting Movies

![Fresh Tomatoes](ft_banner.png "Fresh Tomatoes")


Forked from [ud036_StarterCode](https://github.com/udacity/ud036_StarterCode "Fresh Tomatoes Starter Code")


## Installation

First, you will need to clone the repo locally.

```sh
$ git clone https://github.com/drownedout/ud036_StarterCode.git
```

## Usage

Once you have successfully cloned the project, you can add any movie you want to your site by opening ```entertainment_center.py```

As you can see, there are six movies already there but you can remove them and add your own!

```python
your_movie_title = Movie(title, storyline, poster_image_url, trailer_youtube_url)
```

After constructing your movie instance, just simply add it to the movies array and pass the array into the open_movies_page method.

```python
movies = [your_movie_title]

fresh_tomatoes.open_movies_page(movies)
```