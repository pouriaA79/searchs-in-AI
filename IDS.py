# import re
#
#
# def read_file():
#     file = open("test1.txt", 'r')
#     s = file.readline()
#     rows, columns = s.split("\t")
#     rows, columns = int(rows), int(columns)
#
#     costarr = [[0 for i in range(columns)] for j in range(rows)]
#     Xarr = [['n' for i in range(columns)] for j in range(rows)]
#     for i in range(rows):
#         str = file.readline()
#         row = re.split("\n|\t", str)
#         for j in range(columns):
#             if len(row[j]) == 1:
#                 if (row[j] == 'x'):
#                     Xarr[i][j] = row[j]
#                 else:
#                     costarr[i][j] = int(row[j])
#             elif len(row[j]) == 2:
#                 costarr[i][j] = int(row[j][0])
#                 Xarr[i][j] = row[j][1]
#     return rows, columns, Xarr, costarr
#
#
# def butter_map(Xarr, Cost, rows, columns, goal_x, goal_y):
#     last_move = []
#     cost = Cost
#     xarr = Xarr
#     found = False
#     remaining = True
#     root = {}
#     number = 0
#     x = 0
#     y = 0
#     for i in range(rows):
#         for j in range(columns):
#             if xarr[i][j] == "b":
#                 number += 1
#                 x = i
#                 y = j
#                 # root.update({str(number): [i, j]})
#         # for t in range(number):
#         #     x = root.get(str(t))[0]
#         #     y = root.get(str(t))[1]
#
#     for i in range(rows* columns):
#         found, remaining = IDS(x, y, i + 1, rows, columns, xarr, goal_x, goal_y)
#         if found:
#             return True
#         elif not remaining:
#             return False
#
#     return True
#
#
# def action(x, y, move, rows, columns, xarr):
#     if move == "D":
#         if x + 1 <= columns - 1 and xarr[x + 1][y] != "x":
#             return True
#     elif move == "U":
#         if x - 1 >= 0 and xarr[x - 1][y] != "x":
#             return True
#     elif move == "L":
#         if y - 1 >= 0 and xarr[x][y - 1] != "x":
#             return True
#     elif move == "R":
#         if y + 1 <= rows - 1 and xarr[x][y + 1] != "x":
#             return True
#     else:
#         return False
#
#
# def IDS(root_x, root_y, depth, rows, columns, xarr, dist_x, dist_y):
#     global remaining, any_remaining
#     directions = ("R", "D", "L", "U")
#     print(root_x, root_y, dist_x, dist_y)
#     if depth == 0 and (root_y != dist_y or root_x != dist_x):
#         return False, True
#     elif depth == 0 and root_y == dist_y and root_x == dist_x:
#         return True, True
#     elif depth > 0:
#         any_remaining = False
#         for j in directions:
#             print(j)
#             if j == "R":
#                 flag = action(root_x, root_y, "R", rows, columns, xarr)
#                 if flag:
#                     found, remaining = IDS(root_x, root_y + 1, depth - 1, rows, columns, xarr, dist_x, dist_y)
#                     if found:
#                         return True, True
#             elif j == "L":
#                 flag = action(root_x, root_y, "L", rows, columns, xarr)
#                 if flag:
#                     found, remaining = IDS(root_x, root_y - 1, depth - 1, rows, columns, xarr, dist_x, dist_y)
#                     if found:
#                         return True, True
#             elif j == "U":
#                 flag = action(root_x, root_y, "U", rows, columns, xarr)
#                 if flag:
#                     found, remaining = IDS(root_x - 1, root_y, depth - 1, rows, columns, xarr, dist_x, dist_y)
#                     if found:
#                         return True, True
#             elif j == "D":
#                 flag = action(root_x, root_y, "D", rows, columns, xarr)
#                 if flag:
#                     found, remaining = IDS(root_x + 1, root_y, depth - 1, rows, columns, xarr, dist_x, dist_y)
#                     if found:
#                         return True, True
#     if remaining:
#         any_remaining = True
#     return False, any_remaining
#
#
# if __name__ == "__main__":
#     rows, columns, Xarr, cost = read_file()
#     for i in range(rows):
#         for j in range(columns):
#             if Xarr[i][j] == "p":
#                 goalx = i
#                 goaly = j
#                 butter_map(Xarr, cost, rows, columns, goalx, goaly)
#
# moves_butter = []
# moves_robot_to_butter = []
#
#
# def read_file():
#     file = open("test1.txt", 'r')
#     s = file.readline()
#     rows, columns = s.split("\t")
#     rows, columns = int(rows), int(columns)
#
#     costarr = [[0 for i in range(columns)] for j in range(rows)]
#     Xarr = [['n' for i in range(columns)] for j in range(rows)]
#     for i in range(rows):
#         str = file.readline()
#         row = re.split("\n|\t", str)
#         for j in range(columns):
#             if len(row[j]) == 1:
#                 if (row[j] == 'x'):
#                     Xarr[i][j] = row[j]
#                 else:
#                     costarr[i][j] = int(row[j])
#             elif len(row[j]) == 2:
#                 costarr[i][j] = int(row[j][0])
#                 Xarr[i][j] = row[j][1]
#     return rows, columns, Xarr, costarr
#
#
# def butter_map(Xarr, Cost, rows, columns, goal_x, goal_y):
#     last_move = []
#     cost = Cost
#     xarr = Xarr
#     found = False
#     remaining = True
#     root = {}
#     number = 0
#     x = 0
#     y = 0
#     for i in range(rows):
#         for j in range(columns):
#             if  xarr[i][j] == "b":
#                 number += 1
#                 x = i
#                 y = j
#                 # root.update({str(number): [i, j]})
#         # for t in range(number):
#         #     x = root.get(str(t))[0]
#         #     y = root.get(str(t))[1]
#
#     for i in range(rows * columns):
#         found, remaining = IDS(x, y, i + 1, rows, columns, xarr, goal_x, goal_y)
#         if found:
#             print(i + 1)
#             return True
#         elif not remaining:
#             return False
#
#     return True
#
#
# def action(x, y, move, rows, columns, xarr):
#     if move == "D":
#         if x + 1 <= columns - 1 and xarr[x + 1][y] != "x":
#             return True
#     elif move == "U":
#         if x - 1 >= 0 and xarr[x - 1][y] != "x":
#             return True
#     elif move == "L":
#         if y - 1 >= 0 and xarr[x][y - 1] != "x":
#             return True
#     elif move == "R":
#         if y + 1 <= rows - 1 and xarr[x][y + 1] != "x":
#             return True
#     else:
#         return False
#
#
# def IDS(root_x, root_y, depth, rows, columns, xarr, dist_x, dist_y):
#     global remaining, any_remaining
#     directions = ("R", "D", "L", "U")
#     print(root_x, root_y, dist_x, dist_y)
#     if depth == 0 and (root_y != dist_y or root_x != dist_x):
#         return False, True
#     elif depth == 0 and root_y == dist_y and root_x == dist_x:
#         return True, True
#     elif depth > 0:
#         any_remaining = False
#         for j in directions:
#             print(j)
#             if j == "R":
#                 flag = action(root_x, root_y, "R", rows, columns, xarr)
#                 if flag:
#                     found, remaining = IDS(root_x, root_y + 1, depth - 1, rows, columns, xarr, dist_x, dist_y)
#                     if found:
#                         moves_butter.insert(0, j)
#                         return True, True
#             elif j == "L":
#                 flag = action(root_x, root_y, "L", rows, columns, xarr)
#                 if flag:
#                     found, remaining = IDS(root_x, root_y - 1, depth - 1, rows, columns, xarr, dist_x, dist_y)
#                     if found:
#                         moves_butter.insert(0, j)
#                         return True, True
#             elif j == "U":
#                 flag = action(root_x, root_y, "U", rows, columns, xarr)
#                 if flag:
#                     found, remaining = IDS(root_x - 1, root_y, depth - 1, rows, columns, xarr, dist_x, dist_y)
#                     if found:
#                         moves_butter.insert(0, j)
#                         return True, True
#             elif j == "D":
#                 flag = action(root_x, root_y, "D", rows, columns, xarr)
#                 if flag:
#                     found, remaining = IDS(root_x + 1, root_y, depth - 1, rows, columns, xarr, dist_x, dist_y)
#                     if found:
#                         moves_butter.insert(0, j)
#                         return True, True
#     if remaining:
#         any_remaining = True
#     return False, any_remaining
#
#
# def robot_move(xarr, cost, rows, columns, moves_butter):
#     butter = []
#     robot = []
#     X = []
#     flag_robot = False
#     flag_butter = False
#     for i in range(rows):
#         for j in range(columns):
#             if xarr[i][j] == "b":
#                 butter.append(i)
#                 butter.append(j)
#             if xarr[i][j] == "r":
#                 robot.append(i)
#                 robot.append(j)
#             if xarr[i][j] == "x":
#                 X.append(i)
#                 X.append(j)
#     for i in range(len(moves_butter)):
#
#
# if __name__ == "__main__":
#     rows, columns, Xarr, cost = read_file()
#
#     for i in range(rows):
#         for j in range(columns):
#             if Xarr[i][j] == "p":
#                 goalx = i
#                 goaly = j
#                 butter_map(Xarr, cost, rows, columns, goalx, goaly)
#     print(moves_butter)
#     robot_move(Xarr, cost, rows, columns, moves_butter)
import re
import  copy
moves_butter = []
moves_robot_to_butter_temp = []
moves_robot_to_butter = []
lenght_move_robot = 0
dept = 0


