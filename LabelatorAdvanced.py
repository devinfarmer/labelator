
import urllib.request
from bs4 import BeautifulSoup

def addspaces(callno):
    if callno is "":
        return None
    
    c = callno.split()
    for s in c:
        if s is None:
            return None
    
    if c[0] == "J":

        j_options = ["Fiction", "Picture", "Beginner", "Board", "GN"]
        if c[1] in j_options:
            c.insert(2, " ")

        elif c[1] == "Bio":
            c.insert(2, " ").insert(2, " ")

        elif len(c) == 4:
            c.insert(2, " ")

        elif len(c) == 5:
            c.insert(3, " ")

        elif len(c) >= 6:
            c.insert(4, " ")

    elif c[0] == "YA":
        if c[1] == "Fiction":
            c.insert(2, " ")

        elif len(c) == 4:
            c.insert(2, " ")

        elif len(c) == 5:
            c.insert(3, " ")

        elif len(c) >= 6:
            c.insert(4, " ")

    elif c[0] == "Fiction":
        c.insert(1, " ")

    elif c[0] == "PME":
        c.insert(2, " ")

    elif c[0] == "GN":
        c.insert(1, " ")

    else:
        if len(c) == 3:
            c.insert(1, " ")
            c.insert(1, " ")

        elif len(c) == 4:
            c.insert(2, " ")

        elif len(c) >= 5:
            c.insert(3, " ")

    result = "\n".join(c)
    return result

def get_call_number(item_id):
    url = f"https://mccs.ent.sirsi.net/client/en_US/butler/search/results?qu={item_id}"

    with urllib.request.urlopen(url) as response:
       html = response.read()

    soup = BeautifulSoup(html, 'html.parser')

    tds = soup.find_all("td")
    for i in range(len(tds)):
        if item_id in tds[i].get_text():
            call_number = tds[i-3].get_text()
#             print(addspaces(call_number))
            return addspaces(call_number)

    return "No Label Found."


while True:
	cn = input("Please Scan Item ID...")
	print("-----------------")
	print(get_call_number(cn))
	print("-----------------")
	print()