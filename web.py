# we are going to make a program that will perform google search for us
# so we want 3 modules for  this for this program

# 1.webbrowser //which we use for opening address in browser
# 2.sys '''for user command line input'''
# 3.pyperclip //for getting the value from the clipboard

# 1 program

# import webbrowser as web
# import sys
# import pyperclip as pc
# CommandInput = sys.argv
# if len(CommandInput)>1:
#     SearchQuery=" ".join(CommandInput[1:])
# else:
#     SearchQuery=pc.paste();
# web.open("https://www.google.com/search?q="+SearchQuery);

# 2nd program
#  this program is for searching queries in variety of search engine
import  webbrowser as web
print("What are you want to do with me?")
print("do you want to search a query or you want to go to an URL")
print("---------------------------------------")
print("press 1 for a search query")
print("print 2 for opening an URL")
userValue=int(input())
if userValue==1:
    print("Where do you want to search your query?")
    print("press 1 for google.com")
    print("press 2 for bing.com")
    print("press 3 for duckduckgo.com")
    print("press 3 for duckduckgo.com")
    print("press 4 for youtube.com")
    searchPref=int(input())
    if searchPref==1:
        print("Enter your query : ")
        query=input()
        print("Seraching "+query+" in google")
        web.open("https://www.google.com/search?q="+query)
    elif searchPref==2:
        print("Enter your query : ")
        query = input()
        print("Seraching " + query + " in Bing")
        web.open("https://www.bing.com/search?q=" + query)
    elif searchPref==3:
        print("Enter your query : ")
        query = input()
        print("Seraching " + query + " in Duckduckgo")
        web.open("https://duckduckgo.com/?q="+query+"&ia=web")
    elif searchPref==4:
        print("Enter your query : ")
        query = input()
        print("Seraching " + query + " in Youtube")
        web.open("https://www.youtube.com/results?q="+query)
    else:
        print("Wrong option")
elif userValue==2:
    print("Enter the URL")
    URLis=input()
    print("Opening "+URLis+"...")
    web.open(URLis)

else:
    print("You have chosen wrong option")