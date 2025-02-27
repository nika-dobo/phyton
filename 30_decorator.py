#decorator

import webbrowser

def validator(func):
    def wrpper(url):
        if "." in url:
            func(url)
        else:    
            print("url is not valid")
    return wrpper


@validator#decorator
def opep_url(url):
    webbrowser.open(url)

opep_url("https://www.google.com") #ხსნის ლინს რასაც მივუთითებთ