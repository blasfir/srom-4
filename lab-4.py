# Варіант 5, m (розмірність поля) = 233
import time
import numpy

m = 233
p = 2 * m + 1

def toTheSameLength(A, B):
    if len(A) < len(B):
        A = [0] * (len(B) - len(A)) + A
    if len(A) > len(B):
        B = [0] * (len(A) - len(B)) + B
    return A, B  

def deleteExtraZeros(A):
    while A and A[0] == 0:
        A.pop(0)
    if not A:
        return [0]
    return A

def stringToArray(n):
    result = result = list(map(int, n))
    result = deleteExtraZeros(result)
    return result

def arrayToString(n):
    while len(n) > m:
        n.pop(0)
    n = list(map(str, n))
    while len(n) < m:
        n = ['0'] + n
    result = ''.join(n)    
    return result

def fixLength(A):
    A = list(A)
    if len(A) > m:
        return A[:m]  
    elif len(A) < m:
        return [0] * (m - len(A)) + A
    return A

def isThisAPrimeNumber():
    if p <= 1:
        return False  
    for i in range(2, int(p ** 0.5) + 1):
        if p % i == 0:
            return False  
    return True

def isThereAOnb():
    isPAPrimeNumber = isThisAPrimeNumber()
    if isPAPrimeNumber == False:
            return False
    for i in range(1, p):
        if pow(2, i, p) == 1: 
            if i == 2 * m or (i == m and p % 4 == 3):
                return True
            else:
                break 
    return False

def onbAdd(A, B):
    result = []
    for i in range(len(A)):
        k = int(A[i]) + int(B[i])
        n = k % 2
        result.append(n)
    result = deleteExtraZeros(result)    
    return result

def onbTrace(A):
    result = stringToArray(str(sum(A) % 2))
    return result

def onbFindZero(A):
    result = onbAdd(A, A)
    return result

def onbSquarePower(A):
    A = numpy.array(A)
    result = numpy.roll(A, 1)
    result = result.tolist()
    return result

def addMatrix():
    matrix = [[0] * m for i in range(m)]
    for i in range(m):
        k = 2 ** i
        for j in range(m):
            e = 2 ** j
            s1 = (k + e) % p
            s2 = (k - e) % p
            s3 = (e - k) % p
            s4 = (- e - k) % p
            if 1 in (s1, s2, s3, s4):
                matrix[i][j] = 1
    return matrix            

def onbMul(A, B):
    A = numpy.array(A)
    B = numpy.array(B)
    matrix = numpy.array(addMatrix())
    A1 = numpy.zeros((m, m), dtype=int)
    B1 = numpy.zeros((m, m), dtype=int)
    for i in range(m):
        A1[i] = numpy.roll(A, -i)
        B1[i] = numpy.roll(B, -i)
    TB1 = B1.T  
    A1MTB1 =  A1 @ matrix @ TB1 
    result = A1MTB1.diagonal() % 2
    result = result.tolist()
    return result

def onbPower(A, B):
    B = B[::-1]
    result = [1] * m
    for i in B:
        if i == 1:
            result = onbMul(result, A)
        A = onbSquarePower(A)
    return result

def onbInverseElement(A):
    k = bin(2**m - 2)[2:]
    k = stringToArray(k)
    result = onbPower(A, k)
    return result

def onbFindOne(A):
    if A == [0]:
         raise Exception('Error')
    A1 = onbInverseElement(A)
    result = onbMul(A, A1)
    return result

f = '10011011110110001011101001001010100110010000100110101101101011101110101010011110001110011010011101010111111010001010111101101101110110001100011010010011111111001111000001011101010001110110111100110101011100101110101010011100010101011'
g = '10101101110111111101111110100011001100100111110110010010101111111110111000010011111111101110010110010111000010110010001101001010101001011011110101000110001001110101111101010100100101011010000011101010011011000001011010111001000010001'
#h = '10101001011010010000000001001101111100001111001101000010100010000001011000101110100000000000000000011111001111000100000110010111110001110101000011111111011101101001101101111010000001101100000110001111110011101010110011010111000100010'
ff = stringToArray(f)
gg = stringToArray(g)
#hh = stringToArray(h)
#print(isThereAOnb())
#print(onbAdd(ff, gg))
#print(onbTrace(ff))
#print(onbFindZero(ff))
#print(onbSquarePower(ff))
#print(addMatrix())
#print(onbMul(ff, gg))
#print(onbPower(ff, gg))
#print(onbInverseElement(ff))
#print(onbFindOne(ff))
print()
print('onbFindZero: ' + arrayToString(onbFindZero(ff)))
print()
print('onbFindOne: ' + arrayToString(onbFindOne(ff)))
print()
print('onbAdd: ' + arrayToString(onbAdd(gg, ff)))
print()
print('onbMul: ' + arrayToString(onbMul(gg, ff)))
print()
print('onbTrace: ' + arrayToString(onbTrace(ff)))
print()
print('onbSquarePower: ' + arrayToString(onbSquarePower(ff)))
print()
print('onbPower: ' + arrayToString(onbPower(ff, gg)))
print()
print('onbInverseElement: ' + arrayToString(onbInverseElement(ff)))
'''
sumGF = fixLength(onbAdd(gg, ff))
sumGFmulH = fixLength(onbMul(sumGF, hh))
mulHsumGF = fixLength(onbMul(hh, sumGF))
mulGH = fixLength(onbMul(gg, hh))
mulFH = fixLength(onbMul(ff, hh))
sumMulGHmulFH = fixLength(onbAdd(mulGH, mulFH))
if sumMulGHmulFH == mulHsumGF == sumGFmulH:
    print('Success')
else:
    print('Error')

power = stringToArray(bin(2**m - 1)[2:])
fToPower = onbPower(ff, power)
while len(fToPower) > 1:
        fToPower.pop(0)
if fToPower == [1]:
    print('Success')
else:
    print('Error')

def timeSearch(f, *args, repeats=5):
    start = time.perf_counter()
    for _ in range(repeats):
        f(*args)
    end = time.perf_counter()
    avg_time = (end - start) / repeats
    return avg_time  

avg = timeSearch(onbFindZero, ff)
print(f"Середній час роботи onbFindZero: {avg:.10f} сек")
avg1 = timeSearch(onbFindOne, ff)
print(f"Середній час роботи onbFindOne: {avg1:.10f} сек")
avg2 = timeSearch(onbAdd, gg, ff)
print(f"Середній час роботи onbAdd: {avg2:.10f} сек")
avg3 = timeSearch(onbMul, gg, ff)
print(f"Середній час роботи onbMul: {avg3:.10f} сек")
avg4 = timeSearch(onbTrace, gg)
print(f"Середній час роботи onbTrace: {avg4:.10f} сек")
avg5 = timeSearch(onbSquarePower, gg)
print(f"Середній час роботи onbSquarePower: {avg5:.10f} сек")
avg6 = timeSearch(onbPower, gg, ff)
print(f"Середній час роботи onbPower: {avg6:.10f} сек")
avg7 = timeSearch(onbInverseElement, gg)
print(f"Середній час роботи onbInverseElement: {avg7:.10f} сек")
avg8 = timeSearch(stringToArray, g)
print(f"Середній час роботи stringToArray: {avg8:.10f} сек")
avg9 = timeSearch(arrayToString, gg)
print(f"Середній час роботи arrayToString: {avg9:.10f} сек")'''