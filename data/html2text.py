from bs4 import BeautifulSoup

filename = "your_report.html"
with open(filename, 'r') as f:
    text = f.read()
# Initializing variable
gfg = BeautifulSoup(text)
 
# Calculating result
res = gfg.get_text()
 
# Printing the result
print(res)
