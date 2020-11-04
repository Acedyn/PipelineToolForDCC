import engine
import os

class NoEngine(engine.Engine):
    def open(self, path):
        query = "PowerShell.exe " + "\"" + 'start ' + "\'" + path + "\'" + "\""
        print(query)
        os.system(query)
        
    def export(self, path, namespaceString):
        namespaces = namespaceString.split(" ")
        for namespace in namespaces :
            print("Exporting " + namespace)
        print("Alembic export from standalone not supported yet")
 
