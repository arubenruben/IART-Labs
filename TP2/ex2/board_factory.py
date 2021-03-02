# Eduardo Ribeiro copyrights, used under MIT license. Link Github:https://github.com/EduRibeiro00/CovidForecast-feup-iart/blob/375eb834e6759024fccedfd38e4ee43796e49e22/practical_classes/prat_02/n-puzzle/utils.py#L1

def create_board(number):
    if number == 1:
        return [[
            [1, 2, 3],
            [5, 0, 6],
            [4, 7, 8]
        ], (1, 1)]

    elif number == 2:
        return [[
            [1, 3, 6],
            [5, 2, 0],
            [4, 7, 8]
        ], (1, 2)]

    elif number == 3:
        return [[
            [1, 6, 2],
            [5, 7, 3],
            [0, 4, 8]
        ], (2, 0)]

    elif number == 4:
        return [[
            [5, 1, 3, 4],
            [2, 0, 7, 8],
            [10, 6, 11, 12],
            [9, 13, 14, 15]
        ], (1, 1)]

    else:
        return None
