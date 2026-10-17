import re


text = "I love animals, mountains, sea and river. streams flowers. If i" \
"get a chance will love to stay in mountains"

sch = re.search("mountains",text)

print(sch)

findl = re.findall("mountains", text, re.IGNORECASE)

print(findl)

new_text = re.sub("mountains","hills",text)

print(new_text)