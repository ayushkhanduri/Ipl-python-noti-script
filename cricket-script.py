import requests
import notify2
from time import sleep
from bs4 import BeautifulSoup

def displayNotification(data):
	notify2.init("AnyNotifier");
	matchId = checkMatchStatus(data)
	score = data[matchId].text if matchId!=-1 else "No favourite teams playing"
	notification = notify2.Notification("Score: ", score)
	notification.show()

#finds if your favourite team has a match going on
def checkMatchStatus(data):
	allTeams = ["Delhi DareDevils" , "Gujarat Lions","Kings XI Punjab","Kolkata Knight Riders","Mumbai Indians","Rising Pune Supergiant","Royal Challengers Bangalore","Sunrisers Hyderabad"]
	allMatchesToday = []
	for index1 in range(len(data)):
		for index2 in range(len(allTeams)):
			if data[index1].text.find(allTeams[index2])!=-1:
				allMatchesToday.append(index1)	
				break
	return currentMatchGoing(data,allMatchesToday);

def currentMatchGoing(data,allMatchesToday):
	found = -1
	for index in reversed(allMatchesToday):
		if data[index].text.find("*")!=-1:
			found = index
			break
	return found;	
	
url = "http://static.cricinfo.com/rss/livescores.xml"

while True:
	r = requests.get(url)
	if r.status_code == 200:
		soup = BeautifulSoup(r.text,'html.parser');
		data = soup.find_all("description")
		displayNotification(data)
	sleep(600)
	
