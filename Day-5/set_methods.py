set1={'tom & jerry','oggy & cockroaches','power rangers','shinchan','motu patlu'}
set2={'oggy & cockroaches','roll 21','shinchan','heidi'}

print(set1.intersection(set2))
print(set1.union(set2))
print(set1.difference(set2))

print(set2.difference(set1))
print(set1.issubset(set2))
print(set1.issuperset(set2))