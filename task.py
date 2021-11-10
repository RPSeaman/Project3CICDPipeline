from datetime import datetime
class Task:
    def __init__(self,title = "Untitled",tags = [],priority="",status=""):
        dateObj = datetime.now()
        self.title = title
        self.date = dateObj.strftime("%m/%d/%y %H:%M")
        self.tags = tags
        self.priority = priority
        self.status = status
    
    def getTitle(self):
        return self.title
    
    def getDate(self):
        return self.date

    def getTags(self):
        return self.tags
    
    def addTag(self,tag):
        self.tags.append(tag)
        
    def getPriority(self):
        
        return self.priority
    
    def getStatus(self):
        return self.status
    
    def tagsToString(self):
        toReturn = ""
        for i in range(len(self.getTags())):
            toReturn+=(self.getTags()[i]+", ")
        return toReturn    
    
    def changeStatus(self,status):
        self.status = status
        
    def changePriority(self,priority):
        self.priority = priority