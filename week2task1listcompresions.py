
#Let's learn about list comprehensions! You are given three integers x,y,z and  representing the dimensions of a cuboid along with an integer n . Print a list of all possible coordinates given by  on a 3D grid where the sum of i+j+k  is not equal to . Here,0<=i<=x;0<=j<=y;0<=k<=z . Please use list comprehensions rather than multiple loops.


if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    ans=[]
    for i in range(x+1):
        for j in range(y+1):
          for k in range(z+1):
              if i+j+k!=n:
                  ans.append([i,j,k])
    print(ans)     

#Input (stdin)
#1
#1
#1
#2
#Your Output (stdout)
#[[0, 0, 0], [0, 0, 1], [0, 1, 0], [1, 0, 0], [1, 1, 1]]         
