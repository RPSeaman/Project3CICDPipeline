from datetime import datetime
class Task:
    def __init__(self,title = "Untitled",tags = []):
        dateObj = datetime.now()
        self.title = title
        self.date = dateObj.strftime("%m/%d/%y %H:%M %Z")
        self.tags = tags
    
    def getTitle(self):
        return self.title
    
    def getDate(self):
        return self.date

    def getTags(self):
        return self.tags
    
    def addTag(self,tag):
        self.tags.append(tag)
        
    def tagsToString(self):
        toReturn = ""
        for i in range(len(self.getTags())):
            toReturn+=(self.getTags()[i]+", ")
        return toReturn


