class News:
    def __init__(self,source,link,country,id,description):
        self.source = source
        self.link = link
        self.country = country
        self.id = id
        self.description = description


class Articles:
    def __init__(self,author,title,description,url,poster,time):
        self.author = author
        self.title = title
        self.description = description
        self.url = url
        self.poster = poster
        self.time = time 