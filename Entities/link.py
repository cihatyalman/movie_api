class Link:
    def __init__(self,name="",link="",id=0):
        self.name = name
        self.link = link
        self.id = id

    def toMap(self):
        map = {}
        map["id"] = self.id
        map["name"] = self.name
        map["link"] = self.link
        return map

class LinkFromObject(Link):
    def __init__(self, link:Link):
        super().__init__(link.name, link.link, link.id)
