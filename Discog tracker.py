############################################################################### discog tracker 1.0 ##############################################################################
################################################################################# by Autumn Hill ################################################################################

with open("discog list.txt") as textFile:
    ArtistList = [line.split(",") for line in textFile]        #Open text file and puts in 2D array

################################################################################## subroutines ##################################################################################

def PrintArtists(ArtistList):                                               #this function prints the artist list
    for loop in range(len(ArtistList)):
        print(str(ArtistList[loop][0]) + ". " + ArtistList[loop][1])
        AddArtistCounter = ArtistList[loop][0]
    return AddArtistCounter

def HowManyLeft(ArtistList, ArtistNum):                                     #this function shows discog progress
    if ArtistList[ArtistNum][2] == ArtistList[ArtistNum][3]:
        print("You have heard every album by " + ArtistList[ArtistNum][1] + ". Well done!")
    else:
        Difference = ArtistList[ArtistNum][2] - ArtistList[ArtistNum][3]
        print("You have " + str(Difference) + " more albums by " + ArtistList[ArtistNum][1] + " to listen to. Good Luck!")
    return

def DisplayMenu():            #shows menu of all user options
    Loop = True
    while Loop == True:
        print("1. Albums Overview")
        print("2. Sort artists")
        print("3. Artist Overview")
        print("4. Add Artist")
        print("5. Add a listen to existing artist")
        print("6. Update artist discog count")
        print("7. Additional info")
        Choice = int(input("Pick a number: "))

        if Choice > 0 and Choice < 8:
            Loop = False
            return Choice
        else:
            print("Number not in list Choose again")
            print("")


def PickArtist():
    ArtistNum = int(input("Choose an artist by the number next to them: "))
    if ArtistNum != 1:
        ArtistNum = ArtistNum - 2                                   #because of 2d array shananigans, you have to -2 their answer to make it select correctly. Don't ask me why it just works.
    else:
        ArtistNum = ArtistNum - 1
    return ArtistNum

def ArtistOverview(ArtistList):
    ArtistNum = PickArtist()
    print(ArtistList[ArtistNum][1] + " has " + str(ArtistList[ArtistNum][2]) + " albums of which you have heard " + str(ArtistList[ArtistNum][3]))
    return

def AlbumOverview(ArtistList):
    TotalAlbums = 0
    HeardAlbums = 0
    for loop in range(len(ArtistList)):
        TotalAlbums = TotalAlbums + ArtistList[loop][2]         #shows total progress on albums
        HeardAlbums = HeardAlbums + ArtistList[loop][3]
    print("There is a total of " + str(TotalAlbums) + " albums")
    print("You've heard " + str(HeardAlbums) + " albums")
    AlbumsLeft = TotalAlbums - HeardAlbums
    print("You have " + str(AlbumsLeft) + " albums left to hear. Good luck")
    return

def SortArtists(ArtistList):
    SortedList = [["placeholder",0.0]]                               #sorts artists by percentage of discog done
    for loop in range(len(ArtistList)):
        TempArtist = ArtistList[loop][1]
        if ArtistList[loop][3] != 0:
            TempPercentage = (ArtistList[loop][3]/ArtistList[loop][2]) * 100
            SortLoop = True
            TempCount = 0
            while SortLoop == True:
                if SortedList[TempCount][1] <= TempPercentage:
                    SortedList.insert(TempCount, [TempArtist, TempPercentage])
                    SortLoop = False
                else:
                    TempCount += 1
                    SortLoop = True
        else:
            SortedList.append([TempArtist, 0.0])
    for loop in range(len(SortedList)):
        print(str(loop + 1) + ". " + str(SortedList[loop][0]) + " " + str(SortedList[loop][1]) + "%")

    return

def AddArtist(ArtistList, AddArtistCounter):
    print(AddArtistCounter +"A")
    AddArtistCounter = int(AddArtistCounter) + 1                                            #adds new artist to the text file
    ArtistName = input("What is your artists name (please capatalise names properly): ")
    TotalAlbums = input("How many albums does " + ArtistName +" have: ")
    HeardAlbums = input("How many albums have you heard from " + ArtistName + ": ")
    with open("discog list.txt", 'a') as textFile: 
        textFile.write(str(AddArtistCounter) + "," + ArtistName + "," + TotalAlbums + "," + HeardAlbums + "\n" )
    return AddArtistCounter

