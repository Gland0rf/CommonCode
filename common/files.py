import os

class Read:
    def readFileSeperateExtension(filePath, extension):
        '''
        Gives back the content of a specific File in the current Folder\n
        FilePath: The path of the File (without the extension)\n
        Extension: The extension of the File
        '''
        f = open(f"{filePath}.{extension}", "r")
        content = f.read()
        f.close()
        return content
    
    def readFile(filePath):
        '''
        Gives back the content of a specific File in the current Folder\n
        FilePath: The path of the File (with the extension)
        '''
        f = open(f"{filePath}", "r")
        content = f.read()
        f.close()
        return content
    
    def readAllFilesInFolder(path):
        '''
        Reads all the Files in a folder and writes their content into a list\n
        Path: The Path of the Folder with the files in it
        '''
        files = os.listdir(path)

        output = []

        for file in files:
            f = open(f"{path}/{file}", "r")
            content = f.read()
            f.close()
            output.append(content)

        return output
    
class Write:
    def createAndWriteFile(pathAndName, content):
        '''
        Creates a file and writes into it\n
        PathAndName: The Path including the file and it's extension\n
        Content: The Content that should be written into the file
        '''

        f = open(pathAndName, "w")
        f.write(content)
        f.close()