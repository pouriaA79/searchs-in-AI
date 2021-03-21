import copy
import re

moves_butter = []
moves_robot_to_butter_temp = []
moves_robot_to_butter = []
lenght_move_robot = 0
dept = 0


def read_file(str):
    file = open(str, 'r')
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
    number = 0
    for i in range(rows):
        for j in range(columns):
            if flag_butter_or_robot == "butter" and xarr[i][j] == "b":
                number += 1
                if number == 1:
                    x = i
                    y = j
            elif flag_butter_or_robot == "robot" and xarr[i][j] == "r":
                x = i
                y = j

    if goal_y >= columns or goal_y < 0 or goal_x < 0 or goal_x >= rows or Xarr[goal_x][goal_y] == "x":
        return False

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
        if x + 1 <= rows - 1 and xarr[x + 1][y] != "x" and xarr[x + 1][y] != "b":
            return True
    elif move == "U":
        if x - 1 >= 0 and xarr[x - 1][y] != "x" and xarr[x - 1][y] != "b":
            return True
    elif move == "L":
        if y - 1 >= 0 and xarr[x][y - 1] != "x" and xarr[x][y - 1] != "b":
            return True
    elif move == "R":
        if y + 1 <= columns - 1 and xarr[x][y + 1] != "x" and xarr[x][y + 1] != "b":
            return True
    else:
        return False


def IDS(root_x, root_y, depth, rows, columns, xarr, dist_x, dist_y, flag_butter_or_robot):
    global remaining, any_remaining
    directions = ("R", "D", "L", "U")
    if depth == 0 and (root_y != dist_y or root_x != dist_x):
        return False, True
    elif depth == 0 and root_y == dist_y and root_x == dist_x:
        return True, True
    elif depth > 0:
        any_remaining = False
        for j in directions:
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
            if xarr[butter[0]][butter[1] - 1] == "r":
                moves_robot_to_butter.append("R")
                xarr[robot[0]][robot[1]] = "n"
                xarr[butter[0]][butter[1]] = "r"
                xarr[butter[0]][butter[1] + 1] = "b"
                butter[1] += 1
                flag = True

            else:
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

            if xarr[butter[0]][butter[1] + 1] == "r":
                moves_robot_to_butter.append("L")
                xarr[robot[0]][robot[1]] = "n"
                xarr[butter[0]][butter[1]] = "r"
                xarr[butter[0]][butter[1] - 1] = "b"
                butter[1] -= 1
                flag = True
            else:
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
            print(butter[0] + 1)
            if xarr[butter[0] + 1][butter[1]] == "r":
                moves_robot_to_butter.append("U")
                xarr[robot[0]][robot[1]] = "n"
                xarr[butter[0]][butter[1]] = "r"
                xarr[butter[0] - 1][butter[1]] = "b"
                butter[0] -= 1
                flag = True

            else:

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
            if xarr[butter[0] - 1][butter[1]] == "r":
                moves_robot_to_butter.append("D")
                xarr[robot[0]][robot[1]] = "n"
                xarr[butter[0]][butter[1]] = "r"
                xarr[butter[0] + 1][butter[1]] = "b"
                butter[0] += 1
                flag = True

            else:
                flag = butter_map(xarr, cost, rows, columns, butter[0] - 1, butter[1], "robot")
                if flag:
                    xarr[robot[0]][robot[1]] = "n"
                    xarr[butter[0]][butter[1]] = "r"
                    xarr[butter[0] + 1][butter[1]] = "b"
                    for t in range(len(moves_robot_to_butter_temp) - lenght_move_robot):
                        moves_robot_to_butter.append(moves_robot_to_butter_temp[t])
                    moves_robot_to_butter.append("D")
                    butter[0] += 1
        if not flag:
            return False

        last_move = moves_butter[i]
        lenght_move_robot = len(moves_robot_to_butter_temp)


    return True


def robot_cost(Xarr, cost, rows, columns, moves_robot_to_butter):
    cost_robot = 0

    robot = []

    for i in range(rows):
        for j in range(columns):
            if Xarr[i][j] == "r":
                robot.append(i)
                robot.append(j)

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
    str = "test3.txt"
    rows, columns, Xarr, cost = read_file(str)
    xarr = copy.deepcopy(Xarr)

    num_butter = 0
    for i in range(rows):
        for j in range(columns):
            if Xarr[i][j] == "b":
                num_butter += 1
    flag_end = False
    num1 = 0
    num2 = 0
    last_move = ""
    last_p = [-1, -1]

    for k in range(num_butter):
        moves_butter=[]
        rows, columns, Xarr, cost = read_file(str)
        num2 = 0
        num1 = 0
        flag_end = False
        for i in range(rows):
            if flag_end:
                break
            for j in range(columns):
                if flag_end:
                    break

                if num1 < k:
                    if Xarr[i][j] == "r":
                        Xarr[i][j] = "n"
                    if Xarr[i][j] == "p":
                        Xarr[i][j] = "x"
                        num1 += 1

                if num2 < k:
                    if Xarr[i][j] == "r":
                        Xarr[i][j] = "n"
                    if Xarr[i][j] == "b":
                        Xarr[i][j] = "n"
                        num2 += 1

                if num1 == k and num2 == k :
                    if last_move=="D" and k>0:
                        Xarr[last_p[0]-1][last_p[1]]="r"
                    elif last_move=="U" and k>0:
                        Xarr[last_p[0]+1][last_p[1]]="r"
                    elif last_move=="L" and k>0:
                        Xarr[last_p[0]][last_p[1]-1]="r"
                    elif last_move=="R" and k>0:
                        Xarr[last_p[0]][last_p[1]+1]="r"

                    if Xarr[i][j] == "p":

                        goalx = i
                        goaly = j
                        flag, dept = butter_map(Xarr, cost, rows, columns, goalx, goaly, "butter")

                        if not flag:
                            print("cant pass the butter")
                        else:

                            if not robot_move(Xarr, cost, rows, columns, moves_butter):
                                print("cant pass the butter")
                            else:

                                cost_robot = robot_cost(xarr, cost, rows, columns, moves_robot_to_butter)
                                if k==num_butter-1:
                                    print(*moves_robot_to_butter, sep="\t")
                                    print(cost_robot)
                                    print(dept)
                                last_p[0] = goalx
                                last_p[1] = goaly
                                last_move = moves_robot_to_butter[-1]
                                flag_end = True
