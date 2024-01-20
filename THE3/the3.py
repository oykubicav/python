def pattern_search(P, I):
    N = len(P)
    M = len(P[0])
    H = len(I)
    W = len(I[0])
    for i in range(H-N+1):
        for j in range(W-M+1):
            if check_pattern(P,I,i,j):
                return (i,j,0)
                
            elif check_pattern(rotate270_matris(rotate270_matris(rotate270_matris(P))),I,i,j):
                return(i,j,90)
                

            elif check_pattern(rotate270_matris(P),I,i,j):
                return(i,j,270)
                
            elif check_pattern(rotate270_matris(rotate270_matris(P)),I,i,j):
                return(i,j,180)
                

          
    return False

def check_pattern(P,I,i,j):
    N,M = len(P), len(P[0])
    x=True
    for k in range(N):
        for l in range(M):
            if P[k][l] != I[i+k][j+l]:
                x=False
    return x

def rotate270_matris(P):
  return[[P[l][k] for l in range(len(P))] for k in range(len(P[0])-1,-1,-1)]








