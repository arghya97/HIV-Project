with open('article_links.txt','r') as fl:
    links = fl.readlines()

mod = []
for link in links:
    if link !='$content.urlLink.value\n':
        if 'https://' not in link:
            link_mod = 'https'+link[4:]
            mod.append(link_mod)
        else:
            mod.append(link)

with open('article_links_mod.txt','w') as fl:
    fl.write(''.join(mod))
