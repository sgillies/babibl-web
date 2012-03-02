
from collections import defaultdict
import csv
from datetime import datetime
from jinja2 import Template
from unidecode import unidecode

# Get template
template = Template(open("template.html").read())

bibl = defaultdict(list)
for row in csv.DictReader(open("bibl.csv")):
    key = unicode(row['short_new'], "utf-8")
    letter = unidecode(key)[0].lower()
    bibl[letter].append(
        (key, 
         unicode(row['long'], "utf-8"), 
         [unicode(s, "utf-8") for s in row['shorts'].split("; ")] ))

for letter in sorted(bibl.keys()):
    items = sorted(bibl[letter])
    html = template.render(
        keys=sorted(bibl.keys()),
        letter=letter, 
        items=items, 
        modified=datetime.now().isoformat(),
        ).encode("utf-8")
    sink = open("htdocs/%s.html" % letter, "w")
    sink.write(html)
    sink.close()

html = template.render(
    keys=sorted(bibl.keys()),
    letter="Index", 
    items=[], 
    modified=datetime.now().isoformat(),
    ).encode("utf-8")
sink = open("htdocs/index.html", "w")
sink.write(html)
sink.close()

