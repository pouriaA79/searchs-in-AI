import re
from queue import Queue

q_forward = Queue()
q_f_num = Queue()
q_b_num = Queue()
q_backward = Queue()
lenght_move_robot = 0
q_all = Queue()
moves_robot_to_butter = []
moves_robot_to_butter_temp = []
last_move = ""


def read_file(str):
    file = open(str, 'r')
    s = file.readline()
    rows, columns = s.split("\t")
    rows, columns = int(rows), int(columns)

    Xarr = [['n' for i in range(columns)] for j in range(rows)]
    for i in range(rows):
        str = file.readline()
        row = re.split("\n|\t", str)
        for j in range(columns):
            if len(row[j]) == 1:
                if (row[j] == 'x'):
                    Xarr[i][j] = row[j]
            elif len(row[j]) == 2:
                Xarr[i][j] = row[j][1]
    return rows, columns, Xarr


def butter_map(arr, rows, columns, goal_x, goal_y, flag_butter_or_robot):
    x = 0
    y = 0
    for i in range(rows):
        for j in range(columns):
            if flag_butter_or_robot == "butter" and arr[i][j] == "b":
                x = i
                y = j

    if goal_y >= columns or goal_y < 0 or goal_x < 0 or goal_x >= rows or Xarr[goal_x][goal_y] == "x":
        return False

    bidirectional_bfs(goal_x, goal_y, x, y, rows, columns, arr, flag_butter_or_robot)
    return 0


def action(x, y, move, rows, columns, xarr):
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


