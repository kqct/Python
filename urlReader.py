"""Reads the HTML code from a website."""

from urllib.request import urlopen as urlOpen
from writeTextToFile import writeFile


def readURL(outFileName):
    """Read the content of a URL."""
    url = input("Please enter a URL: ")
    urlResponse = urlOpen(url)
    urlData = urlResponse.read()
    # urlText = urlData.decode('utf-8')
    writeFile(outFileName, urlData)

readURL("output.txt")
