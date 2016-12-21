import media
import fresh_tomatoes

# Instantiate movie objects for use on website.
fear_and_loathing = media.Movie("Fear and Loathing in Las Vegas",
                           "1998",
                           "An oddball journalist and his psychopathic "
                            "lawyer travel to Las Vegas for a series of "
                            "psychedelic escapades.",
                           "https://images-na.ssl-images-amazon.com/images/M/MV5BNjA2ZDY3ZjYtZmNiMC00MDU5LTgxMWEtNzk1YmI3NzdkMTU0XkEyXkFqcGdeQXVyNjQyMjcwNDM@._V1_.jpg",  # NOQA
                           "https://www.youtube.com/watch?v=8m662obIvhY")
pulp_fiction = media.Movie("Pulp Fiction",
                           "1994",
                           "The lives of two mob hit men, a boxer, a "
                           "gangster's wife, and a pair of diner bandits "
                           "intertwine in four tales of violence and "
                           "redemption.",
                           "https://images-na.ssl-images-amazon.com/images/M/MV5BMTkxMTA5OTAzMl5BMl5BanBnXkFtZTgwNjA5MDc3NjE@._V1_SY1000_CR0,0,673,1000_AL_.jpg",  # NOQA
                           "https://www.youtube.com/watch?v=s7EdQ4FqbhY")
deadpool = media.Movie("Deadpool",
                           "2016",
                           "A fast-talking mercenary with a morbid sense of "
                           "humor is subjected to a rogue experiment that "
                           "leaves him with accelerated healing powers and "
                           "a quest for revenge.",
                           "https://images-na.ssl-images-amazon.com/images/M/MV5BMjQyODg5Njc4N15BMl5BanBnXkFtZTgwMzExMjE3NzE@._V1_SY1000_SX686_AL_.jpg",  # NOQA
                           "https://www.youtube.com/watch?v=oCvLUxICxEI")
die_hard = media.Movie("Die Hard",
                           "1988",
                           "John McClane, officer of the NYPD, tries to save "
                           "his wife Holly Gennaro and several others that "
                           "were taken hostage by German terrorist "
                           "Hans Gruber during a Christmas party at the "
                           "Nakatomi Plaza in Los Angeles.",
                           "https://images-na.ssl-images-amazon.com/images/M/MV5BMzNmY2IwYzAtNDQ1NC00MmI4LThkOTgtZmVhYmExOTVhMWRkXkEyXkFqcGdeQXVyMTk5NDA3Nw@@._V1_.jpg",  # NOQA
                           "https://www.youtube.com/watch?v=2TQ-pOvI6Xo")
back_to_the_future = media.Movie("Back to the Future",
                                 "1985",
                                 "Marty McFly, a 17-year-old high school "
                                 "student, is accidentally sent 30 years "
                                 "into the past in a time-traveling DeLorean "
                                 "invented by his close friend, the maverick "
                                 "scientist Doc Brown.",
                                 "https://images-na.ssl-images-amazon.com/images/M/MV5BZmU0M2Y1OGUtZjIxNi00ZjBkLTg1MjgtOWIyNThiZWIwYjRiXkEyXkFqcGdeQXVyMTQxNzMzNDI@._V1_SY1000_CR0,0,643,1000_AL_.jpg",  # NOQA
                                 "https://www.youtube.com/watch?v=qvsgGtivCgs")
dark_kight = media.Movie("The Dark Knight",
                         "2008",
                         "When the menace known as the Joker wreaks havoc and "
                         "chaos on the people of Gotham, the caped crusader "
                         "must come to terms with one of the greatest "
                         "psychological tests of his ability to fight "
                         "injustice.",
                         "https://images-na.ssl-images-amazon.com/images/M/MV5BMTMxNTMwODM0NF5BMl5BanBnXkFtZTcwODAyMTk2Mw@@._V1_SY1000_CR0,0,675,1000_AL_.jpg",  # NOQA
                         "https://www.youtube.com/watch?v=_PZpmTj1Q8Q")

# Populate movie list with Movie objects.
movies = [fear_and_loathing,pulp_fiction,deadpool,die_hard,
          back_to_the_future,dark_kight]

# Send the list of objects to the open_movies_page method
# This generates and opens the fresh_tomatoes website
fresh_tomatoes.open_movies_page(movies)
