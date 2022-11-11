def truckTour(petrolpumps):
    # Write your code here
    n = len(petrolpumps)
    for i in range(n):
        step = i
        step_counter, capacity, dist = 0, 0, 0
        while step_counter != n:
            capacity += petrolpumps[step][0]
            dist = petrolpumps[step][1]
            if capacity - dist >= 0:
                capacity = capacity - dist
                step = step + 1 if (step + 1) < n else 0
                step_counter += 1
            else:
                break
        if step_counter == n:
            return i


petrolpumps = [[1, 5],
               [10, 3],
               [3, 4]]

print(truckTour(petrolpumps))
