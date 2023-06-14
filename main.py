# OS path designation needs a better implementation

import ProjectOverviewJSON
import ProjectDataJSON


if __name__ == "__main__":
    
    obj1 = ProjectOverviewJSON.ProjectOverviewJSON()
    obj2 = ProjectDataJSON.ProjectDataJSON()

    obj1.addToJSONFile(1, "Test", "details", "imagesrc", "/IndividualProject")
    obj1.saveJSONFile()

    obj2.addToJSONFile("Test", "subtitle", "Overview", "Objective", [{
            "Trail Storage": "To store trail information the data structure I chose was a TreeSet. Using a tree-based structure is perfect for storing information that needs to be searched and filtered. Using trees you can sort and store information. This is great because if you need to search for that information you don't have to iterate over all the data. Treeset was used since the treeset implements Collections, so searching the tree using streams was possible.",
            "img":"./personal-website-react/images/Trail Recorder/trailoverview.JPG"
        }], "Conclusion", "mainimgsrc", "githublink")
#    temp = obj1.getIndexedJSON(0,0)
#    obj1.editJSONFile(temp, 'title', 'This should work in theory part 2')
#    obj1.addToJSONFile(0,"This is the Title for the addtoJSON method", "","","")

    obj2.saveJSONFile()
