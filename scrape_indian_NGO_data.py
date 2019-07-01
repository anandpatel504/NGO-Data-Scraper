import requests
from bs4 import BeautifulSoup
import pprint

url = "https://www.giveindia.org/certified-indian-ngos"
	
def NGO_data(soup):

	page = requests.get(url)
	data = page.text
	soup = BeautifulSoup(page.text,"html.parser")

	div=soup.find('table',class_="jsx-697282504 certified-ngo-table")
	# print(div)
	trs=div.find_all('tr',class_="jsx-697282504")

	main_list=[]
	for i in trs:
		name=i.find_all('td',class_="jsx-697282504")
		list1=[]
		for i in name:
			a=(i.text)
			list1.append(a)
		main_list.append(list1)
	# print(main_list)
	Dict_list=[]
	for i in range(1,len(main_list)):
		b=(main_list[i])
		# print(b)
		Dict={"name":b[0],"cause":b[1],"state":b[2]}
		Dict_list.append(Dict)
	# print(Dict_list)
	state_list=[]
	for i in Dict_list:
		c=(i["state"])
		if c not in state_list:
			state_list.append(c)
	# print(state_list)
	Dict_2={}
	for i in state_list:
		list2=[]
		for j in Dict_list:
			if i==j["state"]:
				list2.append(j)
		Dict_2[i]=list2
	# return(Dict_2)
	pprint.pprint(Dict_2)


NGO_data(url)
