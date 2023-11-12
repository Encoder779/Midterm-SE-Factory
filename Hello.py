import validators # I used validators import for the validation of the url
import requests # I used requests and BeautifulSoup imports for the web scrapping
from bs4 import BeautifulSoup
import json # I used the json import for the type of file saving and importing of tabs

opennedTabs = [] # Create an empty list to append openned tabs to it

def openTab(): # Add new tab with title and url
    title = input("Please enter a title for the tab: ")
    url = input("Please enter a url for the tab: ")
    if (validators.url(url)):
        print("This is a valid url.")
        tab0 = {"Title" : title , "url" : url , "Nested tabs" : [] }
        opennedTabs.append(tab0)
        print("The " , title , " tab is added successfully.")
    else:
        print("This is not a valid url, please try again.")

def closeTab(): # Input the index of the tab to close (or none to close the last openned tab)
    if len(opennedTabs) > 0:
        index = input("Please enter the index of the tab you want to close (1,2,3,...) or press the enter button to close the last openned tab :")
        if index == "":
            closedTab = [] # Create an empty list to append closed tab to it
            closedTab.append(opennedTabs[-1])
            opennedTabs.pop(-1)
            print("The tab ", closedTab["Title"] , "is closed successfully.")
        else: # index is not empty
            int(index)
            closedTab = [] # Create an empty list to append closed tab to it
            closedTab.append(opennedTabs[index - 1])
            opennedTabs.pop(index - 1)
            print("The tab ", closedTab["Title"] , "is closed successfully.")
    else: # len(opennedTabs) <= 0 , but length can't be negative , so = 0
        print("There are no openned tabs to close, please open a tab and return to this option if you want to close it.")

def switchTab(): # Input the index of the chosen tab (or none to choose automatically the last openned tab) and displaying the html content of the url in it
    if len(opennedTabs) > 0:
        index = input("Please enter the index of tab you want to switch to (1,2,3,...) or press the enter button to switch to the last openned tab :")
        if index == "":
            switchedTab = opennedTabs[-1]
            url = switchedTab["url"]
            htmlText = requests.get(url).text
            soup = BeautifulSoup(htmlText , 'lxml')
            print(htmlText)
        else: # index is not empty
            int(index)
            switchedTab = opennedTabs[index - 1]
            url = switchedTab["url"]
            htmlText = requests.get(url).text
            soup = BeautifulSoup(htmlText , 'lxml')
            print(htmlText)
    else: # len(opennedTabs) <= 0 , but length can't be negative , so = 0
        print("There are no openned tabs to switch to, please open a tab and return to this option if you want to switch to it.")

def displayAllTabs(): # Display the titles of all the open tabs (including the nested tabs)
    if len(opennedTabs) > 0:
        print("All the openned tabs are/is :")
        for i in range(len(opennedTabs)):
            tab = opennedTabs[i]
            print(i + 1 ,")", tab["Title"])
            if tab["Nested tabs"]:
                for j in range(len(tab["Nested tabs"])):
                    nestedTab = tab["Nested tabs"][j]
                    print(i + 1 ,")",j + 1 ,")", nestedTab["Title"])
    else: # len(opennedTabs) <= 0 , but length can't be negative , so = 0
        print("There are no openned tabs to display, please open a tab and return to this option if you want to display it.")

def openNestedTabs(): # Input the index of the chosen tab to be the parent tab and then add the nested tabs with title and url to each of them
    if len(opennedTabs) > 0:
        index = input("Please enter the index of the tab you want it to be the parent tab (1,2,3,...): ")
        parentTab = opennedTabs[index - 1]
        counter = int(input("Please enter how many nested tabs you want to add under the parent tab: "))
        for i in range(counter):
            title = input("Please enter a title for the nested tab: ")
            url = input("Please enter a url for the nested tab: ")
            if (validators.url(url)):
                print("This is a valid url.")
                tabn = {"Title" : title , "url" : url , "Nested tabs" : [] }
                parentTab.append(tabn)
                print("The " , title , " nested tab is added successfully.")
            else:
                print("This is not a valid url, please try again.")
    else: # len(opennedTabs) <= 0 , but length can't be negative , so = 0
        print("There are no openned tabs, please open a tab and return to this option if you want to add nested tabs uder it.")

def clearAllTabs(): # Clear all the open tabs
    opennedTabs.clear()
    print("All the openned tabs are cleared. ")

def saveTabs(): # Input a file-path to save all the openned tabs (including the nested tabs) to it with their's title and url in JSON format
    if len(opennedTabs) > 0:
        file = input("Please enter the file-path you want to save the openned tabs to it: ")
        with open(file , 'w') as f:
            json.dump(opennedTabs , f , indent = 1)
        print("All the openned tabs were added to ", file ," successfully. ")
    else: # len(opennedTabs) <= 0 , but length can't be negative , so = 0
        print("There are no openned tabs to save, please open a tab and return to this option if you want to save it to a file.")

def importTabs(): # Input a file-path to load the tabs from the file
    file = input("Please enter the file-path you want to import the openned tabs from it: ")
    with open(file , 'r') as f:
        importedTabs = json.load(f)
    opennedTabs.extend(importedTabs)
    print("The tabs were imported successfully")

print("#### Hello dear users! ####")
print("***************************")
print("Welcome to the tab program!")
print("***************************")

x=1
while (x>0):
    print("<<<<<<<<<< MENU: >>>>>>>>>>")
    print("1. Open tab")
    print("2. Close tab")
    print("3. Switch tab")
    print("4. Display all tabs")
    print("5. Open nested tab")
    print("6. Clear all tabs")
    print("7. Save tabs")
    print("8. Import tabs")
    print("9. Exit")
    print("---------------------------")

    option = int(input("Please choose one of numbers from the options above: "))

    if option == 1:
        openTab()

    elif option == 2:
        closeTab()

    elif option == 3:
        switchTab()

    elif option == 4:
        displayAllTabs()

    elif option == 5:
        openNestedTabs()

    elif option == 6:
        clearAllTabs()

    elif option == 7:
        saveTabs()

    elif option == 8:
        importTabs()

    elif option == 9: # Terminate the program or the code
        print("Exitting the program.")
        print("########!Bye!########")
        break

    else:
        print("Invalid choice, please choose one of numbers from the options above: ")
