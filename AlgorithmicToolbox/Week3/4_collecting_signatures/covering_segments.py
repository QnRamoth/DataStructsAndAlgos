# Uses python3
import sys
from collections import namedtuple

Segment = namedtuple('Segment', 'start end')

def optimal_points(segments):
    points = []
    #write your code here
    leastLocalEnd = segments[0].end
    for s in segments:
        if(s.start > leastLocalEnd):
            points.append(leastLocalEnd)
            leastLocalEnd = s.end
            continue
        elif(s.end < leastLocalEnd):
            leastLocalEnd = s.end
    if(len(points) == 0 or points[-1] < leastLocalEnd):
        points.append(leastLocalEnd)
    return points

if __name__ == '__main__':
    inputs = input()
    n, *data = map(int, inputs.split())
    segments = list(map(lambda x: Segment(x[0], x[1]), zip(data[::2], data[1::2])))
    segments.sort()
    points = optimal_points(segments)
    print(len(points))
    for p in points:
        print(p, end=' ')
