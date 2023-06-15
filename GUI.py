import tkinter as tk
from tkinter import messagebox
import ProjectOverviewJSON


class GUI:
    
    

    def __init__(self):

        #init ProjectOverview JSON
        self.obj1 = ProjectOverviewJSON.ProjectOverviewJSON()


        self.root = tk.Tk()

        self.root.title("Python JSON Editor For Personal Website")
        self.root.geometry('1080x720')

        self.Label = tk.Label(self.root, text="Project Overview Edit", font=("", 20))
        self.Label.pack(pady=50)

        #Spinner

        self.Spinner1 = tk.Spinbox(self.root)
        self.Spinner1.pack(pady=10)
        self.Spinner2 = tk.Spinbox(self.root)
        self.Spinner2.pack(pady=10)

        #Load Button
        self.Button_LoadJSON = tk.Button(self.root, text="Load JSON", command=self._LoadJSONINFO)
        self.Button_LoadJSON.pack(padx=10, pady=10)

        # Frames
        self.frame = tk.Frame(self.root)
        self.frame.columnconfigure(0, weight=1)
        self.frame.columnconfigure(1, weight=1)

        # Labels
        self.Label_Title = tk.Label(self.frame, text="Title")
        self.Label_Title.grid(row=0, column=0)

        self.Label_Details = tk.Label(self.frame, text="Details")
        self.Label_Details.grid(row=1, column=0)

        self.Label_Image = tk.Label(self.frame, text="Image Source")
        self.Label_Image.grid(row=2, column=0)

        self.Label_Link = tk.Label(self.frame, text="Link")
        self.Label_Link.grid(row=3, column=0)

        # Text Boxes
        self.Textbox_Title = tk.Text(self.frame,  height=1)
        self.Textbox_Title.grid(row=0, column=1, pady=10)

        self.Textbox_Details = tk.Text(self.frame, height=5)
        self.Textbox_Details.grid(row=1, column=1, pady=10)

        self.Textbox_Image = tk.Text(self.frame, height=1)
        self.Textbox_Image.grid(row=2, column=1, pady=10)

        self.Textbox_Link = tk.Text(self.frame, height=1)
        self.Textbox_Link.grid(row=3, column=1, pady=10)

        self.frame.pack(padx=20, pady=20)

        self.button = tk.Button(self.root, text="Update", command=self._updateJSONInfo)
        self.button.pack(padx=10, pady=10)
        self.button = tk.Button(self.root, text="Create", command=self._CreateJSONInfo)
        self.button.pack(padx=10, pady=10)
        self.button = tk.Button(self.root, text="Clear", command=self._ClearTextBoxes)
        self.button.pack(padx=10, pady=10)

        self.root.mainloop()

    def _LoadJSONINFO(self):
        
        tempDict = self.obj1.getIndexedJSON(int(self.Spinner1.get()), int(self.Spinner2.get()))
        
        self._ClearTextBoxes()

        self.Textbox_Title.insert(tk.INSERT, tempDict.get('title'))
       
        self.Textbox_Details.insert(tk.INSERT, tempDict.get('details'))
       
        self.Textbox_Image.insert(tk.INSERT, tempDict.get('imagesrc'))
        
        self.Textbox_Link.insert(tk.INSERT, tempDict.get('link')) 
        
    def _updateJSONInfo(self):

        tempDict = self.obj1.getIndexedJSON(int(self.Spinner1.get()), int(self.Spinner2.get()))

        self.obj1.editJSONFile(tempDict, 'title', self.Textbox_Title.get('1.0', 'end-1c'))
        self.obj1.editJSONFile(tempDict, 'details', self.Textbox_Details.get('1.0', 'end-1c'))
        self.obj1.editJSONFile(tempDict, 'imagesrc', self.Textbox_Image.get('1.0', 'end-1c'))
        self.obj1.editJSONFile(tempDict, 'link', self.Textbox_Link.get('1.0', 'end-1c'))

        self.obj1.saveJSONFile()
        res = messagebox.showinfo(title="Create", message="File has been successfully updated")

        if res == 'ok':
            self._ClearTextBoxes()
        

    def _CreateJSONInfo(self):
       
        self.obj1.addToJSONFile(int(self.Spinner1.get()),
                                self.Textbox_Title.get('1.0', 'end-1c'),
                                self.Textbox_Details.get('1.0', 'end-1c'),
                                self.Textbox_Image.get('1.0', 'end-1c'),
                                self.Textbox_Link.get('1.0', 'end-1c'))
        
        self.obj1.saveJSONFile()

        res = messagebox.showinfo(title="Create", message="New File has been sucessfully Created")
        
        if res == 'ok':
            self._ClearTextBoxes()

    def _ClearTextBoxes(self):
        self.Textbox_Title.delete('1.0', 'end')
        self.Textbox_Details.delete('1.0', 'end')
        self.Textbox_Image.delete('1.0', 'end')
        self.Textbox_Link.delete('1.0', 'end')