class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        stops = {}
        for t in trips:
            people = t[0]
            for stop in range(t[1], t[2]):
                if stop in stops:
                    stops[stop] += people
                else:
                    stops[stop] = people
        maxKey = max(stops, key=stops.get)
        return stops[maxKey] <= capacity
