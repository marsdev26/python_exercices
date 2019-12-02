
def rotate(l, n):
    return l[n:] + l[:n]

def get_substrings(s):
    for j in range(0, len(s)):
        for i in range(j+1, len(s)+1):
            yield s[j:i]

def get_values(matrix):
    transposed = [*zip(*matrix)]
    for i in range(len(matrix[0])):
        transposed[i] = rotate(transposed[i], -i)
    transposed = [*zip(*transposed)]
    for i, lst in enumerate(transposed, 1):
        yield from get_substrings(''.join(lst[:i]))
    for i, lst in enumerate(transposed, 1):
        yield from get_substrings(''.join(lst[i:]))

for v in get_values(matrix):
    print(v, end=' ')
