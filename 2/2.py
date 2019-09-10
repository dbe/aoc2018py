def run(lines):
    for i in range(0, len(lines)):
        for j in range(i + 1, len(lines)):
            if(hamming_distance(lines[i], lines[j]) == 1):
                common = [a if a == b else '' for a, b in zip(lines[i], lines[j])]
                return ''.join(common)

def hamming_distance(a, b):
    d = 0
    
    for e1, e2 in zip(a, b):
        d += 1 if e1 != e2 else 0

    return d
