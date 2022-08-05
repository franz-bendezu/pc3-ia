def main_processes(pA, pB):
    tempS = F1(pA)
    tempQ = F2(pB)
    tempP = F3(tempS, tempQ)
    return tempP

def F1(pA):
    tempP = pA
    return tempP

def F2(pB):
    tempP = pB
    return tempP

def F3(pS, pQ):
    tempP = pS + pQ
    return tempP

if __name__ == '__main__':
    A = 1
    B = 2
    P = main_processes(A, B)
    print(P)
