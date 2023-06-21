import json
import os

class ProjectOverviewJSON:

    jsonFile = []

    def __init__(self):
        self.loadJSONFile()


    def loadJSONFile(self):

        path = r"JsonFilesOverview"
        #print('Folder', os.path.basename(os.getcwd()))
        if(os.path.basename(os.getcwd()) == r"JsonFilesData"):
            os.chdir("..")

        if(os.path.basename(os.getcwd()) != path):
            os.chdir(path)
        
        for file in os.listdir():
            if (file.endswith('.json')):

                with open(os.path.abspath(file)) as f:
                    file_contents = json.load(f)

                    self.jsonFile.append(file_contents)

    def saveJSONFile(self):

        path = r"JsonFilesOverview"
        os.chdir("..")
        os.chdir(path)

        index = 0
        for file in os.listdir():
            if (file.endswith('.json')):

                with open(os.path.abspath(file), 'w') as outfile:
                    json.dump(self.jsonFile[index], outfile)
                index += 1

    def getIndexedJSON(self, index1, index2):
        return self.jsonFile[index1][index2]
    
    def editJSONFile(self, JSON, switch, content):

        match switch:
            case "title":
                JSON.update({'title': content})
                pass
            case "details":
                JSON.update({'details': content})
                pass
            case "imagesrc":
                JSON.update({'imagesrc': content})
                pass
            case "link":
                JSON.update({'link': content})
                pass
            case "id":
                JSON.update({'id': content})
                pass
            case _:
                print("The switch cannont be found")

        pass

    def addToJSONFile(self,JSONIndex, title, details, imagesrc, link):

        id = len(self.jsonFile[JSONIndex]) + 1
        
        self.jsonFile[JSONIndex].append({'title':title, 'details':details, 'imagesrc':imagesrc, 'link':link, 'id': id})
        
        pass
