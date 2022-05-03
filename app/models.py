class Article:
    '''Instantiates object of the news article objects'''

    def __init__(self, author,title,description,time, url,image):
        self.author = author
        self.title = title
        self.description = description
        self.time = time
        self.url = url
        self.image = image