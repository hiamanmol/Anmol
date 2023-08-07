contacts =[
    {
        "names": "Anmol",
        "phone no": "99999 11111",
        "conversation": [
                        "hi",
                         "whatsapp"
        ]
    },
    {
        "names": "Abhi",
        "phone no": "99999 11111",
        "conversation": [
                        "hi",
                         "kaise ho"
        ]
    },
    {
        "names": "Sam",
        "phone no": "99999 11111",
        "conversation": [
                        "hi",
                         "there"
        ]
    }
]
# print(contacts)

search_keyword = input("Enter keyword to search:")
print("search keyword", search_keyword)

for contacts in contacts:
    # if contacts ["name"].lower().startswith(search_keyword.lower()):
    # if contacts ["name"].lower().__contains__(search_keyword.lower()):
    if contacts["names"].lower().find(search_keyword.lower()) >= 0\
          or contacts["phone"].find(search_keyword) >= 0:
        print(contacts)
        print("************************")
