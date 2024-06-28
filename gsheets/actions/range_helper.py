from st2common.runners.base_action import Action
import math

class Get(Action):
    def run(self, row, column):
        row += 1
        column_name_len = 0
        temp = column
        start = 0
        while temp > 0:
            column_name_len+=1
            temp -= 26 ** column_name_len
            if temp > 0:
                start += 26 ** column_name_len
        letter_idx = []
        column = column - start
        if column == 0:
            letter_idx = [0]
        else:
            while column > 0:
                letter_idx.append(int(column % 26))
                column = column // 26
        letter_idx.reverse()
        return "".join([chr(ord('A') + x) for x in letter_idx]) + str(row)