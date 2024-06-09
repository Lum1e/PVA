def find_intervals_with_same_sum(sequence):
    n = len(sequence)
    sum_intervals = {}  # slovník pro uložení součtů a intervalů, které k nim patří

    # Generovat všechny intervaly délky alespoň 2
    for start in range(n):
        for end in range(start + 1, n):
            interval_sum = sum(sequence[start:end + 1])
            if interval_sum not in sum_intervals:
                sum_intervals[interval_sum] = []
            sum_intervals[interval_sum].append((start, end))
    
    # Počítat počet dvojic různých intervalů se stejným součtem
    count_pairs = 0
    for intervals in sum_intervals.values():
        if len(intervals) > 1:
            count_pairs += len(intervals) * (len(intervals) - 1) // 2

    return count_pairs

# Příkladová posloupnost
sequence = [1, 5, 2, 4, 2, 2, 2]
result = find_intervals_with_same_sum(sequence)
print("Počet dvojic různých intervalů se stejným součtem je:", result)
