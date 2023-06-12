import json
import os


def loadJSONFile():

    path = r"JsonFiles"
    os.chdir(path)

    for file in os.listdir():
        if (file.endswith('.json')):

            with open(os.path.abspath(file)) as f:
                file_contents = json.load(f)

                jsonFile.append(file_contents)


def saveJSONFile():

    # access can be achieved by using jsonFile[index][index]
    jsonFile[0][0].update({'title': "This re-write WORKED"})
    print(jsonFile[0][0].get('title'))

    # path = r"JsonFiles"
    # os.chdir(path)
    index = 0
    for file in os.listdir():
        if (file.endswith('.json')):

            with open(os.path.abspath(file), 'w') as outfile:
                json.dump(jsonFile[index], outfile)
            index += 1

#    'JsonFiles\ProjectOverviewDataCourse.json'


if __name__ == "__main__":
    jsonFile = []
    loadJSONFile()
    saveJSONFile()
