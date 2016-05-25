"""Writes text to a file."""


def writeFile(fileName, fileText):
    """Write text to a file."""
    file = open(fileName, 'a')
    file.write(fileText)

writeFile("josh.txt", "Hi, this is Josh!")
