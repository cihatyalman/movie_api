class Movie:
    def __init__(self,name="",link="",imdb=1.0,image="",language_index=1,subject="",year=1000,category_indexes="",id=0):
        self.name = name
        self.link = link
        self.imdb = imdb
        self.image = image
        self.language_index = language_index
        self.subject = subject
        self.year = year
        self.category_indexes = category_indexes
        self.id = id

    def toMap(self):
        map = {}
        map["id"] = self.id
        map["name"] = self.name
        map["link"] = self.link
        map["imdb"] = self.imdb
        map["image"] = self.image
        map["language_index"] = self.language_index
        map["subject"] = self.subject
        map["year"] = self.year
        map["category_indexes"] = self.category_indexes
        return map

class MovieFromObject(Movie):
    def __init__(self,movie:Movie):
        super().__init__(movie.name, movie.link, movie.imdb, movie.image, movie.language_index, 
            movie.subject, movie.year, movie.category_indexes,movie.id)
