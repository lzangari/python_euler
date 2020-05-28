import numpy as np

series = '73167176531330624919225119674426574742355349194934969835203127745063262395783180169848018694788518438586156' \
         '0789112949495459501737958331952853208805511125406987471585238630507156932909632952274430435576689664895044524' \
         '45231617318564030987111217223831136222989342338030813533627661428280644448664523874930358907296290491560440' \
         '772390713810515859307960866701724271218839987979087922749219016997208880937766572733300105336788122023542180' \
         '97512545405947522435258490771167055601360483958644670632441572215539753697817977846174064955149290862569' \
         '32197846862248283972241375657056057490261407972968652414535100474821663704844031998900088952434506585412275' \
         '8866688116427171479924442928230863465674813919123162824586178664583591245665294765456828489128831426076900' \
         '42242190226710556263211111093705442175069416589604080719840385096245544436298123098787992724428490918884580' \
         '1561660979191338754992005240636899125607176060588611646710940507754100225698315520005593572972571636269561' \
         '882670428252483600823257530420752963450'



def getProduct(n):
    product = 1
    while (n != 0):
        product = product * (n % 10)
        n = n // 10
    return product


def largest_product_in_series(number):
    seri_product = []
    for i in range(len(number) - 13):
        seri_product.append(getProduct(int(number[i: i+13])))
    return np.max(seri_product)


largest_product_in_series(series)