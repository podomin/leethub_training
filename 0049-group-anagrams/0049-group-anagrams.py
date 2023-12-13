class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # 딕셔너리 사용
        # key: 알파벳 순으로 정렬한 문자열
        # value: 해당하는 문자 리스트
        answer = []
        d = defaultdict(list)
        for s in strs:
            print("".join(sorted(s)))
            d["".join(sorted(s))].append(s)
        #print(d)
        #print(d.values())
        return list(d.values())


        