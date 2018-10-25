from bs4 import BeautifulSoup
import requests

payload = {'usuario': '', 'passwd': ''}
Session_CIEE = requests.Session()
Session_CIEE.post("http://www.ciee.org.br/portal/validalogin.asp", data = payload)
response3 = Session_CIEE.post('http://www.ciee.org.br/portal/estudantes/servicos/vagas.asp?')

soup = BeautifulSoup(response3.content, 'html.parser')
text = soup.find("table", { "width" : "100%" })
text = text.find("span", { "style" : "font-size: 12px" })
print(text.get_text())
