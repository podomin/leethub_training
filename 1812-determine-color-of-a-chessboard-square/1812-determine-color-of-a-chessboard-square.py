class Solution:
    def squareIsWhite(self, coordinates: str) -> bool:
        alphabet, number = coordinates
        if alphabet in "aceg":
            if number in "2468":
                return True
            else:
                return False
        else:
            if number in "2468":
                return False
            else:
                return True
