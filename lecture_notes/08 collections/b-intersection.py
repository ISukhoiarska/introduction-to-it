intersection = lambda s1, s2: s1 & s2

cities1 = {'Beijing', 'Kiev'}
cities2 = {'Kiev', 'London', 'Baghdad'}

print({'cities1': cities1})
print({'cities2': cities2})

results = intersection(cities1, cities2)
print(results)
