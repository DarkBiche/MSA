import itertools
import numpy as np
import SmithWaterman as sw
import FileParser as fp

#GLOBAL VARIABLE:
msa = []

def find_msa(msa, base_tok, toklst):
    if len(msa) == 0:
        return None

    res = None
    for m in msa:
        if(m[2]==base_tok):
            res = True
            buffer1=[]
            buffer2=[]
            for tok in toklst:
                buffer1.append(tok[0])
                buffer2.append(tok[1])

            m[1] = m[1] + 2
            m.append(buffer1)
            m.append(buffer2)

    return res

def create_new_msa(toklst,base_tok):
    m = []
    m.append(len(toklst))
    m.append(2)
    m.append(base_tok)
    for i in range(0,5):
        m.append([])
    
    y=0
    for i in range(0,len(toklst)):
        m[3].append(i)
        if toklst[i][0] == toklst[i][1]:
            m[4].append(y)
            m[5].append(None)
            y=y+1
        else:
            m[4].append(None)
            if toklst[i][0] == '-' or toklst[i][1] == '-':
                m[5].append('+')
            else:
                m[5].append('~')
        m[6].append(toklst[i][0])
        m[7].append(toklst[i][1])
                
    return m

def process_msa(sentences,i):
    a = sentences[i]
    b = sentences[i+1]
    toklst = sw.smith_waterman(a, b)
    base_tok = sw.print_base_tokens(toklst)
    m = find_msa(msa, base_tok, toklst)
    if(m == None):
        m = create_new_msa(toklst,base_tok)
        msa.append(m)
    
def generate_msa_from_file(file):
    sentences = fp.parsing_file(file)
    s = len(sentences)
    for i in range(0,s - s%2,2):
        process_msa(sentences,i)
    if s%2:
        i=i+1
        process_msa(sentences,i)

    print_msa()

def print_msa():
    for m in msa:
        print("Size = ", m[0])
        print("Token Size Max = ", m[1])
        print("Base Token: ", m[2])
        print("----------------------")
        for i in range(3,len(m)):
            print(m[i])
        print("----------------------")
        
generate_msa_from_file("examples/example3.ttg")

#a, b = ["there", "is", "a", "large", "mass", "seen", "in", "the", "<target>"], ["a", "mass", "in", "the", "<target>", "is", "seen"]
#print(sw.smith_waterman(a, b))

 
