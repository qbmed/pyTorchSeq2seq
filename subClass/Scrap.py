class Scrap():
  def __init__(self,url):
    self.url=url
  def print(self):
    print(self.url)
sc=Scrap('http://iraset.org/')
sc.print();
