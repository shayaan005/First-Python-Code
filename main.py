#List of invited people
Invited=['Nelson Mandela','Bruce Wayne','Grandfather']
#Sending out invites to the invited guests
print('Hello ' + Invited[0] + ', ' + "I would like to formally invite you to my thanksgiving dinner this Saturday. I hope you can make it.")
print('Hello ' + Invited[1] + ', ' + "I would like to formally invite you to my thanksgiving dinner this Saturday. I hope you can make it.")
print('Hello ' + Invited[2] + ', ' + "I would like to formally invite you to my thanksgiving dinner this Saturday. I hope you can make it.")
print('Bruce Wayne')
#Removing the guest who is not coming
del Invited[1]
Invited.insert(0, 'Shawn Michaels')
#Sending out new invites
print('Hello ' + Invited[0] + ', ' + 'I would like to formally invite you to my thanksgiving dinner this Saturday. I hope you can make it.')
print('Hello ' + Invited[1] + ', ' + 'I would like to formally invite you to my thanksgiving dinner this Saturday. I hope you can make it.')
print('Hello ' + Invited[2] + ', ' + 'I would like to formally invite you to my thanksgiving dinner this Saturday.')
#Informing people about the new discovery
print('Folks, I\'ve just discovered an even larger dining table.')
#Adding more guests
Invited.insert(0,'Adolf Hitler')
Invited.insert(2,'Lord Darkseid')
Invited.append('Tifa Lockhart')
#inviting the new guests
print('Hello ' + Invited[3] + ', ' + 'I would like to formally invite you to my thanksgiving dinner this Saturday. I hope you can make it.')
print('Hello ' + Invited[5] + ', ' + 'I would like to formally invite you to my thanksgiving dinner this Saturday. I hope you can make it.')
print('Hello ' + Invited[0] + ', ' + 'I would like to formally invite you to my thanksgiving dinner this Saturday. I hope you can make it.')
print('Hello ' + Invited[1] + ', ' + 'I would like to formally invite you to my thanksgiving dinner this Saturday. I hope you can make it.')
print('Hello ' + Invited[2] + ', ' + 'I would like to formally invite you to my thanksgiving dinner this Saturday.')
print(Invited)
#Informing the guests about a change in events
print('Folks, I apologize but it looks like I can only invite two people')
print(Invited)
removed_name= Invited.pop(0)
print('I\'m sorry,' + removed_name + ' but you can\'t come anymore')
removed_name=Invited.pop((2))
print('I\'m sorry,' + removed_name + ' but you can\'t come anymore')
removed_name= Invited.pop(1)
print('I\'m sorry,' + removed_name + ' but you can\'t come anymore')
removed_name= Invited.pop(1)
print('I\'m sorry,' + removed_name + ' but you can\'t come anymore')
print(Invited)
#Letting two people know they're still invited
print(Invited[0] + ',' + ' you are still invited to the party.')
print(Invited[1] + ',' + ' you are still invited to the party')
#Deleting the remaining guests from the list
del Invited[0]
del Invited[0]
print(Invited)