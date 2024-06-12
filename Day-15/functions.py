def get_todo(filepath):
    with open(filepath, 'r') as local_file:
        local_todos = local_file.readlines()
    return local_todos


def write_tods(filepath, todo_arg):
    with open(filepath, 'w') as local_file:
        local_file.writelines(todo_arg)

