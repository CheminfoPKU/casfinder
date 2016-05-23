from chemspipy import ChemSpider
import os
import re
import requests
import bs4

#simles to chemspider id
def smiles2cas(smiles_input):
    myToken = 'a1d50aa3-6729-49df-a3e1-cd66240fab22'
    cs = ChemSpider(security_token=myToken)
    
    comp = cs.search(smiles_input)
    for result in comp:
        temp = result  
    res = temp.csid
    res = str(res)
    
    http = requests.session()
    url = 'http://www.chemspider.com/MassSpecApi.asmx/GetExtendedCompoundInfoArray' 
    params={'token':myToken} 
    http.post(url, data=params)  
    
    url_search = 'http://www.chemspider.com/Search.aspx?q='+res
    r = http.get(url_search)
    soup = bs4.BeautifulSoup(r.text,"html.parser")
    cas = [a.attrs.get('href') for a in soup.select('div.syn a[title="RN"]')]
    
    for x in range(len(cas)):
        cas[x] = re.findall(r"\"(.+?)\"",cas[x])
    
    return(cas)
    