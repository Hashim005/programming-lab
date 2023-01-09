
# program to copy odd line of one file to  another
# open file writing and writing data

input_file = open('myfile.txt')
output_file =  open('writedata.txt', 'w')

# copy content from read_file to copy_data
copy_data = input_file.readlines()
print("\nactual file content is")
print(copy_data, "\n")

for i in range (0,len(copy_data)):
    if i % 2 == 0:
        output_file.write(copy_data[i])
    else:
        pass


# closing file after writing
output_file.close()

# open write file in read mode and printing values
output_file = open('writedata.txt', 'r')

print("odd lines are:")
print(output_file.read())

# close files
input_file.close()
output_file.close()