inpt = """3-5
10-14
16-20
12-18

1
5
8
11
17
32"""

fresh = [(int(i.split("-")[0]), int(i.split("-")[1])) for i in inpt.split("\n\n")[0].split("\n")]
available = [(int(i.split("-")[0])) for i in inpt.split("\n\n")[1].split("\n")]


print(sum(1 for i in available if any(f[0] <= i <= f[1] for f in fresh)))

fresh = sorted(fresh)
interval_ranges = []
for f in fresh:
    f_queue = [f]
    while f_queue:
        l, r = f_queue.pop(0)
        partially_contained = False
        completely_contained = False
        for interval in interval_ranges:
            l_interval, r_interval = interval
            if l <= l_interval <= r_interval <= r:
                # Indeholder andet interval, skal splitte og tjekke enderne
                f_queue.append((l, l_interval - 1))
                f_queue.append((r_interval + 1, r))
                partially_contained = True
                break
            if l_interval <= l <= r <= r_interval:
                # Er helt indeholdt i et tidligere behandlet interval
                completely_contained = True
                break
            if l <= r_interval <= r:
                # Er delvist overlappende med øvre ende af et andet interval
                l = r_interval + 1
            if l <= l_interval <= r:
                # Er delvist overlappende med nedre ende af et andet interval
                r = l_interval - 1

        if partially_contained:
            continue
        if completely_contained:
            continue
        if l > r:
            continue

        interval_ranges.append((l, r))

print(sum(r - l + 1 for l, r in interval_ranges))
