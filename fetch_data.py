from bs4 import BeautifulSoup
import requests
import wget

prefix = 'https://digital.nmla.metoffice.gov.uk/download/file/'
suffix = 'IO_5eac6aa4-b455-45e5-9610-b6507cfb1cd8'


r  = requests.get("https://digital.nmla.metoffice.gov.uk/SO_feb1a621-72a3-4501-a6d2-8af1a8abe545/")
data = r.text
soup = BeautifulSoup(data)

top_levels = []

for link in soup.find_all('a'):
  url = link.get('href')
  if url and url.startswith('https') and 'SO' in url:
    #print(url)
    top_levels.append(url)

files = {}
for u in top_levels:
  files[u] = []
  r  = requests.get(u)
  data = r.text
  soup = BeautifulSoup(data)
  for link in soup.find_all('a'):
    url = link.get('href')
    if url and url.startswith('https') and 'IO' in url:
      #print(url)
      s = url[url.find('IO'):]
      s = s[:s.find('/')]
      files[u].append((s, link.text))
    files[u] = sorted(list(set(files[u])))

done = []
for k in files:
  print(k)
  for f in files[k]:
    print('\t', f)
    if f[0] not in done:
      filename = wget.download(prefix+f[0])
      done.append(f[0])
    print('\t','done!')
    #f = requests.get(prefix+f)
  print('---')
