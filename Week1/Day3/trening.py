# sample_dict = {
#          "student": "John" ,
#          "name": "Mike",
#          "marks": "Mark",
#          "physics":70,
#          "history":80
#           }
# a = sample_dict.get("history")
# print(a)
# # print(sample_dict["history"])



# sample_dict = { 
#    "class":{ 
#       "student":{ 
#          "name":"Mike",
#          "marks":{ 
#             "physics":70,
#             "history":80
#          }
#       }
#    }
# }
# print(sample_dict["class"]["student"]["marks"]["history"])

sample_dict = {
  "name": "Kelly",
  "age":25,
  "salary": 8000,
  "city": "New york"
}
# del sample_dict["name"]
# del sample_dict["salary"]

keys_to_remove = ["name", "salary", "weight"]
for key in keys_to_remove:
      if key in sample_dict:
        del sample_dict[key]

print(sample_dict)

