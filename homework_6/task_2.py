var1 = 'Hello World'
var2 = 'Hello World2'
var3 = 'Hello World3'
var4 = 'Hello World4'

f = open('task_2.txt', 'w')
f.write(var1 + '\n' + var2)
f.close()

f = open('task_2.txt', 'a')
f.write('\n' + var3 + '\n' + var4)
f.close()
