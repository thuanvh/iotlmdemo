from bs4 import BeautifulSoup
 
# Initializing variable
gfg = BeautifulSoup("<b>Section </b><br/>BeautifulSoup<ul>\
<li>Example <b>1</b></li>")
 
# Calculating result
res = gfg.get_text()
 
# Printing the result
print(res)
