import bisect
class TimeMap:

    def __init__(self):
        self.timestamps: defaultdict[str, list[tuple[int, str]]] = defaultdict(list) 
        
    def set(self, key: str, value: str, timestamp: int) -> None:
        self.timestamps[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        pairs = self.timestamps.get(key, [])
        i = bisect.bisect_left(pairs, timestamp, key=lambda p: p[0])
        if i < len(pairs) and pairs[i][0] == timestamp:
            return pairs[i][1]
        if i == 0:
            return ""
        return pairs[i - 1][1]
            
        
        
