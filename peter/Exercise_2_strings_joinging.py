# learn how to create strings

name = 'Name'
Number = 30
Endung = 'txt'

string_name = name + '%0.4d' %Number + '.' + Endung
string_name2 = name + str(Number) + '.' + Endung
print(string_name)