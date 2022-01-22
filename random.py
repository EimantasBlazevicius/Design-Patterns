def sum_of_intervals(intervals):
    mushed_intervals = []
    if len(intervals) == 1:
        return intervals[0][1]-intervals[0][0]
    else:
        for inter in intervals:
            for every in intervals:
                if (list(inter)[0] in range(every)) or (list(inter)[1] in range(every)):
                    new_set = (min(inter[0], every[0]), max(inter[1], every[1]))
                    intervals.remove(every)
                    mushed_intervals.append(new_set)
    print(intervals)
    print(mushed_intervals)