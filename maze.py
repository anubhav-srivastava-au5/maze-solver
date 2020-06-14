
# ----------------------------------INPUT----------------------------------

input_file = open("inputfile.txt","w")
input_file.write(input())
input_file.close()

input_file = open("inputfile.txt","r")
N = input_file.readline()
input_file.close()

input_file = open("inputfile.txt","a")
input_file.write('\n')
for i in range(int(N)):
    input_file.write(input())
    input_file.write('\n')

input_file = open("inputfile.txt","r")
input_matrix = []
N = int(N)
for i in range(N+1):
    line = input_file.readline()
    if i > 0: input_matrix.append(list(map(int, line.rstrip().split())))
input_file.close()

# -------------------------------CODE-------------------------------------

def isSafe( maze, x, y ): 
      
    if x >= 0 and x < N and y >= 0 and y < N and maze[x][y] == 1: 
        return True
      
    return False

def solveMaze( maze ): 

    sol = [ [ 0 for j in range(N) ] for i in range(N) ] 
      
    if solveMazeUtil(maze, 0, 0, sol) == False:  
        return "-1"
    return sol 


def solveMazeUtil(maze, x, y, sol): 

    if x == N - 1 and y == N - 1 and maze[x][y]== 1: 
        sol[x][y] = 1
        return True

    if isSafe(maze, x, y) == True: 
        sol[x][y] = 1

        if solveMazeUtil(maze, x + 1, y, sol) == True: 
            return True

        if solveMazeUtil(maze, x, y + 1, sol) == True: 
            return True

        sol[x][y] = 0
        return False

# --------------------OUTPUT----------------------------------
temp_list=solveMaze(input_matrix)
output_file = open("outputfile.txt","w")

if type(temp_list) is list:
    for i in temp_list: 
        for j in i: 
            output_file.write(str(j))
            output_file.write(" ")

        
        output_file.write("\n")
    output_file.close()  

else: 
    output_file.write(str(temp_list))
    output_file.close()