def bfs(dir, s_x, s_y, dest_x, dest_y, row, col, arr, b_or_r):
    global barkhord
    directions = ("R", "D", "L", "U")
    parent = [[0 for i in range(col)] for j in range(row)]
    seen = [[-1 for i in range(col)] for j in range(row)]
    q_forward = Queue()
    q_f_num = Queue()
    q_b_num = Queue()
    q_backward = Queue()
    q_all = Queue()
    # barkhord=()
    q_forward.put((s_x, s_y))
    q_backward.put((dest_x, dest_y))
    q_all.put((dest_x, dest_y))
    q_all.put((s_x, s_y))
    q_b_num.put(1)
    q_f_num.put(1)
    seen[s_x][s_y] = 2
    seen[dest_x][dest_y] = 1
    parent[s_x][s_y] = -1
    parent[dest_x][dest_y] = -1
    flag_end = False
    dif_x = s_x - dest_x
    dif_y = s_y - dest_y

    if dif_y == 0 and dif_x == 1:
        return "U", (0, 0), parent, 0, 0, "R", "f"
    elif dif_y == 0 and dif_x == -1:
        return "D", (0, 0), parent, 0, 0, "R", "f"
    elif dif_y == 1 and dif_x == 0:
        return "L", (0, 0), parent, 0, 0, "R", "f"
    elif dif_y == -1 and dif_x == 0:
        return "R", (0, 0), parent, 0, 0, "R", "f"

    for i in range(row * col):
        if i % 2 == 0:
            numf_to_add = 0
            num_f = q_f_num.get()

            for j in range(num_f):

                f = q_forward.get()
                for j in directions:
                    flag = action(f[0], f[1], j, row, col, arr)

                    if flag:
                        numf_to_add += 1
                        if j == "R":

                            q_forward.put((f[0], f[1] + 1, j))
                            if seen[f[0]][f[1] + 1] == 1:
                                flag_end = True
                                barkhord = (f[0], f[1] + 1)
                                return "n", barkhord, parent, f[0], f[1], j, "f"
                            else:
                                if parent[f[0]][f[1] + 1] == 0:
                                    parent[f[0]][f[1] + 1] = f[0] * 10 + f[1]
                                seen[f[0]][f[1] + 1] = 2
                                q_all.put((f[0], f[1] + 1, j, i))

                        elif j == "L":

                            q_forward.put((f[0], f[1] - 1, j))
                            if seen[f[0]][f[1] - 1] == 1:
                                flag_end = True
                                barkhord = (f[0], f[1] - 1)
                                return "n", barkhord, parent, f[0], f[1], j, "f"
                            else:
                                if parent[f[0]][f[1] - 1] == 0:
                                    parent[f[0]][f[1] - 1] = f[0] * 10 + f[1]
                                seen[f[0]][f[1] - 1] = 2
                                q_all.put((f[0], f[1] - 1, j))
                        elif j == "U":

                            q_forward.put((f[0] - 1, f[1], j))
                            if seen[f[0] - 1][f[1]] == 1:
                                flag_end = True
                                barkhord = (f[0] - 1, f[1])
                                return "n", barkhord, parent, f[0], f[1], j, "f"
                            else:
                                if parent[f[0] - 1][f[1]] == 0:
                                    parent[f[0] - 1][f[1]] = f[0] * 10 + f[1]
                                seen[f[0] - 1][f[1]] = 2
                                q_all.put((f[0] - 1, f[1], j))
                        elif j == "D":

                            q_forward.put((f[0] + 1, f[1], j))
                            if seen[f[0] + 1][f[1]] == 1:
                                flag_end = True
                                barkhord = (f[0] + 1, f[1])
                                return "n", barkhord, parent, f[0], f[1], j, "f"
                            else:
                                if parent[f[0] + 1][f[1]] == 0:
                                    parent[f[0] + 1][f[1]] = f[0] * 10 + f[1]
                                seen[f[0] + 1][f[1]] = 2
                                q_all.put((f[0] + 1, f[1], j))

                if numf_to_add > 0:
                    q_f_num.put(numf_to_add)
            # print(seen, 1)
        else:
            numb_to_add = 0
            num_b = q_b_num.get()
            for j in range(num_b):
                b = q_backward.get()
                for j in directions:

                    flag = action(b[0], b[1], j, row, col, arr)
                    if flag:
                        numb_to_add += 1
                        if j == "R":

                            q_backward.put((b[0], b[1] + 1, j))
                            if seen[b[0]][b[1] + 1] == 2:
                                flag_end = True
                                barkhord = (b[0], b[1] + 1)
                                return "n", barkhord, parent, b[0], b[1], j, "b"
                            else:
                                if parent[b[0]][b[1] + 1] == 0:
                                    parent[b[0]][b[1] + 1] = b[0] * 10 + b[1]
                                seen[b[0]][b[1] + 1] = 1
                                q_all.put((b[0], b[1] + 1, j))

                        elif j == "L":

                            q_backward.put((b[0], b[1] - 1, j))
                            if seen[b[0]][b[1] - 1] == 2:

                                flag_end = True
                                barkhord = (b[0], b[1] - 1)
                                return "n", barkhord, parent, b[0], b[1], j, "b"

                            else:
                                if parent[b[0]][b[1] - 1] == 0:
                                    parent[b[0]][b[1] - 1] = b[0] * 10 + b[1]
                                seen[b[0]][b[1] - 1] = 1
                                q_all.put((b[0], b[1] - 1, j))
                        elif j == "U":

                            q_backward.put((b[0] - 1, b[1], j))
                            if seen[b[0] - 1][b[1]] == 2:
                                flag_end = True
                                barkhord = (b[0] - 1, b[1])
                                return "n", barkhord, parent, b[0], b[1], j, "b"
                            else:
                                if parent[b[0] - 1][b[1]] == 0:
                                    parent[b[0] - 1][b[1]] = b[0] * 10 + b[1]
                                seen[b[0] - 1][b[1]] = 1
                                q_all.put((b[0] - 1, b[1], j))
                        elif j == "D":

                            q_backward.put((b[0] + 1, b[1], j))
                            if seen[b[0] + 1][b[1]] == 2:
                                flag_end = True
                                barkhord = (b[0] + 1, b[1])
                                return "n", barkhord, parent, b[0], b[1], j, "b"

                            else:
                                if parent[b[0] + 1][b[1]] == 0:
                                    parent[b[0] + 1][b[1]] = b[0] * 10 + b[1]
                                seen[b[0] + 1][b[1]] = 1
                                q_all.put((b[0] + 1, b[1], j))

                    if numb_to_add > 0:
                        q_b_num.put(numb_to_add)
    if not flag_end:
        return "n", barkhord, parent, -1, -1, "R", "b"

    return 0


