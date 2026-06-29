import time

def generate_ascent_sequences(n):
    """Generate all valid ascent sequences of length n including [0,1,0,1,3]"""
    if n == 0:
        yield []
        return

    def helper(sequence, num_ascents):
        if len(sequence) == n:
            yield sequence
            return

        # The next element can be anything from 0 to num_ascents + 1
        for x in range(0, num_ascents + 2):
            new_sequence = sequence + [x]

            # Calculate new number of ascents
            new_ascents = num_ascents
            if len(sequence) > 0 and sequence[-1] < x:
                new_ascents += 1

            yield from helper(new_sequence, new_ascents)

    yield from helper([0], 0)

def sequence_to_intervals(seq):
    return [[a_i, i - 1] for i, a_i in enumerate(seq, start=1)]

n = 4
start = time.time()
count = 0
for idx, seq in enumerate(generate_ascent_sequences(n), 1):
    intervals = sequence_to_intervals(seq)
    count += 1
    print(f"{idx:02d}:  {seq}  →  Intervalles: {intervals}")
end = time.time()
print(f"{n} - {count} - {end - start:.4f} seconds")