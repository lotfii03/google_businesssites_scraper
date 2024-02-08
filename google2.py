from googlesearch import search

results = search('site:business.site', country ='NL', num=100, verify_ssl=False)
for result in results:
    print(result)