def bidirectional_bfs(dest_x, dest_y, row, col, arr, flag_butter_or_robot):
    start_x = 0
    start_y = 0
    for i in range(row):
        for j in range(col):
            if arr[i][j] == "b":
                start_x = i
                start_y = j
                break

    one_move, barkhord, parent, x, y, move, b_f = bfs("f", start_x, start_y, dest_x, dest_y, row, col, arr,
                                                      flag_butter_or_robot)
    list_f = []
    list_b = []

    if x < 0 and y < 0:
        return False, [0, 0]
    else:
        if one_move != "n":
            list_f.append(one_move)
            return True, one_move
        else:
            list_f.insert(0, [barkhord[0], barkhord[1]])
            list_b.insert(0, [x, y])

            for i in range(row * col):
                x = parent[list_f[0][0]][list_f[0][1]]
                list_f.insert(0, [int(x / 10), x % 10])
                if parent[list_f[0][0]][list_f[0][1]] == -1:
                    break
            for i in range(row * col):
                x = parent[list_b[-1][0]][list_b[-1][1]]
                list_b.append([int(x / 10), x % 10])
                if parent[list_b[-1][0]][list_b[-1][1]] == -1:
                    break
            moves_butter_to_p = []
            if b_f == "b":
                list_f = list_f + list_b
            else:
                list_b.reverse()
                list_f.reverse()

                list_f = list_b + list_f

            for i in range(len(list_f) - 1):
                dif_x = list_f[i + 1][0] - list_f[i][0]
                dif_y = list_f[i + 1][1] - list_f[i][1]
                if dif_x > 0:
                    moves_butter_to_p.append("D")
                elif dif_x < 0:
                    moves_butter_to_p.append("U")
                elif dif_y > 0:
                    moves_butter_to_p.append("R")
                elif dif_y < 0:
                    moves_butter_to_p.append("L")
            return True, moves_butter_to_p

    return 0, [55]


def road(x, parent, f0, f1):
    list_f = []
    if f0 < 0 and f1 < 0:
        return False, [0, 0]
    else:
        if x != "n":
            list_f.append(x)
            print(list_f)
        else:
            list_f.insert(0, [f0, f1])
            for i in range(rows * columns):
                x = parent[list_f[0][0]][list_f[0][1]]
                list_f.insert(0, [int(x / 10), x % 10])
                if parent[list_f[0][0]][list_f[0][1]] == -1:
                    break
    for i in range(len(list_f) - 1):
        dif_x = list_f[i + 1][0] - list_f[i][0]
        dif_y = list_f[i + 1][1] - list_f[i][1]
        if dif_x > 0:
            moves_robot_to_butter_temp.append("D")
        elif dif_x < 0:
            moves_robot_to_butter_temp.append("U")
        elif dif_y > 0:
            moves_robot_to_butter_temp.append("R")
        elif dif_y < 0:
            moves_robot_to_butter_temp.append("L")
    return True, moves_robot_to_butter_temp


def BFS(start_x, start_y, dest_x, dest_y, row, col, arr):
    directions = ("R", "D", "L", "U")
    parent = [[0 for i in range(col)] for j in range(row)]
    seen = [[-1 for i in range(col)] for j in range(row)]
    q_forward = Queue()
    q_f_num = Queue()
    q_forward.put((start_x, start_y))
    q_f_num.put(1)
    seen[start_x][start_y] = 2
    seen[dest_x][dest_y] = 1
    parent[start_x][start_y] = -1
    flag_end = False
    dif_x = start_x - dest_x
    dif_y = start_y - dest_y

    if dif_y == 0 and dif_x == 1:
        return "U", parent, 0, 0

    elif dif_y == 0 and dif_x == -1:
        return "D", parent, 0, 0

    elif dif_y == 1 and dif_x == 0:
        return "L", parent, 0, 0

    elif dif_y == -1 and dif_x == 0:
        return "R", parent, 0, 0

    for i in range(row * col * 100):
        numf_to_add = 0
        num_f = q_f_num.get()
        for j in range(num_f):

            f = q_forward.get()
            for j in directions:
                flag = action(f[0], f[1], j, row, col, arr)

                if flag:
                    numf_to_add += 1
                    if j == "R":

                        q_forward.put((f[0], f[1] + 1))
                        if seen[f[0]][f[1] + 1] == 1:
                            barkhord = (f[0], f[1] + 1)
                            if parent[f[0]][f[1] + 1] == 0:
                                parent[f[0]][f[1] + 1] = f[0] * 10 + f[1]
                            road("n", parent, f[0], f[1] + 1)
                            return True
                        else:
                            if parent[f[0]][f[1] + 1] == 0:
                                parent[f[0]][f[1] + 1] = f[0] * 10 + f[1]
                            seen[f[0]][f[1] + 1] = 2

                    elif j == "L":

                        q_forward.put((f[0], f[1] - 1))
                        if seen[f[0]][f[1] - 1] == 1:
                            if parent[f[0]][f[1] - 1] == 0:
                                parent[f[0]][f[1] - 1] = f[0] * 10 + f[1]
                            flag_end = True
                            barkhord = (f[0], f[1] - 1)
                            road("n", parent, f[0], f[1] - 1)

                            return True
                        else:
                            if parent[f[0]][f[1] - 1] == 0:
                                parent[f[0]][f[1] - 1] = f[0] * 10 + f[1]
                            seen[f[0]][f[1] - 1] = 2
                    elif j == "U":

                        q_forward.put((f[0] - 1, f[1]))
                        if seen[f[0] - 1][f[1]] == 1:
                            if parent[f[0] - 1][f[1]] == 0:
                                parent[f[0] - 1][f[1]] = f[0] * 10 + f[1]
                            barkhord = (f[0] - 1, f[1])
                            road("n", parent, f[0] - 1, f[1])

                            return True
                        else:
                            if parent[f[0] - 1][f[1]] == 0:
                                parent[f[0] - 1][f[1]] = f[0] * 10 + f[1]
                            seen[f[0] - 1][f[1]] = 2

                    elif j == "D":

                        q_forward.put((f[0] + 1, f[1]))
                        if seen[f[0] + 1][f[1]] == 1:
                            if parent[f[0] + 1][f[1]] == 0:
                                parent[f[0] + 1][f[1]] = f[0] * 10 + f[1]

                            road("n", parent, f[0] + 1, f[1])

                            return True
                        else:
                            if parent[f[0] + 1][f[1]] == 0:
                                parent[f[0] + 1][f[1]] = f[0] * 10 + f[1]
                            seen[f[0] + 1][f[1]] = 2

                if numf_to_add > 0:
                    q_f_num.put(numf_to_add)
    if not flag_end:
        return False

    return False


