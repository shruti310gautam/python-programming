#Given the names and grades for each student in a Physics class of N students, store them in a nested list and print the name(s) of any student(s) having the second #lowest grade.
#Note: If there are multiple students with the same grade, order their names alphabetically and print each name on a new line.

#Sample Input :
#5
#Harry
#37.21
#Berry
#37.21
#Tina
#37.2
#Akriti
#41
#Harsh
#39


students = sorted([[raw_input(), float(input())] for _ in range(int(input()))])
secndLow = sorted(list(set(score for [_, score] in students)))[1]
print ("\n".join( name for [name, score] in students if score == secndLow))


#Sample Output :

#Berry
#Harry

