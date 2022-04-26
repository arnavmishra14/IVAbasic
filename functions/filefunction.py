import os
import subprocess as sp
import shutil
class filefuction :
    def __init__(self,args):
        self.intent=args["intent"]
        self.object=args["object"]
        self.dirname=args["dirname"]
        self.to_dirname=args["to_dirname"]
        self.from_dirname=args["from_dirname"]
        self.note=args["note"]
    
    def openEntity(self):
        os.startfile(self.object)

    def UNK(self):
        pass

    def CloseEntity(self):
        try:
            os.close(self.object)
        except:
            pass
    
    def DeleteEntity(self):
        try:
            os.remove(self.object)
        except:
            pass

    def MoveEntity(self):
        shutil.move(form_dirname,to_dirname)
    
    def AddToNotes(self):
        f=open("updated.txt", "a")
        f.write("now the file has more content!")
        f.close()
        f=open("updated.txt" , "a")
        print(f.read())
        