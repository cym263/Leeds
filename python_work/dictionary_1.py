birthdays = {'Newton' : 1642, 'Darwin' : 1809}

print birthdays['Newton']
#print birthdays['1809']

band = ["mel", "geri", "victoria", "mel", "emma"]
counts = {}

for name in band:
   if name not in counts:
      counts[name] = 1
   else:
      counts[name] += 1

for name in counts:
   print name, counts[name]

print counts

dir(counts)
print counts.items()
print counts.keys()
print counts.values()


