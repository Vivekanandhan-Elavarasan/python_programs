def bubbleSort(nlist):
    for passnum in range(len(nlist)-1,0,-1):
        for i in range(passnum):
            if nlist[i]>nlist[i+1]:
                temp = nlist[i]
                nlist[i] = nlist[i+1]
                nlist[i+1] = temp

nlist = [14,46,43,27,57,41,45,21,70]
bubbleSort(nlist)
print(nlist)

a=[3, 1, 4, 2, 5] 
for i in a: 
       print (i**2,end=" ")


l3 = [ (105, "d"), (21, "z"), (0, "v") ]
for j in l3:
    print (j[0],j[1],end=" ")

l = [ { "color": "red", "value": "#f00" }, {"color": "green", "value": "#0f0" }, {"color": "blue", "value": "#00f"} ]

for i in l:
     print (i['value'])

for i in l:
    if(i['color']=="green"):
             print (i['value'])

for x in l:
    print(list(x.values())[1])

# Print the languages that are inferior to Python
py = {'Python': 'Rocks', 'inferior': ['java', 'cobol']}

print(py['inferior'])

# Print my Bill
prices = {'apple': 0.40, 'banana': 0.50}
my_purchase = {
    'apple': 1,
    'banana': 6}

print(str(my_purchase['apple']*prices['apple'] +
          my_purchase['banana']*prices['banana']))


# print the roles
junk = {
    "characters": {
        "Lonestar": {
            "id": 55923,
            "role": "renegade",
            "items": [
                "space winnebago",
                "leather jacket"
            ]
        },
        "Barfolomew": {
            "id": 55924,
            "role": "mawg",
            "items": [
                "peanut butter jar",
                "waggy tail"
            ]
        },
        "Dark Helmet": {
            "id": 99999,
            "role": "Good is dumb",
            "items": [
                "Shwartz",
                "helmet"
            ]
        },
        "Skroob": {
            "id": 12345,
            "role": "Spaceballs CEO",
            "items": [
                "luggage"
            ]
        }
    }
}

for chara in list(junk['characters'].values()):
    print(chara['role'])


omg = {2: [1, 2, 3], 'a': {'b': {'c': {'d': {'e': [1, 2, 3]}}}}}
# Get the first array value for the key 2

print(omg[2][0])

# Print all the array value for the key 2
print(omg[2])

# Print value of key 'a','b','c','d','e'

print(omg['a'])
print(omg['a']['b'])
print(omg['a']['b']['c'])
print(omg['a']['b']['c']['d'])
print(omg['a']['b']['c']['d']['e'])


# Print the sum of the array with key 'e'

print(sum(omg['a']['b']['c']['d']['e']))

# set value of key 'e' to ['Chera','Chola','Pandiya']

omg['a']['b']['c']['d']['e'] = ['Chera', 'Chola', 'Pandiya']
print(omg['a']['b']['c']['d']['e'])

# Get the value Mats from the Dict
body = {
    'query': {
        'filtered': {
            'query': {
                'match': {'description': 'addictive'}
            },
            'filter': {
                'term': {'created_by': 'Mats'}
            }
        }
    }
}

print(body['query']['filtered']['filter']['term']['created_by'])

# Modify the below statement to print Mats

print(body['query']['filtered']['filter']['term']['created_by'])

# print the IMDB star rating ( 6.7)
# print the length of the movie
movie_box = {
    "Robin Hood: Men in Tights": {
        "imdb_stars": 6.7,
        "length": 104,
        "stars": [{"name": "Cary Elwes", "imdb": "nm0000144", "role": "RobinHood"},
                  {"name": "Richard Lewis", "imdb": "nm0507659", "role": "PrinceJohn"}]
    }
}
print(movie_box["Robin Hood: Men in Tights"]['imdb_stars'],
      movie_box["Robin Hood: Men in Tights"]['length'])