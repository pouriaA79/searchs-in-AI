import os
import re


class Node:
    def __init__(self, parent=None, position=None):
        self.parent = parent
        self.position = position

        self.g = 0
        self.h = 0
        self.f = 0

    def __eq__(self, other):
        return self.position == other.position


def read_input(file_name):
    file = open(file_name, 'r')
    first_line = file.readline()
    rows_no, columns_no = first_line.split("\t")
    rows_no, columns_no = int(rows_no), int(columns_no)

    cost_map = [[0 for i in range(columns_no)] for j in range(rows_no)]
    object_map = [['n' for i in range(columns_no)] for j in range(rows_no)]
    for i in range(rows_no):
        line = file.readline()
        row = re.split("\n|\t", line)
        for j in range(columns_no):
            if len(row[j]) == 1:
                if row[j] == 'x':
                    object_map[i][j] = row[j]
                else:
                    cost_map[i][j] = int(row[j])
            elif len(row[j]) == 2:
                cost_map[i][j] = int(row[j][0])
                object_map[i][j] = row[j][1]
    return rows_no, columns_no, object_map, cost_map


def convert_path_to_action(shortest_path):
    action = []
    for i in range(len(shortest_path) - 1):
        action_x = shortest_path[i + 1][0] - shortest_path[i][0]
        action_y = shortest_path[i + 1][1] - shortest_path[i][1]
        if action_x == -1 and action_y == 0:
            action.append("UP")
        elif action_x == 1 and action_y == 0:
            action.append("DOWN")
        elif action_x == 0 and action_y == 1:
            action.append("RIGHT")
        elif action_x == 0 and action_y == -1:
            action.append("LEFT")

    return action


