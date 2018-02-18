# stores details of movies and displays them on website.
import fresh_tomatoes
import media

# Creating various instances for the class Movie.
insidious = media.Movie("Insidious",
                        "The story is about a couple and his son with ghosts.",
                        "insidious.jpg",
                        "https://www.youtube.com/watch?v=Gmpn9_D8sZ0")


annabelle = media.Movie("Annabelle",
                        "A myterious doll named annabelle having some spirit.",
                        "annabelle.jpg",
                        "https://www.youtube.com/watch?v=yd27oUBi3-I")


Now_you_see_me = media.Movie("Now you see me",
                             "American thriller film having great magicians",
                             "nowyouseeme.jpg",
                             "https://www.youtube.com/watch?v=4OtM9j2lcUA")


The_fault_in_our_stars = media.Movie(
                                "The fault in our stars",
                                "American romantic director film",
                                "fault in our stars.jpg",
                                "https://www.youtube.com/watch?v=9ItBvH5J6ss")

Hunger_games = media.Movie(
    "Hunger games",
    "American post-apocalyptic science fiction action adventurous film",
    "hunger.jpg",
    "https://www.youtube.com/watch?v=mfmrPu43DF8")
Hangover = media.Movie("Hangover",
                       "Comedy film",
                       "hangover.jpg",
                       "https://www.youtube.com/watch?v=TZc39afdeXU")

# Creating an array called movies and store the Movie objects in that list.
movies = [
            insidious, annabelle, Now_you_see_me,
            The_fault_in_our_stars, Hunger_games, Hangover]

# using the python program fresh tomatoes for opening our website.
fresh_tomatoes.open_movies_page(movies)
