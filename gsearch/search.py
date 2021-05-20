import webbrowser

def google():
    content = input("Query :- ")
    url = "https://www.google.com/search?q="+content
    webbrowser.get().open(url)

def youtube():
    content = input("Query :- ")
    url = "https://www.youtube.com/results?search_query="+content
    webbrowser.get().open(url)   


