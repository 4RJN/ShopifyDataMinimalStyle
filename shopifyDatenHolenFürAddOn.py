# Shopify Internals

reader = open("peter.html", 'r', encoding='UTF-8')
inhalt = reader.read().split('<script>var Shopify = Shopify || {};\n')
gefiltert = inhalt[1].split(';</script>')
d = dict(x.split(" = ") for x in gefiltert[0].split(';\n'))
print(d['Shopify.locale'])
print(d['Shopify.theme'])
print(d['Shopify.currency'])
print(d.values())

d = dict((x.strip(), y.strip()) for x,y in (element.split('-') for element in reader.split(', ')))
