
# sort the states in order by the length of the first city name.
# Here, it’s pretty easy to compute that property.
# states[state] is the list of cities associated with a particular state.
# So If state is a list of city strings, len(states[state][0]) is the length of the first city name.
# Thus, we can use a lambda expression:

states = {"Minnesota": ["St. Paul", "Minneapolis", "Saint Cloud", "Stillwater"],
          "Michigan": ["Ann Arbor", "Traverse City", "Lansing", "Kalamazoo"],
          "Washington": ["Seattle", "Tacoma", "Olympia", "Vancouver"]}

print(sorted(states, key=lambda state: len(states[state][0])))

#
# For our second sort order, the property we want to sort by is the number of cities
# that begin with the letter ‘S’. The function defining this property is harder to express,
# requiring a filter and count accumulation pattern. So we are better off defining a separate,
# named function. Here, we’ve chosen to make a lambda expression that looks up the value
#  associated with the particular state and pass that value to the named function s_cities_count.
# We could have passed just the key, but then the function would have to look up the value,
# and it would be a little confusing, from the code, to figure out what dictionary the key is
# supposed to be looked up in. Here, we’ve done the lookup right in the lambda expression,
# which makes it a little bit clearer that we’re just sorting the keys of the states dictionary
# based on a property of their values. It also makes it easier to reuse the counting function
# on other city lists, even if they aren’t embedded in that particular states dictionary.

def s_cities_count(city_list):
    ct = 0
    for city in city_list:
        if city[0] == "S":
            ct += 1
    return ct

def s_cities_count_for_state(state):
    city_list=states[state]
    return s_cities_count(city_list)

states = {"Minnesota": ["St. Paul", "Minneapolis", "Saint Cloud", "Stillwater"],
          "Michigan": ["Ann Arbor", "Traverse City", "Lansing", "Kalamazoo"],
          "Washington": ["Seattle", "Tacoma", "Olympia", "Vancouver"]}

print(sorted(states, key=lambda state: s_cities_count(states[state])))
#cleaner use
print(sorted(states, key=s_cities_count_for_state))
