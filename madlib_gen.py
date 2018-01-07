import os
import random
import nytimes_get

#get nytimes story full text


#determine words that's longer then 5 char to replace
#determine their type
#replace them with words_not_submitted
#add their type to a list
#ask user to input list
#print out new story with user input list



def main():
    


if __name__ == '__main__':
    main()
    









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



