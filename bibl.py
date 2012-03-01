
from collections import defaultdict
import csv
from jinja2 import Template

# Get template
template = Template(open("template.html").read())

bibl = defaultdict(list)
for row in csv.DictReader(open("bibl.csv")):
    key = row['short_new']
    letter = key[0].capitalize()
    bibl[letter].append(
        (unicode(key, "utf-8"), 
         unicode(row['long'], "utf-8"), 
         [unicode(s, "utf-8") for s in row['shorts'].split("; ")] ))

letter = 'A'
items = sorted(bibl[letter])
html = template.render(letter=letter, items=items).encode("utf-8")
sink = open("htdocs/%s.html" % letter, "w")
sink.write(html)
sink.close()

