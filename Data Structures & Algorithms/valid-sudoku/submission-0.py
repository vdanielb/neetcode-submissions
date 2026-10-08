class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # idea: check sum of each row and col. First check row, then check by col
        target = 45
        col_dict = defaultdict(set)
        box_dict = defaultdict(set)
        for j,row in enumerate(board):
            row_seen = set()
            for i,val in enumerate(row):
                if val != ".":
                    if val not in row_seen:
                        row_seen.add(val)
                    else:
                        return False
                    
                    if val not in col_dict[i]:
                        col_dict[i].add(val)
                    else:
                        return False
                    
                    if val not in box_dict[(j//3, i//3)]:
                        box_dict[(j//3, i//3)].add(val)
                    else:
                        return False
        return True