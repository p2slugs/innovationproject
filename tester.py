import json


#Make a Dictionary of you, your siblings, parents, and grandparents.  Have at least 4 attributes per person.


fm1 = { "name":"Linda", "age":18, "food":"cheese"}
fm2 = { "name":"Christina", "age":44, "food":"seafood", "parent":True}
fm3 = { "name":"Henry", "age":48, "food":"beef",  "parent":True}
fm4 = { "name":"Yu", "age":74, "food":"pork", "grandparent":True}
fm5 = { "name":"Zhong", "age":83, "food":"cookies", "grandparent":True}


#Turn the dictionaries into a list.


list_of_family_members = [fm1, fm2, fm3, fm4, fm5]
print("List Of Family Members")
print(type(list_of_family_members))
print(list_of_family_members)
print()
for family_member in list_of_family_members:
    print(family_member['name'] + ", " + str(family_member['age']) + ", " + family_member['food'])
print()


#Turn the list into a dictionary called 'family'


family = {'family_members': list_of_family_members}


#Print members to run/console


print("Dictionary Of Family Members")
print(type(family))
print(family)
family_members = family['family_members']
print()
for family_member in family_members:
    print(family_member['name'] + ", " + str(family_member['age']) + ", " + family_member['food'])
print()


#Turn the dictionary into a JSON file


json_family_members = json.dumps(family)


#Print the JSON file to the run/console window, inserting a character or emoji in between each item in the JSON.


print("JSON Family Members")
print(type(json_family_members))
print(json_family_members)
x = json.loads(json_family_members)
family_members = x['family_members']
print()
for family_member in family_members:
    print(family_member['name'] + ", " + str(family_member['age']) + ", " + family_member['food'])
    print('👍🏻')
print()


#Return JSON file to a dictionary with key "family"- my key is family_members
print("Return JSON File To A Dictionary - Key is family_members")
print(json_family_members)


#Using program logic, make new dictionaries from "family" key/values, creating "parents" and "grandparents" key with logically corresponding lists as values.


dictfamilymembers = json.loads(json_family_members)


listfamilymembers = dictfamilymembers['family_members']


parents = []
grandparents = []
me = []


for member in listfamilymembers:
    if "parent" in member:
        parents.append(member)
    elif "grandparent" in member:
        grandparents.append(member)
    else:
        me.append(member)


#Print members to run/console in fashion that highlights
print()
print("Organized Members")
print()


print("Parents")
print(parents)
print()
for member in parents:
    print(member['name'] + ", " + str(member['age']) + ", " + member['food'])
print()


print("Grandparents")
print(grandparents)
print()
for member in grandparents:
    print(member['name'] + ", " + str(member['age']) + ", " + member['food'])
print()


print("Me")
print(me)
print()
for member in me:
    print(member['name'] + ", " + str(member['age']) + ", " + member['food'])
print()



#Place code in text form in journal as well as run/console output.