def UpdateAlbumsHeard(ArtistList, Number):
    ArtistNum = PickArtist()
    TotalAlbums = ArtistList[ArtistNum][2]              #updates the amount of albums heard
    HeardAlbums = ArtistList[ArtistNum][3]
    ArtistName = ArtistList[ArtistNum][1]
    print("You've previously heard " + str(ArtistList[ArtistNum][3]) + " albums by " + ArtistList[ArtistNum][1])
    NewAlbumCount = input("How many albums by " + ArtistList[ArtistNum][1] + " have you heard now: ")
    lines = open("discog list.txt", "r").readlines()
    lines[ArtistNum] = str(Number) + "," + str(ArtistName) + "," + str(TotalAlbums) + "," + str(NewAlbumCount) + "\n"
    out = open("discog list.txt", "w")
    out.writelines(lines)
    out.close()
    return

def UpdateDiscogAccount(ArtistList, Number):
    ArtistNum = PickArtist()
    TotalAlbums = ArtistList[ArtistNum][2]
    HeardAlbums = ArtistList[ArtistNum][3]              #updates the amount of albums an artist has
    ArtistName = ArtistList[ArtistNum][1]
    print(ArtistList[ArtistNum][1] + " currently has " + str(ArtistList[ArtistNum][2]) + " albums")
    NewAlbumCount = input("How many albums does " + ArtistList[ArtistNum][1] + " have now: ")
    lines = open("discog list.txt", "r").readlines()
    lines[ArtistNum] = str(Number) + "," + str(ArtistName) + "," + str(NewAlbumCount) + "," + str(HeardAlbums) + "\n"
    out = open("discog list.txt", "w")
    out.writelines(lines)
    out.close()
    return

def AdditionalInfo():
    print("")
    print("Made to help track progress on going through discographies")
    print("Program must be restarted for any changes to register")
    print("If you have feature suggestions feel free to give them")
    print("Will not work without discog list.txt")
    print("I'd reccomend RYM to find how many albums an artist has (aoty supremacy tho)")
    print("Follow me @ninjakirby1969 on twitter i talk about music a lot :3")
    print("")
    print("Originally coded by Autumn Hill/Ninjakirbz")
    print("Open source. Feel free to copy, modify and distribute though I ask morally to keep in credit for me")
    print("Version 1.0.0 13/09/2024 (dd/mm/yyyy)")
    return
#################################################################################### main code ####################################################################################

AddArtistCounter = PrintArtists(ArtistList)
print("")
for loop in range(len(ArtistList)):
        ArtistList[loop][0] = int(ArtistList[loop][0])  #makes all numbers in the text file integers
        ArtistList[loop][2] = int(ArtistList[loop][2])
        ArtistList[loop][3] = int(ArtistList[loop][3])

MainLoop = True
while MainLoop == True:
    
    Choice = DisplayMenu()

    if Choice == 1:
        AlbumOverview(ArtistList)   #does different functions based on menu choice
    elif Choice == 2:
        SortArtists(ArtistList)
    elif Choice == 3:
        ArtistOverview(ArtistList)
    elif Choice == 4:
        AddArtistCounter = AddArtist(ArtistList, AddArtistCounter)
    elif Choice == 5:
        UpdateAlbumsHeard(ArtistList, AddArtistCounter)
    elif Choice == 6:
        UpdateDiscogAccount(ArtistList, AddArtistCounter)
    elif Choice == 7:
        AdditionalInfo()

    print("")
    Again = input("Again? Y/N ").upper()

    if Again == "N":
        MainLoop = False            #breaks loop ends program
        print("")
        print("Thanks for using my program!")
    else:
        print("")
        DisplayAgain = input("Do you want the list to be displayed again Y/N ").upper()
        if DisplayAgain == "Y":
            print(" ")
            PrintArtists(ArtistList)

#finished on the 13th September 2024