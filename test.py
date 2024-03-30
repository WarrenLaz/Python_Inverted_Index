string = 'https://en.wikipedia.org/wiki?curid=17249'
docid = ""
i=-1
while(string[i] != '='):
    docid += string[i]
    i-=1
docid = docid[::-1]
print(docid)
tuple = (int(2), int(1))
tuple[1] =  4
print(tuple[-1])