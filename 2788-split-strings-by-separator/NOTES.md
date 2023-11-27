if split_word:
answer.append(split_word)
한 줄로도 가능
for word in words:
[x for x in word.split(separator) if x]
return answer