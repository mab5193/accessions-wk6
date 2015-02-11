accs = ["xkn59438", "yhdck2", "eihd39d9", "chdsye847", "hedle3455",
"xjhd53e", "45da", "de37dp"]
for acc in accs: 
	#print if it passes the test

#contain the number 5
for acc in accs:
if re.search(r"5", acc):
print("\t" + acc)

#contain letters d or e
for acc in accs:
if re.search(r"(d|e)", acc):
print("\t" + acc)

#contain both d and e
for acc in accs:
if re.search(r"d.*e", acc):
print("\t" + acc)

#contain d followed by a single letter, followed by e
for acc in accs:
if re.search(r"(d.e)", acc):
print("\t" + acc)

#contain d and e in any order
for acc in accs:
if re.search(r"d.*e", acc) or re.search(r"e.*d", acc):
print("\t" + acc)

#start with either x or y
for acc in accs:
if re.search(r"^(x|y)", acc):
print("\t" + acc)

#start with x or y and ends with e
for acc in accs:
if re.search(r"^(x|y).*e$", acc):
print("\t" + acc)

#match 3 or more numbers in a row
for acc in accs:
if re.search(r"\d{3,}", acc):
print("\t" + acc)

#end with d followed by either a, r or p
for acc in accs:
if re.search(r"d[arp]$", acc):
print("\t" + acc)