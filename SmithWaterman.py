import itertools
import numpy as np

def matrix(a, b, target_score, match_score, gap_cost):
    H = np.zeros((len(a) + 1, len(b) + 1), np.float)

    for i, j in itertools.product(range(1, H.shape[0]), range(1, H.shape[1])):

        if a[i - 1] == b[j - 1]:
            match=H[i - 1, j - 1] + match_score
        else:
            match= H[i - 1, j - 1] + 0
        if a[i - 1] == b[j - 1] == "<target>":
            match= H[i - 1, j - 1] + (target_score - match_score)
        
        delete = H[i - 1, j] + gap_cost
        insert = H[i, j - 1] + gap_cost
        H[i, j] = max(match, delete, insert, 0)

    
    return H

def traceback(H, a, b):
    i,j = np.unravel_index(np.argmax(H, axis=None), H.shape)
    toklst = []
    print(a)
    toklst.append((a[i-1],b[j-1]))
    
    while i>1 and j>1:
        if H[i-1,j-1] > H[i,j-1]:
            if H[i-1,j-1] > H[i-1,j]:
                i = i - 1
                j = j - 1
                toklst.append((a[i-1],b[j-1]))
            else:
                i = i - 1
                toklst.append((a[i-1],'-'))
        else:
            if H[i,j-1] > H[i-1,j]:
                j = j - 1
                toklst.append(('-',b[j-1]))
            else:
                i = i - 1
                toklst.append((a[i-1],'-'))

    toklst.reverse()
    return toklst

            
def smith_waterman(a, b, target_score = 100, match_score = 1, gap_cost=-0.01):
    H = matrix(a, b, target_score, match_score, gap_cost)
    #print_scoring_matrix(H)
    toklst = traceback(H, a, b)
    return toklst

def print_scoring_matrix(H): 
    print("----Scoring Matrix----\n\n", H, "\n")
    
def print_base_tokens(toklst):
    base_tok = ""
    for tok in toklst:
        if tok[0] == tok[1]:
            base_tok = base_tok + tok[0]
            
    #print("----Base Tokens----\n\n", base_tok, "\n")
    return base_tok

