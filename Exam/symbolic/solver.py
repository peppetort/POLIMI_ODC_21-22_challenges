import z3

FLAG = "flag{bet_u_d1dn't_r3ally_n33d_th4t_l1cen5e_right?}"
 
n = 5
def repeated_entry(vector, solver):
    print(vector)
    for i in range(5):
        for j in range(5):
            if i!=j :
                solver.add(vector[i] != vector[j])

def activation_check(entries, solver):

    matrix = [[0] * 5 for _ in range(5)]

    for i in range(5):
        for j in range(5):
            matrix[i][j] = entries[i][j]

    for i in range(n):
        vector = [matrix[i][j] for j in range(n)]
        repeated_entry(vector, solver)

    for j in range(n):
        vector = [matrix[i][j] for i in range(n)]
        repeated_entry(vector, solver)

    vector = [matrix[i][i] for i in range(n)]
    repeated_entry(vector, solver)

    vector = [matrix[i][n-1-i] for i in range(n)]
    repeated_entry(vector, solver)


matrix = [[z3.Int('c%d' % (int(str(j) + str(i))))  for i in range(5)] for j in range(5)]
solver = z3.Solver()
for i in range(5):
    for j in range(5):
        solver.add(z3.And(matrix[i][j] >= 49, matrix[i][j] <= 53))

activation_check(matrix, solver)
sum__ = z3.Int('sum')
for i in range(5):
    for j in range(5):
        sum__ += matrix[i][j]
solver.add(sum__ % 96 == 75)

print(solver.check())
m = solver.model()
print(matrix)
result = ""
for i in range(5):
    for j in range(5):
        print(m.eval(matrix[i][j]), ",")

res = [50 ,
51 ,
53 ,
52 ,
49 ,
49 ,
53 ,
52 ,
50 ,
51 ,
52 ,
49 ,
51 ,
53 ,
50 ,
51 ,
52 ,
50 ,
49 ,
53 ,
53 ,
50 ,
49 ,
51 ,
52]

result = ""
count = 0
for i in res:
    result += chr(i)
    count +=1
    if count == 5:
        result += "-"
        count = 0
print(result)