file1 = open('output.txt','w')
writing_file = file1.write(input('Enter text to write to the file : ')+'\n')
print('Data successfully written to output.txt. \n')
file1.close()

file1 = open('output.txt','a')
appending_file = file1.write(input('enter additional text to append : ')+'\n')
print('data succesfully appended \n')
file1.close()

file1 = open('output.txt','r')
print('final content of output.txt: ')
reading_file = file1.read()
print(reading_file)
file1.close()







