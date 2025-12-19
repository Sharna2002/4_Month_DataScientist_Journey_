'''You have two dictionaries: defaults = {"theme":"light, "audio" : "on"}
and user_pref = {"theme": "dark"}. Merge them so user_pref override defaults'''

defaults = {"theme" : "light", "audio": "on"}

user_pref = {"theme" : "dark"}

print(defaults | user_pref)