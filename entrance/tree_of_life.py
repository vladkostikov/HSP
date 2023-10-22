def TreeOfLife(_height: int, _weight: int, years_of_modeling: int, starting_tree: list) -> list:
    tree = convert_starting_tree(starting_tree)

    for year in range(years_of_modeling):
        tree = continue_growth(tree)
        if (year % 2) == 1:
            tree = mark_branches_for_destruction(tree)
            tree = destroy_old_branches(tree)

    final_tree = convert_to_final_tree(tree)
    return final_tree


def convert_starting_tree(tree):
    new_tree = []
    for _index_line, line in enumerate(tree):
        new_line = []
        for char in line:
            if char == "+":
                new_line.append([1, "Young"])
                continue
            new_line.append([0, "Young"])
        new_tree.append(new_line)
    return new_tree


def continue_growth(tree: list) -> list:
    new_tree = []
    for _index_line, line in enumerate(tree):
        new_line = []
        for branch in line:
            new_age = branch[0] + 1
            new_branch_status = branch[1]
            if new_age >= 3:
                new_branch_status = "Old"
            new_line.append([new_age, new_branch_status])
        new_tree.append(new_line)
    return new_tree


def mark_branches_for_destruction(tree: list) -> list:
    for index_line, line in enumerate(tree):
        for index_branch, branch in enumerate(line):
            if branch[1] != "Old":
                continue

            side_branches = []
            if index_line > 0:
                upper_branch = tree[index_line - 1][index_branch]
                side_branches.append(upper_branch)

            if index_line < (len(tree) - 1):
                lower_branch = tree[index_line + 1][index_branch]
                side_branches.append(lower_branch)

            if index_branch > 0:
                left_branch = tree[index_line][index_branch - 1]
                side_branches.append(left_branch)

            if index_branch < (len(line) - 1):
                right_branch = tree[index_line][index_branch + 1]
                side_branches.append(right_branch)

            for side_branch in side_branches:
                if side_branch[1] == "Young":
                    side_branch[1] = "Destroy"
    return tree


def destroy_old_branches(tree: list) -> list:
    for index_line, line in enumerate(tree):
        for index_branch, branch in enumerate(line):
            if (branch[1] == "Old") or (branch[1] == "Destroy"):
                branch[0] = 0
                branch[1] = "Young"
    return tree


def convert_to_final_tree(tree: list) -> list:
    final_tree = []
    for _index_line, line in enumerate(tree):
        new_line_elements = []
        for branch in line:
            if branch[0] > 0:
                branch = "+"
                new_line_elements.append(branch)
                continue
            branch = "."
            new_line_elements.append(branch)
        new_line = "".join(new_line_elements)
        final_tree.append(new_line)
    return final_tree
