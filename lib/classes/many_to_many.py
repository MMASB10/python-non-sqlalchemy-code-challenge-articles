class Article:
    all = []
    
    def __init__(self, author, magazine, title):
        if hasattr(self, '_title'):
            return
        if isinstance(title, str) and 5 <= len(title) <= 50:
            self._title = title
        self._author = author
        self._magazine = magazine
        Article.all.append(self)
    
    @property
    def title(self):
        return self._title
    
    @title.setter
    def title(self, value):
        pass
    
    @property
    def author(self):
        return self._author
    
    @author.setter
    def author(self, value):
        self._author = value
    
    @property
    def magazine(self):
        return self._magazine
    
    @magazine.setter
    def magazine(self, value):
        self._magazine = value
        
class Author:
    def __init__(self, name):
        if hasattr(self, '_name'):
            return
        if isinstance(name, str) and len(name) > 0:
            self._name = name
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        pass

    def articles(self):
        return [a for a in Article.all if a.author == self]

    def magazines(self):
        return list(set(a.magazine for a in self.articles()))

    def add_article(self, magazine, title):
        return Article(self, magazine, title)

    def topic_areas(self):
        articles = self.articles()
        return list(set(m.category for m in self.magazines())) if articles else None

class Magazine:
    def __init__(self, name, category):
        if isinstance(name, str) and 2 <= len(name) <= 16:
            self._name = name
        if isinstance(category, str) and len(category) > 0:
            self._category = category
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        if isinstance(value, str) and 2 <= len(value) <= 16:
            self._name = value
    
    @property
    def category(self):
        return self._category
    
    @category.setter
    def category(self, value):
        if isinstance(value, str) and len(value) > 0:
            self._category = value

    def articles(self):
        return [a for a in Article.all if a.magazine == self]

    def contributors(self):
        return list(set(a.author for a in self.articles()))

    def article_titles(self):
        articles = self.articles()
        return [a.title for a in articles] if articles else None

    def contributing_authors(self):
        counts = {}
        for a in self.articles():
            counts[a.author] = counts.get(a.author, 0) + 1
        authors = [author for author, count in counts.items() if count > 2]
        return authors if authors else None