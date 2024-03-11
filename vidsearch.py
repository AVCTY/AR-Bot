#Importing all necessary libraries
import urllib.request, urllib.parse, re, webbrowser


#Defining the searching codes for video names
def searchinput():
    global query_string
    global html_content
    global search_results
    
    query_string = urllib.parse.urlencode({"search_query" : input("Enter a video title:")})

    html_content = urllib.request.urlopen("http://www.youtube.com/results?" + query_string)

    search_results = re.findall(r'href=\"\/watch\?v=(.{11})', html_content.read().decode())
    


#Code here prints out the url link of searched video
#and shows the search result from the search query
def searchoutput():
    global result
    global videoname
    global url
    
    result= print("\nHere is your search result for:", query_string)

    videoname= print("Video for:", query_string, "http://www.youtube.com/watch?v=" + search_results[0])

    url= ("http://www.youtube.com/watch?v=" + search_results[0])
    


#This line opens up the searched video on YouTube on the computer's default browser
def outputopen():
    webbrowser.open_new_tab(url)


#Calling out the functions
searchinput()
searchoutput()
outputopen()

