def all_even_digits():
    results = []
    for n in range(1000, 3001):
        digits = [int(d) for d in str(n)]
        if all(d % 2 == 0 for d in digits):
            results.append(str(n))
    
    print(",".join(results))
