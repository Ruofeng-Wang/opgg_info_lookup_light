"""
	@author: Ed-is-on Wang
	@date: 1/5/2021
	@location: Berkeley, CA
"""
import webbrowser
from urllib import request, response, error, parse
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup

def main():
	query = input("Champion and Line:")
	query = query.split()
	URL = "https://na.op.gg/champion/" + query[0].lower() + "/statistics/" + query[1].lower() + "/build"

	req = Request(URL)
	html = request.urlopen(req)
	soup = BeautifulSoup(html, "html.parser")
	countercp = soup.find("table", {"class": "champion-stats-header-matchup__table champion-stats-header-matchup__table--strong tabItem"})
	tbody = countercp.find("tbody")
	tr = tbody.find_all("tr")
	champinfo = []
	
	for t in tr[0:3]:
		champ = []
		for td in t.find_all("td")[0:2]:
			if (td["class"][0] == "champion-stats-header-matchup__table__champion"):
				champ.append(td.text.strip())
			if (td["class"][0] == "champion-stats-header-matchup__table__winrate"):
				champ.append(td.text.strip().split())
		champinfo.append(champ)

	countercp = soup.find("table", {"class": "champion-stats-header-matchup__table champion-stats-header-matchup__table--weak tabItem"})
	tbody = countercp.find("tbody")
	tr = tbody.find_all("tr")

	for t in tr[0:3]:
		champ = []
		for td in t.find_all("td")[0:2]:
			if (td["class"][0] == "champion-stats-header-matchup__table__champion"):
				champ.append(td.text.strip())
			if (td["class"][0] == "champion-stats-header-matchup__table__winrate"):
				champ.append(td.text.strip().split())
		champinfo.append(champ)    



	print("Counter Champion:")	
	print(champinfo[0][0] + "	" + champinfo[0][1][0] + " " + champinfo[0][1][1] + ": " + champinfo[0][1][2])
	print(champinfo[1][0] + "	" + champinfo[1][1][0] + " " + champinfo[1][1][1] + ": " + champinfo[1][1][2])
	print(champinfo[2][0] + "	" + champinfo[2][1][0] + " " + champinfo[2][1][1] + ": " + champinfo[2][1][2])
	print("Strong Against:")
	print(champinfo[3][0] + "	" + champinfo[3][1][0] + " " + champinfo[3][1][1] + ": " + champinfo[3][1][2])
	print(champinfo[4][0] + "	" + champinfo[4][1][0] + " " + champinfo[4][1][1] + ": " + champinfo[4][1][2])
	print(champinfo[5][0] + "	" + champinfo[5][1][0] + " " + champinfo[5][1][1] + ": " + champinfo[5][1][2])


if __name__ == "__main__":
	main()

