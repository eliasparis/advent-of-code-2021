# Part 1: Start by finding the sum of all unmarked numbers on that board; in this case, the sum is 188.
# Then, multiply that sum by the number that was just called when the board won, 24, to get the final score
# !!! This one could be accomplished by flattening the list and work on board-based slices
# But felt lazy for refactor

import json
f = open('input.json')
data = json.load(f)
numbers = data['numbers']
boards = data['boards']

winning_board = None
last_number = None

for number in numbers:
    if winning_board:
        break
    last_number = number
    for i, board in enumerate(boards):

        if winning_board:
            break

        for ii, row in enumerate(board):

            if winning_board:
                break

            for iii, rownumber in enumerate(row):
                if rownumber == number:
                    boards[i][ii][iii] = None
                    row_wins = not(any(row))

                    column = list()
                    for row2 in board:
                        column.append(row2[iii])
                    column_wins = not(any(column))

                    if column_wins | row_wins:
                        winning_board = board
                        break


sum_of_unmarked = 0
for row in winning_board:
    for number in row:
        sum_of_unmarked += 0 if number == None else number

result = sum_of_unmarked * last_number
print(result)


# Part 2: You aren't sure how many bingo boards a giant squid could play at once, so rather than waste time counting its arms,
# the safe thing to do is to figure out which board will win last and choose that one
# !!! Not proud of this one, felt lazy today

winning_board = None
last_number = None
winning_boards = [False]*len(boards)

for number in numbers:
    if winning_board:
        break
    last_number = number
    for i, board in enumerate(boards):

        if winning_board:
            break

        for ii, row in enumerate(board):

            if winning_board:
                break

            for iii, rownumber in enumerate(row):
                if rownumber == number:
                    boards[i][ii][iii] = None
                    row_wins = not(any(row))

                    column = list()
                    for row2 in board:
                        column.append(row2[iii])
                    column_wins = not(any(column))

                    if column_wins | row_wins:
                        winning_boards[i] = True
                        if all(winning_boards):
                            winning_board = board
                            break


sum_of_unmarked = 0
for row in winning_board:
    for number in row:
        sum_of_unmarked += 0 if number == None else number

result = sum_of_unmarked * last_number
print(result)
