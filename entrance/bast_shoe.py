current_string = ""
history = []
undo_history = []
undo_flag = False


def BastShoe(command: str) -> str:
    global current_string
    global history
    global undo_flag

    operation = command[0]
    argument = command[2:]

    if operation == "1":
        if undo_flag:
            undo_flag = False
            history = []
        return add(argument)

    if operation == "2":
        if undo_flag:
            undo_flag = False
            history = []
        return delete(int(argument))

    if operation == "3":
        return give(int(argument))

    if operation == "4":
        return undo()

    if operation == "5":
        return redo()

    return current_string


def add(string: str) -> str:
    global current_string
    global history
    global undo_history

    history.append(current_string)
    current_string += string
    undo_history = []
    return current_string


def delete(length: int) -> str:
    global current_string
    global history
    global undo_history

    history.append(current_string)
    current_string = current_string[:-length]
    undo_history = []
    return current_string


def give(index: int) -> str:
    global current_string

    if len(current_string) > index and len(current_string) > -index:
        return current_string[index]
    return ""


def undo() -> str:
    global current_string
    global history
    global undo_history
    global undo_flag

    undo_flag = True
    if len(history) > 0:
        undo_history.append(current_string)
        current_string = history.pop()
    return current_string


def redo() -> str:
    global current_string
    global undo_history

    if len(undo_history) > 0:
        history.append(current_string)
        current_string = undo_history.pop()
    return current_string
