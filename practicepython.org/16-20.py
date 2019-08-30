# EX 16
from random import randint
passList = "#$%&'()*+,-./:;<=>?@[\]^_`{|}~0123456789abcdefghijklmnopqrstuvwxyz"
pass_user = int(input("How many characters would you lie your password to have"))
i = 1 
final_pass = ""
#possible to use choice(sequence) or sample(sequence,k)
while i < pass_user:
    final_pass += passList[randint(1,len(passList)-1)]
    i += 1
print(final_pass)


# EX 17
from bs4 import BeautifulSoup
import requests
url = "https://www.nytimes.com/"
r_html = requests.get(url)
r_text = r_html.text
p_print = BeautifulSoup(r_text,"html.parser")
titles = p_print.find_all("h2")
for (i,x) in enumerate(titles):
    if i == 28 or i == 27:
        continue
    print(x.text)

# EX 18
from random import sample

print("Welcome to the Cows and Bulls Game")

numbers = "0123456789"
random_number = sample(numbers, 4)
print(random_number)
game_continue = True
counter = 1

def compare_value(userN, randN):
    cows = 0
    bulls = 0
    iv_random = list(enumerate(randN))
    iv_user = list(enumerate(userN))
    for i,v in iv_user:
        for j,w in iv_random:
            if i == j and v == w:
                cows += 1
            elif v == w and i != j:
                bulls += 1
                continue
            else:
                continue
    return cows, bulls

while game_continue:
    user_num = input("Enter a number: ")
    cowbulls = compare_value(user_num, random_number)
    
    if cowbulls[0] == 4:
        print("You won the game after {} guesses".format(counter))
        game_continue = False
        
    else:
        cowbulls = compare_value(user_num, random_number)
        print("You have {0} cow(s) and {1} bull(s)".format(cowbulls[0], cowbulls[1]))
        counter += 1
        game_continue = True

# EX 19
import requests
from bs4 import BeautifulSoup

url = "https://www.vanityfair.com/style/society/2014/06/monica-lewinsky-humiliation-culture"
page = requests.get(url)
p_html = page.text

soup = BeautifulSoup(p_html,"html.parser")
full_text = soup.find_all("p")
for i in full_text:
    print(i.text)
    
# EX 20
def binary_search(aList, target):
    lower = 0
    upper = len(aList) - 1

    while lower <= upper:
        mid = (lower + upper) // 2
        print(mid)
        if aList[mid] == target:
            return ("Target found at index: ", mid)
        elif aList[mid] < target:
            lower = mid + 1
        elif aList[mid] > target:
            upper = mid - 1
    if target not in aList:
        print("Target not found")
