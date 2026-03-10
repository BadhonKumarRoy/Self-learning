#Day 7 - Sets
#Level 1
#1
it_companies = {"Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"}
print(len(it_companies))
#2
it_companies.add('Twitter')
print(it_companies)
#3
it_companies.update(['Cognizant', 'TCS', 'Wipro'])
print(it_companies)
#4
it_companies.remove('Wipro')
print(it_companies)
#5
it_companies.discard('Wipro')
#it_companies.remove('Wipro') Shows error as Wipro is already removed in step 4
#Level 2
#1
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
print(A.union(B))
#2
print(A.intersection(B))
#3
print(A.issubset(B))
#4
print(A.isdisjoint(B))
#5
print(A.union(B))
print(B.union(A))
#6
print(A.symmetric_difference(B))
#7
del A
del B
#Level 3
#1
age = [22, 19, 24, 25, 26, 24, 25, 24]
age_set = set(age)
if len(age) > len(age_set):
    print("The list is Bigger than the set")
else:
    print("Both are equal")
#2
string1 = "I am a teacher and I love to inspire and teach people"
list1 = string1.split()
tuple1 = tuple(list1)
set1 = set(list1)
print(type(string1))
print(type(list1))
print(type(tuple1))
print(type(set1))
#3
sentence = "I am a teacher and I love to inspire and teach people"
words = sentence.split()
unique_words = set(words)
print(len(unique_words))
print(unique_words)
#The end