def read_file():
    file = open("test1.txt", 'r')
    s = file.readline()
    rows, columns = s.split("\t")
    rows, columns = int(rows), int(columns)

    costarr = [[0 for i in range(columns)] for j in range(rows)]
    Xarr = [['n' for i in range(columns)] for j in range(rows)]
    for i in range(rows):
        str = file.readline()
        row = re.split("\n|\t", str)
        for j in range(columns):
            if len(row[j]) == 1:
                if (row[j] == 'x'):
                    Xarr[i][j] = row[j]
                else:
                    costarr[i][j] = int(row[j])
            elif len(row[j]) == 2:
                costarr[i][j] = int(row[j][0])
                Xarr[i][j] = row[j][1]
    return rows, columns, Xarr, costarr


def butter_map(Xarr, Cost, rows, columns, goal_x, goal_y, flag_butter_or_robot):
    last_move = []
    cost = Cost
    xarr = Xarr
    found = False
    remaining = True
    root = {}
    number = 0
    x = 0
    y = 0
    for i in range(rows):
        for j in range(columns):
            if flag_butter_or_robot == "butter" and xarr[i][j] == "b":
                number += 1
                x = i
                y = j
            elif flag_butter_or_robot == "robot" and xarr[i][j] == "r":
                x = i
                y = j
                # root.update({str(number): [i, j]})
        # for t in range(number):
        #     x = root.get(str(t))[0]
        #     y = root.get(str(t))[1]

    for i in range(rows * columns):
        found, remaining = IDS(x, y, i + 1, rows, columns, xarr, goal_x, goal_y, flag_butter_or_robot)
        if found:
            if flag_butter_or_robot == "robot":
                return True
            else:
                return True, i + 1
        elif not remaining:
            return False

    return False


