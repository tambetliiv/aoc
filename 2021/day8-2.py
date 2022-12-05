import pprint

def check_segments(segment, check_segments):
    for check in check_segments:
        if check not in segment:
            return False
    return True

file = open("day8-input.txt", "r")

summa = 0
for line in file:
    mappings = {}
    segments = list(map(sorted, line.split("|")[0].split()))
    outputs = list(map(sorted, line.split("|")[1].split()))
    
    for segment in segments:
        if len(segment) == 2:
            mappings[1] = segment.copy()
            segments.remove(segment)
    for segment in segments:
        if len(segment) == 4:
            mappings[4] = segment.copy()
            segments.remove(segment)
    for segment in segments:
        if len(segment) == 3:
            mappings[7] = segment.copy()
            segments.remove(segment)
    for segment in segments:
        if len(segment) == 7:
            mappings[8] = segment.copy()
            segments.remove(segment)
    for segment in segments:
        if check_segments(segment, mappings[4]):
            mappings[9] = segment.copy()
            segments.remove(segment)
    for segment in segments:
        if len(segment) == 6 and check_segments(segment, mappings[1]):
            mappings[0] = segment.copy()
            segments.remove(segment)
    for segment in segments:
        if len(segment) == 6:
            mappings[6] = segment.copy()
            segments.remove(segment)
    for segment in segments:
        if check_segments(segment, mappings[1]):
            mappings[3] = segment.copy()
            segments.remove(segment)
    for segment in segments:
        if check_segments(mappings[9], segment):
            mappings[5] = segment.copy()
            segments.remove(segment)
    mappings[2] = segments[0]
    segments.remove(segments[0])

    answer = ""

    for output in outputs:
        for key, value in mappings.items():
            if output == value:
                answer += str(key)
    summa += int(answer)
file.close()

print(summa)

