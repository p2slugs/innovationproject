# code here
import json

# some dictionaries
p1 = { "name":"John", "age":30, "city":"New York"}
p2 = { "name":"Betty", "age":10, "city":"Alaska"}
p3 = { "name":"George", "age":40, "city":"San Diego"}
p4 = { "name":"Eva", "age":17, "city":"Seattle"}


# a list of dictionaries
list_of_people = [p1, p2, p3, p4]
# write some code to Print List of people one by one
print("List of people")
print(type(list_of_people))
print(list_of_people)
for person in list_of_people:
    print(person['name'] + "," + str(person['age']) + "," + person['city'])
print()

# turn list to dictionary of people
dict_people = {'people': list_of_people}
print("Dictionary of people")
# write some code to Print People from Dictionary
print(type(dict_people))
print(dict_people)
people = dict_people['people']
for person in people:
    print(person['name'] + "," + str(person['age']) + "," + person['city'])
print()


# prepare list for JSON, this can be sent via a browser
json_people = json.dumps(dict_people)
# the result is a JSON file:
print("JSON People")
# write some code to Print People from JSon
print(type(json_people))
print(json_people)
x = json.loads(json_people)
people = x['people']
for person in people:
    print(person['name'] + "," + str(person['age']) + "," + person['city'])
print()


# unwind people back to JSON
dict_people = json.loads(json_people)
print("Dictionary of people")
# write some code to Print People from Dictionary
print(type(dict_people))
unwind = json.loads(json_people)['people']
for person in unwind:
    print(person['name'] + "," + str(person['age']) + "," + person['city'])
print()

#this is what i tried doing first for the unwind section but it was just doing the same as the above section
#x = json.loads(json_people)
#people = x['people']
#for person in people:
#    print(person['name'] + "," + str(person['age']) + "," + person['city'])
#print()

