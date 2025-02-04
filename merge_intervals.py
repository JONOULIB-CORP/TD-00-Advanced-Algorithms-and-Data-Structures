# Merge Intervals Implementation
def merge_intervals(intervals):
    if not intervals:
        return []
    intervals.sort(key=lambda x: x[0])
    merged = [intervals[0]]
    for current in intervals[1:]:
        last = merged[-1]
        if current[0] <= last[1]:
            merged[-1] = (last[0], max(last[1], current[1]))
        else:
            merged.append(current)
    return merged

# Test Case
if __name__ == "__main__":
    intervals = [(1, 3), (2, 6), (8, 10), (15, 18)]
    merged = merge_intervals(intervals)
    print("Merged Intervals:", merged)