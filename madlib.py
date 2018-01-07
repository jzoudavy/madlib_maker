import os
import random

#get which story we are doing:
storyNum = str(random.randint(1,5))
storyNum = '1'

word_not_submitted ='[Word Not Submitted]'

#template and list name
template_name='template'+storyNum+'.txt'
list_name='list'+storyNum+'.txt'

#print(template_name,' ',list_name)


word_list_key = []
word_list_value = []

with open(list_name) as f:
    for line in f:
        line = line.strip('\t\n')
        word_list_key.append(line)


for key in word_list_key:
    prompt= 'Need a '+key+':'
    text = input(prompt)
    word_list_value.append(text)

    

#print (word_list_key,' ',word_list_value)

with open(template_name) as f:
    filedata=f.read()

for value in word_list_value:
    filedata=filedata.replace(word_not_submitted,value,1)

output = open('output1.txt','w+')
output.write(filedata)



