sorted, counter
sorted_array = sorted(s, key=lambda x: (-c[x]), x)
counter x 로 1차 정렬, x 알파벳 순으로 2차 정렬
return "".join(sorted_array)