import requests

def get_file_from_url(url, allow_redirects=True):
    """Download a file with the URL link.

    This function takes a url as a string and returns
    """
    file = requests.get(url, allow_redirects)
    # open("testWorkbook.xlsx", "wb").write(file.content)
    return file.content