def search(cost_map, objects_map, src, dest):
    start_node = Node(None, tuple(src))
    start_node.g = start_node.h = start_node.f = 0
    end_node = Node(None, tuple(dest))
    end_node.g = end_node.h = end_node.f = 0

    yet_to_visit_list = []
    visited_list = []

    # Add the start node
    yet_to_visit_list.append(start_node)

    # Adding a stop condition. This is to avoid any infinite loop and stop
    # execution after some reasonable number of steps
    outer_iterations = 0
    max_iterations = (len(objects_map) // 2) ** 10

    # what squares do we search . serarch movement is left-right-top-bottom
    # (4 movements) from every positon

    move = [[-1, 0],  # go up
            [0, 1],  # go right
            [1, 0],  # go down
            [0, -1]]  # go left

    no_rows = len(objects_map)
    no_columns = len(objects_map[0])

    # Loop until you find the end

    while len(yet_to_visit_list) > 0:

        # Every time any node is referred from yet_to_visit list, counter of limit operation incremented
        outer_iterations += 1

        # Get the current node
        current_node = yet_to_visit_list[0]
        current_index = 0
        for index, item in enumerate(yet_to_visit_list):
            if item.f < current_node.f:
                current_node = item
                current_index = index

        # if we hit this point return the path such as it may be no solution or
        # computation cost is too high
        if outer_iterations > max_iterations:
            print("giving up on pathfinding too many iterations")
            path2 = []
            current = current_node
            while current is not None:
                path2.append(current.position)
                current = current.parent
            return path2[::-1], -1, -1

            # Pop current node out off yet_to_visit list, add to visited list
        yet_to_visit_list.pop(current_index)
        visited_list.append(current_node)

        # test if goal is reached or not, if yes then return the path
        if current_node == end_node:
            path1 = []
            current = current_node
            while current is not None:
                path1.append(current.position)
                current = current.parent

            return path1[::-1], current_node.g, outer_iterations - 1

            # Generate children from all adjacent squares
        children = []

        for new_position in move:
            # Get node position
            node_position = (current_node.position[0] + new_position[0], current_node.position[1] + new_position[1])

            # Make sure within range (check if within maze boundary)
            if (node_position[0] > (no_rows - 1) or
                    node_position[0] < 0 or
                    node_position[1] > (no_columns - 1) or
                    node_position[1] < 0):
                continue

            # Make sure walkable terrain
            if objects_map[node_position[0]][node_position[1]] == 'x':
                continue

            if objects_map[node_position[0]][node_position[1]] == 'b':
                if not (src[0] == node_position[0] and src[1] == node_position[1]):
                    continue
            # Create new node
            new_node = Node(current_node, node_position)

            # Append
            children.append(new_node)

        # Loop through children
        for child in children:

            # Child is on the visited list (search entire visited list)
            if len([visited_child for visited_child in visited_list if visited_child == child]) > 0:
                continue

            child.g = current_node.g + cost_map[current_node.position[0]][current_node.position[1]]
            # Heuristic costs calculated here, this is using eucledian distance
            child.h = (((child.position[0] - end_node.position[0]) ** 2) +
                       ((child.position[1] - end_node.position[1]) ** 2))

            child.f = child.g + child.h

            # Child is already in the yet_to_visit list and g cost is already lower
            if len([d for d in yet_to_visit_list if child == d and child.g > d.g]) > 0:
                continue

            # Add the child to the yet_to_visit list
            yet_to_visit_list.append(child)


def robot_goal(initial_state, move):
    goal_x = initial_state[0]
    goal_y = initial_state[1]
    if move == 'UP':
        goal_x += 1
    elif move == 'DOWN':
        goal_x -= 1
    elif move == 'LEFT':
        goal_y += 1
    elif move == 'RIGHT':
        goal_y -= 1
    return goal_x, goal_y


def get_position(objects_map, career):
    for k in range(len(objects_map)):
        for j in range(len(objects_map[0])):
            if career in objects_map[k][j]:
                return k, j


def get_career_num(objects_map, career):
    count = 0
    for k in range(len(objects_map)):
        for j in range(len(objects_map[0])):
            if career in objects_map[k][j]:
                count += 1
    return count


if __name__ == '__main__':
    map_num = 2
    input_dir = "input"
    inputs = os.listdir(input_dir)
    rows, columns, objects, cost = read_input(input_dir + os.sep + inputs[map_num])

    all_actions = []
    all_cost = 0
    all_deep = 0
    can_not = 0
    for z in range(get_career_num(objects, 'b')):
        start = get_position(objects, 'b')
        end = get_position(objects, 'p')
        if search(cost, objects, start, end) is None:
            can_not = True
            break
        path, search_c, deep = search(cost, objects, start, end)

        moves = convert_path_to_action(path)

        each_search_actions = []

        robot_cost = 0
        for i in range(len(path) - 1):
            robot_start = get_position(objects, 'r')
            robot_end = robot_goal(path[i], moves[i])
            if robot_end[0] < 0 or robot_end[1] < 0:
                can_not = True
                break
            if objects[robot_end[0]][robot_end[1]] == 'x':
                stop_point_x = path[i + 1][0]
                stop_point_y = path[i + 1][1]
                content = objects[stop_point_x][stop_point_y]
                objects[stop_point_x][stop_point_y] = 'x'
                if search(cost, objects, start, end) is None:
                    can_not = True
                    break
                path, search_c, tmp1 = search(cost, objects, start, end)
                moves = convert_path_to_action(path)
                objects[stop_point_x][stop_point_y] = content

                robot_end = robot_goal(path[i], moves[i])

            if search(cost, objects, robot_start, robot_end) is None:
                can_not = True
                break
            robot_path, one_cost, tmp2 = search(cost, objects, robot_start, robot_end)
            one_cost += cost[robot_end[0]][robot_end[1]]

            robot_cost += one_cost
            one_move = convert_path_to_action(robot_path)
            one_move.append(moves[i])
            each_search_actions.append(one_move)

            # update_robot_end
            robot_end_x = robot_end[0]
            robot_end_y = robot_end[1]
            if moves[i] == 'UP':
                robot_end_x -= 1
            elif moves[i] == 'DOWN':
                robot_end_x += 1
            elif moves[i] == 'LEFT':
                robot_end_y -= 1
            elif moves[i] == 'RIGHT':
                robot_end_y += 1

            objects[path[i][0]][path[i][1]] = 'n'
            objects[path[i + 1][0]][path[i + 1][1]] = 'b'
            objects[robot_start[0]][robot_start[1]] = 'n'
            objects[robot_end_x][robot_end_y] = 'r'

        if not can_not:
            all_actions.append(each_search_actions)
            all_cost += robot_cost
            if deep > all_deep:
                all_deep = deep
    if not can_not:
        robot_moves = ""
        for each_butter_action in all_actions:
            for actions in each_butter_action:
                for item in actions:
                    if item == 'UP':
                        robot_moves += "U "
                    elif item == 'DOWN':
                        robot_moves += "D "
                    elif item == 'LEFT':
                        robot_moves += "L "
                    elif item == 'RIGHT':
                        robot_moves += "R "

        print(robot_moves)
        print(all_cost)
        print(all_deep)
        res_path = "output"
        with open(res_path + os.sep + "result" + (str(map_num + 1)) + ".txt", "x") as f:
            f.write(robot_moves + "\n" + str(all_cost) + "\n" + str(all_deep))
    else:
        print("cant pass the butter")
