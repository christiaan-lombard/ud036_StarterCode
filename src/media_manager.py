from media import Movie

class MediaManager():
    # def __init__(self):

    def list_favourite_movies(self):
        movies = []
        movies.append(
            Movie(
                "Watchmen",
                '''In a gritty and alternate 1985 the glory days of costumed 
                vigilantes have been brought to a close by a government crackdown,
                but after one of the masked veterans is brutally murdered, 
                an investigation into the killer is initiated. The reunited 
                heroes set out to prevent their own destruction, 
                but in doing so uncover a sinister plot that puts 
                all of humanity in grave danger.''',
                "http://image.tmdb.org/t/p/w300/1QqwJBv5a6ddgzaT6cLytJioyrJ.jpg", 
                "2009-03-05",
                "https://www.youtube.com/watch?v=PVgUZ2NSzBo"
            )
        )
        movies.append(
            Movie(
                "Howl's Moving Castle",
                '''When Sophie, a shy young woman, is cursed with an old body by 
                a spiteful witch, her only chance of breaking the spell lies with 
                a self-indulgent yet insecure young wizard and his companions in 
                his legged, walking home.''',
                "http://image.tmdb.org/t/p/w300/iMarB2ior30OAXjPa7QIdeyUfM1.jpg", 
                "2004-11-19",
                "https://www.youtube.com/watch?v=bHTrnAVPens"
            )
        )
        movies.append(
            Movie(
                "Grandma's Boy",
                '''Even though he's 35, Alex acts more like he's 13, spending 
                his days as the world's oldest video game tester and his 
                evenings developing the next big Xbox game. But he gets 
                kicked out of his apartment and is forced to move in 
                with his grandmother.''',
                "http://image.tmdb.org/t/p/w300/9Z0Q9uIH4il75dfPVqFhVKljfY.jpg", 
                "2006-01-06",
                "https://www.youtube.com/watch?v=sEA_g1UK64k"
            )
        )
        return movies
