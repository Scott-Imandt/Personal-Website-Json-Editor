import tkinter as tk
from tkinter import messagebox
import ProjectOverviewJSON
import ProjectDataJSON


class GUI:

    def __init__(self):

        # init ProjectOverview JSON
        self.obj1 = ProjectOverviewJSON.ProjectOverviewJSON()
        self.obj2 = ProjectDataJSON.ProjectDataJSON()

        self.root = tk.Tk()

        self.root.title("Python JSON Editor For Personal Website")
        self.root.geometry('1080x1080')

        # variables
        self.page1Var = False
        self.page2Var = False

        self.window1()

        self.root.mainloop()

    def _LoadJSONOVERVIEW(self):

        if (self.page1Var == False):
            pass

        tempDict = self.obj1.getIndexedJSON(
            int(self.Spinner1.get()), int(self.Spinner2.get()))

        self._ClearTextBoxes()

        self.Textbox_Title.insert(tk.INSERT, tempDict.get('title'))

        self.Textbox_Details.insert(tk.INSERT, tempDict.get('details'))

        self.Textbox_Image.insert(tk.INSERT, tempDict.get('imagesrc'))

        self.Textbox_Link.insert(tk.INSERT, tempDict.get('link'))

    def _LoadJSONPROJECT(self):

        if (self.page2Var == False):
            pass

        tempDict = self.obj2.getIndexedJSON(
            int(self.Spinner1_Project.get()))

        self._ClearTextBoxes_Project()

        self.Textbox_Title_Project.insert(tk.INSERT, tempDict.get('title'))
        self.Textbox_Subtitle_Project.insert(
            tk.INSERT, tempDict.get('subtitle'))
        self.Textbox_Overview_Project.insert(
            tk.INSERT, tempDict.get('Overview'))
        self.Textbox_Objective_Project.insert(
            tk.INSERT, tempDict.get('Objective'))
        self.Textbox_Conclusion_Project.insert(
            tk.INSERT, tempDict.get('Conclusion'))
        self.Textbox_Mainimgsrc_Project.insert(
            tk.INSERT, tempDict.get('mainimgsrc'))
        self.Textbox_Githublink_Project.insert(
            tk.INSERT, tempDict.get('githublink'))

 #       print(tempDict.get('Array'))

  #      for x in tempDict.get('Array'):
  #          print(x.get)

    def _updateJSONOVERVIEW(self):

        if (self.page1Var == False):
            pass

        tempDict = self.obj1.getIndexedJSON(
            int(self.Spinner1.get()), int(self.Spinner2.get()))

        self.obj1.editJSONFile(
            tempDict, 'title', self.Textbox_Title.get('1.0', 'end-1c'))
        self.obj1.editJSONFile(tempDict, 'details',
                               self.Textbox_Details.get('1.0', 'end-1c'))
        self.obj1.editJSONFile(tempDict, 'imagesrc',
                               self.Textbox_Image.get('1.0', 'end-1c'))
        self.obj1.editJSONFile(
            tempDict, 'link', self.Textbox_Link.get('1.0', 'end-1c'))

        self.obj1.saveJSONFile()
        res = messagebox.showinfo(
            title="Create", message="File has been successfully updated")

        if res == 'ok':
            self._ClearTextBoxes()

    def _UpdateJSONPROJECT(self):
        if (self.page2Var == False):
            pass

        tempDict = self.obj2.getIndexedJSON(
            int(self.Spinner1_Project.get()))

        self.obj2.editJSONFile(
            tempDict, 'title', self.Textbox_Title_Project.get('1.0', 'end-1c'))

        self.obj2.editJSONFile(
            tempDict, 'subtitle', self.Textbox_Subtitle_Project.get('1.0', 'end-1c'))

        self.obj2.editJSONFile(
            tempDict, 'Overview', self.Textbox_Overview_Project.get('1.0', 'end-1c'))

        self.obj2.editJSONFile(
            tempDict, 'Objective', self.Textbox_Objective_Project.get('1.0', 'end-1c'))

        self.obj2.editJSONFile(
            tempDict, 'Conclusion', self.Textbox_Conclusion_Project.get('1.0', 'end-1c'))

        self.obj2.editJSONFile(
            tempDict, 'githublink', self.Textbox_Githublink_Project.get('1.0', 'end-1c'))

        self.obj2.editJSONFile(
            tempDict, 'mainimgsrc', self.Textbox_Mainimgsrc_Project.get('1.0', 'end-1c'))

        self.obj2.saveJSONFile()
        res = messagebox.showinfo(
            title="Create", message="File has been successfully updated")

        if res == 'ok':
            self._ClearTextBoxes_Project()

    def _CreateJSONOVERVIEW(self):

        if (self.page1Var == False):
            pass

        self.obj1.addToJSONFile(int(self.Spinner1.get()),
                                self.Textbox_Title.get('1.0', 'end-1c'),
                                self.Textbox_Details.get('1.0', 'end-1c'),
                                self.Textbox_Image.get('1.0', 'end-1c'),
                                self.Textbox_Link.get('1.0', 'end-1c'))

        self.obj1.saveJSONFile()

        res = messagebox.showinfo(
            title="Create", message="New File has been sucessfully Created")

        if res == 'ok':
            self._ClearTextBoxes()

    def _CreateJSONPROJECT(self):

        if (self.page2Var == False):
            pass

        self.obj2.addToJSONFile(
            self.Textbox_Title_Project.get('1.0', 'end-1c'),
            self.Textbox_Subtitle_Project.get('1.0', 'end-1c'),
            self.Textbox_Overview_Project.get('1.0', 'end-1c'),
            self.Textbox_Objective_Project.get('1.0', 'end-1c'),
            [],
            self.Textbox_Conclusion_Project.get('1.0', 'end-1c'),
            self.Textbox_Mainimgsrc_Project.get('1.0', 'end-1c'),
            self.Textbox_Githublink_Project.get('1.0', 'end-1c'),
        )

        self.obj2.saveJSONFile()

        res = messagebox.showinfo(
            title="Create", message="New File has been sucessfully Created")

        if res == 'ok':
            self._ClearTextBoxes_Project()

    def _ClearTextBoxes(self):

        if (self.page1Var == False):
            pass

        self.Textbox_Title.delete('1.0', 'end')
        self.Textbox_Details.delete('1.0', 'end')
        self.Textbox_Image.delete('1.0', 'end')
        self.Textbox_Link.delete('1.0', 'end')

    def _ClearTextBoxes_Project(self):

        if (self.page2Var == False):
            pass

        self.Textbox_Title_Project.delete('1.0', 'end')
        self.Textbox_Subtitle_Project.delete('1.0', 'end')
        self.Textbox_Overview_Project.delete('1.0', 'end')
        self.Textbox_Objective_Project.delete('1.0', 'end')
        self.Textbox_Conclusion_Project.delete('1.0', 'end')
        self.Textbox_Mainimgsrc_Project.delete('1.0', 'end')
        self.Textbox_Githublink_Project.delete('1.0', 'end')

    def window1(self):

        self.page1Var = True

        if (self.page2Var == True and self.page2 != None ):
            self.page2Var = False
            self.page2.destroy()

        self.obj1.loadJSONFile()

        # Frames
        self.page1 = tk.Frame(self.root)
        self.page1grid = tk.Frame(self.page1)
        self.page1grid.columnconfigure(0, weight=1)
        self.page1grid.columnconfigure(1, weight=1)

        self.Label = tk.Label(
            self.page1, text="Project Overview Edit", font=("", 20))
        self.Label.pack(pady=50)

        # Switch Button
        self.Button_SwitchWindow = tk.Button(
            self.page1, text="Switch", command=self.window2)
        self.Button_SwitchWindow.pack(padx=10, pady=10)

        # Spinner
        self.Spinner1 = tk.Spinbox(self.page1)
        self.Spinner1.pack(pady=10)
        self.Spinner2 = tk.Spinbox(self.page1)
        self.Spinner2.pack(pady=10)

        # Load Button
        self.Button_LoadJSON = tk.Button(
            self.page1, text="Load JSON", command=self._LoadJSONOVERVIEW)
        self.Button_LoadJSON.pack(padx=10, pady=10)

        # Labels
        self.Label_Title = tk.Label(self.page1grid, text="Title")
        self.Label_Title.grid(row=0, column=0)

        self.Label_Details = tk.Label(self.page1grid, text="Details")
        self.Label_Details.grid(row=1, column=0)

        self.Label_Image = tk.Label(self.page1grid, text="Image Source")
        self.Label_Image.grid(row=2, column=0)

        self.Label_Link = tk.Label(self.page1grid, text="Link")
        self.Label_Link.grid(row=3, column=0)

        self.page1grid.pack()

        # Text Boxes
        self.Textbox_Title = tk.Text(self.page1grid,  height=1)
        self.Textbox_Title.grid(row=0, column=1, pady=10)

        self.Textbox_Details = tk.Text(self.page1grid, height=5)
        self.Textbox_Details.grid(row=1, column=1, pady=10)

        self.Textbox_Image = tk.Text(self.page1grid, height=1)
        self.Textbox_Image.grid(row=2, column=1, pady=10)

        self.Textbox_Link = tk.Text(self.page1grid, height=1)
        self.Textbox_Link.grid(row=3, column=1, pady=10)

        # Function Buttons
        self.button = tk.Button(self.page1, text="Update",
                                command=self._updateJSONOVERVIEW)
        self.button.pack(padx=10, pady=10, side='top', fill='x')
        self.button = tk.Button(self.page1, text="Create",
                                command=self._CreateJSONOVERVIEW)
        self.button.pack(padx=10, pady=10, side='top', fill='x')
        self.button = tk.Button(self.page1, text="Clear",
                                command=self._ClearTextBoxes)
        self.button.pack(padx=10, pady=10, side='top', fill='x')

        self.page1.pack(padx=20, pady=20)

        pass

    def window2(self):

        self.page2Var = True

        if (self.page1Var == True and self.page1 != None ):
            self.page1Var = False
            self.page1.destroy()

        self.obj2.loadJSONFile()

        # Frames
        self.page2 = tk.Frame(self.root)
        self.page2grid = tk.Frame(self.page2)
        self.page2grid.columnconfigure(0, weight=1)
        self.page2grid.columnconfigure(1, weight=1)

        self.page2gridArray = tk.Frame(self.page2)
        self.page2gridArray.columnconfigure(0, weight=1)
        self.page2gridArray.columnconfigure(1, weight=1)

        self.Label = tk.Label(
            self.page2, text="Project Specific Edit", font=("", 20))
        self.Label.pack(pady=50)

         # Switch Button
        self.Button_SwitchWindow = tk.Button(
            self.page2, text="Switch", command=self.window1)
        self.Button_SwitchWindow.pack(padx=10, pady=10)

        # Spinner
        self.Spinner1_Project = tk.Spinbox(self.page2)
        self.Spinner1_Project.pack(pady=10)

        # Load Button
        self.Button_LoadJSON_Project = tk.Button(
            self.page2, text="Load JSON", command=self._LoadJSONPROJECT)
        self.Button_LoadJSON_Project.pack(padx=10, pady=10)

        # Labels
        self.Label_Title_Project = tk.Label(self.page2grid, text="Title")
        self.Label_Title_Project.grid(row=0, column=0)

        self.Label_Subtitle_Project = tk.Label(self.page2grid, text="Subtitle")
        self.Label_Subtitle_Project.grid(row=1, column=0)

        self.Label_Overview_Project = tk.Label(self.page2grid, text="Overview")
        self.Label_Overview_Project.grid(row=2, column=0)

        self.Label_Objective_Project = tk.Label(
            self.page2grid, text="Objective")
        self.Label_Objective_Project.grid(row=3, column=0)

        # Array needed

        self.Label_Conclusion_Project = tk.Label(
            self.page2grid, text="Conslusion")
        self.Label_Conclusion_Project.grid(row=4, column=0)

        self.Label_Mainimgsrc_Project = tk.Label(
            self.page2grid, text="Main Image Src")
        self.Label_Mainimgsrc_Project.grid(row=5, column=0)

        self.Label_Githublink_Project = tk.Label(
            self.page2grid, text="Github Link")
        self.Label_Githublink_Project.grid(row=6, column=0)

        self.Textbox_Title_Project = tk.Text(self.page2grid,  height=1)
        self.Textbox_Title_Project.grid(row=0, column=1, pady=10)

        self.Textbox_Subtitle_Project = tk.Text(self.page2grid, height=5)
        self.Textbox_Subtitle_Project.grid(row=1, column=1, pady=10)

        self.Textbox_Overview_Project = tk.Text(self.page2grid, height=5)
        self.Textbox_Overview_Project.grid(row=2, column=1, pady=10)

        self.Textbox_Objective_Project = tk.Text(self.page2grid, height=5)
        self.Textbox_Objective_Project.grid(row=3, column=1, pady=10)

        # Array needed

        self.Textbox_Conclusion_Project = tk.Text(self.page2grid, height=5)
        self.Textbox_Conclusion_Project.grid(row=4, column=1, pady=10)

        self.Textbox_Mainimgsrc_Project = tk.Text(self.page2grid, height=1)
        self.Textbox_Mainimgsrc_Project.grid(row=5, column=1, pady=10)

        self.Textbox_Githublink_Project = tk.Text(self.page2grid, height=1)
        self.Textbox_Githublink_Project.grid(row=6, column=1, pady=10)

        self.page2grid.pack()

        # Function Buttons
        self.button = tk.Button(self.page2, text="Update",
                                command=self._UpdateJSONPROJECT)
        self.button.pack(padx=10, pady=10, side='top', fill='x')
        self.button = tk.Button(self.page2, text="Create",
                                command=self._CreateJSONPROJECT)
        self.button.pack(padx=10, pady=10, side='top', fill='x')
        self.button = tk.Button(self.page2, text="Clear",
                                command=self._ClearTextBoxes_Project)
        self.button.pack(padx=10, pady=10, side='top', fill='x')

        self.page2.pack(padx=20, pady=20)
