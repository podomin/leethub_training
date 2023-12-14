class Solution:
    def circularGameLosers(self, n: int, k: int) -> List[int]:
        # 한 번이라도 폭탄을 받은 친구들
        visited = set() 
        #현재 폭탄 위치
        cur_loc = 0
        visited.add(cur_loc)
        cnt = 0  
        while True:
            print("visited", visited, "cur_loc", cur_loc)
            cnt += 1
            next_loc = (cur_loc + cnt *k) % n
            if next_loc in visited:
                break
            print("cur_loc", cur_loc, "move", cnt*k, "next_loc", next_loc)
            cur_loc = next_loc
            # 방문한위치는 visited에 추가하고
            visited.add(cur_loc)
            # next_loc이 visited 안에 포함되어 있다면 break
        return [x+1 for x in range(n) if x not in visited]
        