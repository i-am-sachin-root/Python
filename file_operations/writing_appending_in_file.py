"""
w :- will create file if does no exist, and will overwrite if does exist """

file1 = open("D:\\Python\\Mihai\\Python\\file_operations\\test_write_append.txt", "w")
file1.write("writing in the file")
file1.seek(0)
print(file1.readlines())