def action(x, y, move, rows, columns, xarr, flag):
    if move == "D":
        if x + 1 <= columns - 1 and xarr[x + 1][y] != "x":
            if flag == "robot":
                if xarr[x + 1][y] != "b":
                    return True
                else:
                    return False
            else:
                return True
    elif move == "U":
        if x - 1 >= 0 and xarr[x - 1][y] != "x":
            if flag == "robot":
                if xarr[x - 1][y] != "b":
                    return True
                else:
                    return False
            else:
                return True
    elif move == "L":
        if y - 1 >= 0 and xarr[x][y - 1] != "x":
            if flag == "robot":
                if xarr[x][y - 1] != "b":
                    return True
                else:
                    return False
            else:
                return True
    elif move == "R":
        if y + 1 <= rows - 1 and xarr[x][y + 1] != "x":
            if flag == "robot":
                if xarr[x][y + 1] != "b":
                    return True
                else:
                    return False
            else:
                return True
    else:
        return False


def IDS(root_x, root_y, depth, rows, columns, xarr, dist_x, dist_y, flag_butter_or_robot):
    global remaining, any_remaining
    directions = ("R", "D", "L", "U")
    # print(root_x, root_y, dist_x, dist_y)
    if depth == 0 and (root_y != dist_y or root_x != dist_x):
        return False, True
    elif depth == 0 and root_y == dist_y and root_x == dist_x:
        return True, True
    elif depth > 0:
        any_remaining = False
        for j in directions:
            # print(j)
            if j == "R":
                flag = action(root_x, root_y, "R", rows, columns, xarr, flag_butter_or_robot)

                if flag:
                    found, remaining = IDS(root_x, root_y + 1, depth - 1, rows, columns, xarr, dist_x, dist_y,
                                           flag_butter_or_robot)
                    if found:
                        if flag_butter_or_robot == "butter":
                            moves_butter.insert(0, j)
                        else:
                            moves_robot_to_butter_temp.insert(0, j)
                        return True, True
            elif j == "L":
                flag = action(root_x, root_y, "L", rows, columns, xarr, flag_butter_or_robot)
                if flag:
                    found, remaining = IDS(root_x, root_y - 1, depth - 1, rows, columns, xarr, dist_x, dist_y,
                                           flag_butter_or_robot)
                    if found:
                        if flag_butter_or_robot == "butter":
                            moves_butter.insert(0, j)
                        else:
                            moves_robot_to_butter_temp.insert(0, j)
                        return True, True
            elif j == "U":
                flag = action(root_x, root_y, "U", rows, columns, xarr, flag_butter_or_robot)
                if flag:
                    found, remaining = IDS(root_x - 1, root_y, depth - 1, rows, columns, xarr, dist_x, dist_y,
                                           flag_butter_or_robot)
                    if found:
                        if flag_butter_or_robot == "butter":
                            moves_butter.insert(0, j)
                        else:
                            moves_robot_to_butter_temp.insert(0, j)
                        return True, True
            elif j == "D":
                flag = action(root_x, root_y, "D", rows, columns, xarr, flag_butter_or_robot)
                if flag:
                    found, remaining = IDS(root_x + 1, root_y, depth - 1, rows, columns, xarr, dist_x, dist_y,
                                           flag_butter_or_robot)
                    if found:
                        if flag_butter_or_robot == "butter":
                            moves_butter.insert(0, j)
                        else:
                            moves_robot_to_butter_temp.insert(0, j)
                        return True, True
    if remaining:
        any_remaining = True
    return False, any_remaining


