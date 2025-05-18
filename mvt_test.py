import copy

LTUBES = 4
NTUBES = 3
MTEST = [['r','b','r','b'],['b','r','b','r'],[]]
M1 = [['r','y','r','r'],[]]
M1RES = [['r','y'],['r','r']]
M2 = [['r','y','r','r'],['y','r']]
M2RES = [['r','y'],['y','r','r','r']]
M3 = [['r','y','r','r'],['r','y','r']]
M3RES = [['r','y','r'],['r','y','r','r']]
MPLEIN = [['r','y','r','r'],['y','l','y','r']]

def test_uniform(m,t) :
    # doit retourner  si uniforme 0 ou 1 
    #  
    if len(m[t]) == 1:
        return True
    else:
        color = m[t][len(m[t])-1] 
        j=0
        while color == m[t][len(m[t])-1-j] :
            j += 1
            if len(m[t])-1-j ==-1:
                break
        if j== len(m[t]):
            return True 
        else:
            return False

def deplace(m,i,j,nb):
    # doit déplacer n balles de du tube i vers le tube j
    posi = len(m[i]) -1
    color = m[i][posi]
    n=copy.deepcopy(m)
    while nb > 0:
        n[i].pop()
        n[j].append(color)
        nb -=1    
    return n

def cherche_mvt(m):
    tmvt = []
    for t in range(NTUBES) :
        # ne pas toucher les tubes vides ou 
        #  les couleurs pleines uniformes
        if len(m[t]) == 0:
            #print('tube vide, on passe ',t)
            pass
        else :
            color = m[t][len(m[t]) - 1]
            ref = LTUBES * [m[t][len(m[t]) - 1]]
            if m[t] == ref:
                pass   # le tube est plein et uniforme, on n'y touche pas  
            else:
            # on cherche un tube avec cette couleur et place libre
                for u in range(NTUBES) :
                    if u==t:
                        pass
                    # si le tube est plein
                    elif  len(m[u]) == LTUBES:
                        pass
                    elif (len(m[u]) == 0) and test_uniform(m,t):
                        # on ne déplace pas 1 tube t uniforme  vers un tube vide
                        pass
                    elif (len(m[u])==0) or ((len(m[u]) < LTUBES) & ( m[u][len(m[u])-1] == color)):
                        # nombre de répétition de la couleur
                        k= 1
                        while m[t][len(m[t])-1 -k] == color:
                            if len(m[t])-1 -k >0:
                                k+=1
                            else:
                                break
                        place_libreu = LTUBES-len(m[u])
                        if k > place_libreu:
                            k= place_libreu
                        mvt=(t,u,k)
                        tmvt.append(mvt)              
    return tmvt

L1 = cherche_mvt(MTEST)
print('L1 ', L1)
    
