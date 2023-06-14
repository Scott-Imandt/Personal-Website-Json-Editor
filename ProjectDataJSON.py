import json
import os


class ProjectDataJSON:

    jsonFile = []

    def __init__(self):
        self.loadJSONFile()

    def loadJSONFile(self):

        path = r"JsonFilesData"

        os.chdir("..")
        os.chdir(path)

        for file in os.listdir():
            if (file.endswith('.json')):

                with open(os.path.abspath(file)) as f:
                    file_contents = json.load(f)

                    self.jsonFile.append(file_contents)

    def saveJSONFile(self):

        path = r"JsonFilesData"

        os.chdir("..")
        os.chdir(path)

        index = 0
        for file in os.listdir():
            if (file.endswith('.json')):

                with open(os.path.abspath(file), 'w') as outfile:
                    json.dump(self.jsonFile[index], outfile)
                index += 1

    def getIndexedJSON(self, index1):
        return self.jsonFile[index1]

    def editJSONFile(self, JSON, switch, content):

        match switch:
            case "title":
                JSON.update({'title': content})
                pass
            case "subtitle":
                JSON.update({'subtitle': content})
                pass
            case "Overview":
                JSON.update({'Overview': content})
                pass
            case "Objective":
                JSON.update({'Objective': content})
                pass
            case "Conclusion":
                JSON.update({'Conclusion': content})
                pass
            case "id":
                JSON.update({'id': content})
                pass
            case "mainimgsrc":
                JSON.update({'mainimgsrc': content})
                pass
            case "githublink":
                JSON.update({'githublink': content})
                pass
            case "Array":
                JSON.update({'Array': content})
                pass
            case _:
                print("The switch cannont be found")

        pass

    def addToJSONFile(self, title, subtitle, Overview, Objective, Array, Conclusion, mainimgsrc, githublink):

        path = r"JsonFilesData"

        os.chdir("..")
        os.chdir(path)


        # Data to be written
        Data = {
            "title": title,
            "subtitle": subtitle,
            "Overview": Overview,
            "Objective": Objective,
            "Array": Array,
            "Conclusion": Conclusion,
            "mainimgsrc": mainimgsrc,
            "githublink": githublink,
            "id": 1

        }

        self.jsonFile.append(Data)

        with open((title+"ProjectData.json"), "w") as outfile:
            json.dump(Data, outfile)
    pass
