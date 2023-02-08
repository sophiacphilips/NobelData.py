#Name: Sophia Philips
#GitHub Username: sophiacphilips
#Date: 02/06/2023
#This code is designed to read a nobel prize json file and search the data within it
#When given a year and category (2000, chemistry) it will return an alphabetical list of the winner's surnames




import json
class NobelData:
    """
    init method reads nobel prize json file
    """
    def __init__(self):
        with open('nobels.json', 'r') as infile: #opens json file
            self._nobels_list = json.load(infile) #loads json file

    def search_nobel(self, year, category):
        """
        search nobel takes a year and category from the user and returns a list of winner's surnames
        """
        prize_list = len(self._nobels_list['prizes']) #length of prize list
        winners = [] #list of winners
        surnames_list = [] #list of surnames

        for i in range(0, prize_list): #iterates through prize list
            if (self._nobels_list["prizes"][i]["year"]==year and #finds and matches year within prize list
                    self._nobels_list['prizes'][i]['category']==category):#finds and matches category within prize list
                winners = self._nobels_list['prizes'][i]['laureates'] #finds names of winners in prize list
        winners_length = len(winners) #moves through length of winners list
        for i in range(0, winners_length): #iterates through list
            surnames_list.append(winners[i]['surname']) #adds surnames of the winners to the list that will be returned
        surnames_list.sort() #sorts names alphabetically
        return surnames_list #returns list of surnnames

