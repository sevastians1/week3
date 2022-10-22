import random
def bubble_swap1(sequence, swaps=0):
    for i in range(len(sequence)-1):
        current=i+1
        previous=i
        swaps +=1
        # iterations+=1
        # print(sequence[previous], sequence[current], sequence, "iterations", iterations)
        if sequence[current]<sequence[previous]:
            sequence[current],sequence[previous] = sequence[previous],sequence[current]
            bubble_swap(sequence, swaps)
            return
    print(f"Final result: {sequence}")
    print(f"Iterations: {swaps}")
    return sequence, swaps

def bubble_swap(sequence, iterations=0):
    swaps=0
    for i in range(len(sequence)-1):
        current=i+1
        previous=i
        iterations+=1
        print(sequence[previous], sequence[current], sequence, "iterations", iterations)
        if sequence[current]<sequence[previous]:
            sequence[current],sequence[previous] = sequence[previous],sequence[current]
            swaps+=1
    if swaps:
        bubble_swap(sequence, iterations)
        return
    print(f"Final result: {sequence}")
    print(f"Iterations: {iterations}")
    return sequence, iterations








sequence3=[]
for x in range(0, 63):
    sequence3.append(random.randint(0,1000))
placeholder=sequence3.copy()
sequence0 = [4, 3, 5, 0, 1]
sequence1=[7, 113, -2, 17, -9, 3]
sequence2=[11, 112, 12123, 1241, 346, 346, 4,4232, 34,5326, 4753, 34262624632342346, 36,643, 423,42346,263]
placeholder=sequence0.copy()
sequence4=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
# bubble_swap(sequence0)
# bubble_swap(sequence4)
# bubble_swap(sequence2)
bubble_swap1(sequence0)
bubble_swap(placeholder)




