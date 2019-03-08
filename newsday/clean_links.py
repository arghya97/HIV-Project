with open('article_links.txt','r') as fl:
    links = fl.readlines()

mod = []
for link in links:
    if link !='$content.urlLink.value':
        mod.append(link)

with open('article_links_mod.txt','w') as fl:
    fl.write(''.join(mod))
