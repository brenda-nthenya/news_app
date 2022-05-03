class Article:
    '''Instantiates object of the news article objects'''

    def __init__(self, author,title,description,time, url,image):
        self.author = author
        self.title = title
        self.description = description
        self.time = time
        self.url = url
        self.image = image


class Category:

    def __init__(self, author,title,description,time, url,image):
        self.author = author
        self.title = title
        self.description = description
        self.time = time
        self.url = url
        self.image = image

class Headlines:

    def __init__(self, author,title,description,time, url,image):
        self.author = author
        self.title = title
        self.description = description
        self.time = time
        self.url = url
        self.image = image

class Source:
    '''Source class'''

    def __init__(self,id,name,description,url):
        self.id = id
        self.name = name
        self.description = description
        self.url = url