import ProjectOverviewJSON


if __name__ == "__main__":
    
    obj1 = ProjectOverviewJSON.ProjectOverviewJSON()
    temp = obj1.getIndexedJSON(0,0)
    obj1.editJSONFile(temp, 'title', 'THis should work in theory')
    obj1.addToJSONFile(0,"This is the Title for the addtoJSON method", "","","")
    obj1.saveJSONFile()
