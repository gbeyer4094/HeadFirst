phrase = "Don't panic!"
plist = list(phrase)
print(phrase)
print(plist)

plist.remove("'")
plist.pop(0)

plist.insert(3, plist.pop(2))
for x in range(4):
    plist.pop()
plist.insert(4, plist.pop(5))

new_phrase = ''.join(plist)
print(plist)
print(new_phrase)