def find(arr):
    for i in range(rows):
        for j in range(columns):
            if arr[i][j] == "r":
                return i, j
    return 0, 0


def robot_move(rows, columns, moves_butter, arr):
    global lenght_move_robot
    butter = []
    robot = []
    X = []

    for i in range(rows):
        for j in range(columns):
            if arr[i][j] == "b":
                butter.append(i)
                butter.append(j)
            if arr[i][j] == "r":
                robot.append(i)
                robot.append(j)
            if arr[i][j] == "x":
                X.append(i)
                X.append(j)
    last_move = ""
    if butter[0] >= columns or butter[1] < 0 or butter[1] < 0 or butter[0] >= rows or arr[butter[0]][butter[1]] == "x":
        # print(45)
        return False
    for i in range(len(moves_butter)):
        # print(arr)

        if moves_butter[i] == "R":
            if butter[1] - 1 < 0:
                return False
            if arr[butter[0]][butter[1] - 1] == "r":
                moves_robot_to_butter.append("R")
                for _ in range(rows):
                    for o in range(columns):
                        if arr[_][o] == "r":
                            arr[_][o] = "n"
                arr[robot[0]][robot[1]] = "n"
                arr[butter[0]][butter[1]] = "r"
                arr[butter[0]][butter[1] + 1] = "b"
                butter[1] += 1
                flag = True


            else:
                xx, yy = find(arr)
                flag = BFS(xx, yy, butter[0], butter[1] - 1, rows, columns, arr)
                # print(5,flag)
                if flag:
                    for _ in range(rows):
                        for o in range(columns):
                            if arr[_][o] == "r":
                                arr[_][o] = "n"
                    arr[robot[0]][robot[1]] = "n"
                    arr[butter[0]][butter[1]] = "r"
                    arr[butter[0]][butter[1] + 1] = "b"

                    for t in range(len(moves_robot_to_butter_temp) - lenght_move_robot):
                        moves_robot_to_butter.append(
                            moves_robot_to_butter_temp[t - len(moves_robot_to_butter_temp) + lenght_move_robot])
                    moves_robot_to_butter.append("R")
                    butter[1] += 1
        elif moves_butter[i] == "L":
            if butter[1] + 1 >= columns:
                return False
            if arr[butter[0]][butter[1] + 1] == "r":
                moves_robot_to_butter.append("L")
                for _ in range(rows):
                    for o in range(columns):
                        if arr[_][o] == "r":
                            arr[_][o] = "n"
                arr[robot[0]][robot[1]] = "n"
                arr[butter[0]][butter[1]] = "r"
                arr[butter[0]][butter[1] - 1] = "b"
                butter[1] -= 1

                flag = True

            else:
                xx, yy = find(arr)
                flag = BFS(xx, yy, butter[0], butter[1] + 1, rows, columns, arr)
                if flag:
                    for _ in range(rows):
                        for o in range(columns):
                            if arr[_][o] == "r":
                                arr[_][o] = "n"
                    arr[robot[0]][robot[1]] = "n"
                    arr[butter[0]][butter[1]] = "r"
                    arr[butter[0]][butter[1] - 1] = "b"
                    for t in range(len(moves_robot_to_butter_temp) - lenght_move_robot):
                        moves_robot_to_butter.append(
                            moves_robot_to_butter_temp[t - len(moves_robot_to_butter_temp) + lenght_move_robot])
                    moves_robot_to_butter.append("L")

                    butter[1] -= 1
        elif moves_butter[i] == "U":
            if butter[0] + 1 >= rows:
                return False
            if arr[butter[0] + 1][butter[1]] == "r":
                moves_robot_to_butter.append("U")
                for _ in range(rows):
                    for o in range(columns):
                        if arr[_][o] == "r":
                            arr[_][o] = "n"
                arr[robot[0]][robot[1]] = "n"
                arr[butter[0]][butter[1]] = "r"
                arr[butter[0] - 1][butter[1]] = "b"
                butter[0] -= 1
                flag = True

            else:
                xx, yy = find(arr)
                flag = BFS(xx, yy, butter[0] + 1, butter[1], rows, columns, arr)
                if flag:
                    for _ in range(rows):
                        for o in range(columns):
                            if arr[_][o] == "r":
                                arr[_][o] = "n"
                    arr[robot[0]][robot[1]] = "n"
                    arr[butter[0]][butter[1]] = "r"
                    arr[butter[0] - 1][butter[1]] = "b"
                    # print(arr,45)
                    for t in range(len(moves_robot_to_butter_temp) - lenght_move_robot):
                        moves_robot_to_butter.append(
                            moves_robot_to_butter_temp[t - len(moves_robot_to_butter_temp) + lenght_move_robot])
                    moves_robot_to_butter.append("U")
                    butter[0] -= 1

                    flag = True
        elif moves_butter[i] == "D":
            if butter[0] - 1 < 0:
                return False
            if arr[butter[0] - 1][butter[1]] == "r":
                moves_robot_to_butter.append("D")
                for _ in range(rows):
                    for o in range(columns):
                        if arr[_][o] == "r":
                            arr[_][o] = "n"
                arr[robot[0]][robot[1]] = "n"
                arr[butter[0]][butter[1]] = "r"
                arr[butter[0] + 1][butter[1]] = "b"
                butter[0] += 1
                flag = True

            else:
                xx, yy = find(arr)
                flag = BFS(xx, yy, butter[0] - 1, butter[1], rows, columns, arr)
                if flag:

                    for _ in range(rows):
                        for o in range(columns):
                            if arr[_][o] == "r":
                                arr[_][o] = "n"
                    arr[robot[0]][robot[1]] = "n"
                    arr[butter[0]][butter[1]] = "r"

                    arr[butter[0] + 1][butter[1]] = "b"
                    for t in range(len(moves_robot_to_butter_temp) - lenght_move_robot):
                        moves_robot_to_butter.append(
                            moves_robot_to_butter_temp[t - len(moves_robot_to_butter_temp) + lenght_move_robot])
                    moves_robot_to_butter.append("D")

                    butter[0] += 1
                    flag = True
        if not flag:
            return False

        last_move = moves_butter[i]
        lenght_move_robot = len(moves_robot_to_butter_temp)

    return True


if __name__ == "__main__":
    str = "test3.txt"
    rows, columns, Xarr = read_file(str)
    num_butter = 0
    moves_butter = []

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
        # print(k,546)
        num2 = 0
        num1 = 0
        flag_end = False
        # print(Xarr)
        num1 = k
        for i in range(rows):
            if flag_end:
                break
            for j in range(columns):
                if flag_end:
                    break

                if num1 == k:

                    if Xarr[i][j] == "p":

                        flag, moves_butter = bidirectional_bfs(i, j, rows, columns, Xarr, "b")
                        if not flag:
                            print("cant pass the butter")
                        else:
                            if not robot_move(rows, columns, moves_butter, Xarr):
                                print("cant pass the butter")
                            else:

                                cost_robot = len(moves_robot_to_butter)

                                if k == num_butter - 1:
                                    print(*moves_robot_to_butter, sep="\t")
                                    print(cost_robot)
                                Xarr[i][j] = "x"

                                last_move = moves_robot_to_butter[-1]
                                flag_end = True