def robot_move(xarr, cost, rows, columns, moves_butter):
    global lenght_move_robot
    butter = []
    robot = []
    X = []
    flag_robot = False
    flag_butter = False
    for i in range(rows):
        for j in range(columns):
            if xarr[i][j] == "b":
                butter.append(i)
                butter.append(j)
            if xarr[i][j] == "r":
                robot.append(i)
                robot.append(j)
            if xarr[i][j] == "x":
                X.append(i)
                X.append(j)
    last_move = ""
    for i in range(len(moves_butter)):
        if moves_butter[i] == last_move:
            moves_robot_to_butter.append(last_move)
        elif moves_butter[i] != last_move and moves_butter[i] == "R":
            flag = butter_map(xarr, cost, rows, columns, butter[0], butter[1] - 1, "robot")
            if flag:
                xarr[robot[0]][robot[1]] = "n"
                xarr[butter[0]][butter[1]] = "r"
                xarr[butter[0]][butter[1] + 1] = "b"
                for t in range(len(moves_robot_to_butter_temp) - lenght_move_robot):
                    moves_robot_to_butter.append(moves_robot_to_butter_temp[t])
                moves_robot_to_butter.append("R")
                butter[1] += 1
        elif moves_butter[i] != last_move and moves_butter[i] == "L":

            flag = butter_map(xarr, cost, rows, columns, butter[0], butter[1] + 1, "robot")
            if flag:
                xarr[robot[0]][robot[1]] = "n"
                xarr[butter[0]][butter[1]] = "r"
                xarr[butter[0]][butter[1] - 1] = "b"
                for t in range(len(moves_robot_to_butter_temp) - lenght_move_robot):
                    moves_robot_to_butter.append(moves_robot_to_butter_temp[t])
                moves_robot_to_butter.append("L")
                butter[1] -= 1
        elif moves_butter[i] != last_move and moves_butter[i] == "U":

            flag = butter_map(xarr, cost, rows, columns, butter[0] + 1, butter[1], "robot")
            if flag:
                xarr[robot[0]][robot[1]] = "n"
                xarr[butter[0]][butter[1]] = "r"
                xarr[butter[0] - 1][butter[1]] = "b"
                for t in range(len(moves_robot_to_butter_temp) - lenght_move_robot):
                    moves_robot_to_butter.append(moves_robot_to_butter_temp[t])
                moves_robot_to_butter.append("U")
                butter[0] -= 1
        elif moves_butter[i] != last_move and moves_butter[i] == "D":
            flag = butter_map(xarr, cost, rows, columns, butter[0] - 1, butter[1], "robot")
            if flag:
                xarr[robot[0]][robot[1]] = "n"
                xarr[butter[0]][butter[1]] = "r"
                xarr[butter[0] + 1][butter[1]] = "b"
                for t in range(len(moves_robot_to_butter_temp) - lenght_move_robot):
                    moves_robot_to_butter.append(moves_robot_to_butter_temp[t])
                moves_robot_to_butter.append("D")
                butter[0] += 1
        last_move = moves_butter[i]
        lenght_move_robot = len(moves_robot_to_butter_temp)
        # print(moves_robot_to_butter_temp)
        # print(moves_robot_to_butter)


