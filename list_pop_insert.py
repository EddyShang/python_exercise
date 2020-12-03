#
# method pop usage example
#assume there is a list of cisco switch models
cisco_switch_models=['2960','3560','3750','3850','4500','6500','7600','9300','9400']
print cisco_switch_models
rm_item=raw_input("Which switch model do you want to remove from the list? ")
cisco_switch_models.pop(cisco_switch_models.index(rm_item))
print("Done! "+rm_item+" has been removed from the model list")
print cisco_switch_models
add_item=raw_input("Please enter the switch model you want to add to the list: ")
add_place=int(raw_input("Please enter the position you want the model to be in the list: "))
cisco_switch_models.insert(add_place, add_item)
print cisco_switch_models

raw_input()
