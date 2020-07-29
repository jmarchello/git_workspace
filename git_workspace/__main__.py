import urwid


def __main__():
    repo_list = build_repo_list()
    menu = build_menu()
    container = urwid.Columns(
        [("weight", 3, repo_list), ("weight", 1, menu)], dividechars=1, min_width=10,
    )
    loop = urwid.MainLoop(container)
    loop.run()


def build_menu():
    menu = urwid.SimpleFocusListWalker([urwid.Text("Menu")])
    return urwid.ListBox(menu)


def build_repo_list():
    repo_list = urwid.SimpleFocusListWalker([urwid.Text("Repositories")])
    return urwid.ListBox(repo_list)


if __name__ == "__main__":
    __main__()
