import json


import matplotlib.pyplot as plt


class Histogram:

    def __init__(self):
        self.items = {}

    def add(self, server):
        if server in self.items:
            self.items[server] += 1
        else:
            self.items[server] = 1

    def count(self, server):
        return self.items[server]

    def get_dict(self):
        return self.items


crawler = Histogram()


with open('servers.json', 'r') as f:
    data = json.load(f)
data = [s.encode('utf-8') for s in data]

for server in data:
    if 'Apache' in server or 'Apashi' in server:
        crawler.add('Apache')
    elif 'nginx' in server:
        crawler.add('nginx')
    elif 'lighttpd' in server:
        crawler.add('lighttpd')
    elif 'IIS' in server:
        crawler.add('IIS')


plt.bar(range(len(crawler.get_dict())), crawler.get_dict().values(), align='center')
plt.xticks(range(len(crawler.get_dict())), crawler.get_dict().keys())

print(plt.show())