def robot_cost(Xarr, cost, rows, columns, moves_robot_to_butter):
    cost_robot = 0
    # butter = []
    robot = []

    for i in range(rows):
        for j in range(columns):
            # if Xarr[i][j] == "b":
            #     butter.append(i)
            #     butter.append(j)
            if Xarr[i][j] == "r":
                robot.append(i)
                robot.append(j)
    # print(Xarr)
    # print(cost[robot[0]][robot[1]])
    # print(robot[0], robot[1])
    for i in range(len(moves_robot_to_butter)):
        if moves_robot_to_butter[i] == "R":
            cost_robot = cost_robot + cost[robot[0]][robot[1]]
            robot[1] += 1
        elif moves_robot_to_butter[i] == "L":
            cost_robot = cost_robot + cost[robot[0]][robot[1]]
            robot[1] -= 1
        elif moves_robot_to_butter[i] == "U":
            cost_robot = cost_robot + cost[robot[0]][robot[1]]
            robot[0] -= 1
        elif moves_robot_to_butter[i] == "D":
            cost_robot = cost_robot + cost[robot[0]][robot[1]]
            robot[0] += 1

    return cost_robot


if __name__ == "__main__":
    rows, columns, Xarr, cost = read_file()
    xarr = copy.deepcopy(Xarr)
    for i in range(rows):
        for j in range(columns):
            if Xarr[i][j] == "p":
                goalx = i
                goaly = j
                flag, dept = butter_map(Xarr, cost, rows, columns, goalx, goaly, "butter")
    # print(moves_butter)
    robot_move(Xarr, cost, rows, columns, moves_butter)
    # print(moves_butter)
    cost_robot = robot_cost(xarr, cost, rows, columns, moves_robot_to_butter)
    print(*moves_robot_to_butter,sep="\t")
    print(cost_robot)
    print(dept)

