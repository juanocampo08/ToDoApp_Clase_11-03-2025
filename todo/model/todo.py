class Todo:
    def __init__(self, code_id: int,title: str, description: str):
        self.code_id: int = code_id
        self.title: str = title
        self.description: str = description
        self.completed: bool = False
        self.tags: list[str] = []

    def mark_completed(self):
        if self.completed == False:
            self.completed = True
        else:
            return self.completed

    def add_tag(self, tag: str):

        if tag not in self.tags:
            self.tags.append(tag)
        else:
            return

    def __str__(self):
        return str(f"{self.code_id} - {self.title}")


class TodoBook:
    def __init__(self):
        self.todos: dict[int,Todo] = {}

    def add_todo(self, title: str, description:  str) -> int:
        nuevo_id: int = len(self.todos) + 1
        todo = Todo(nuevo_id, title, description)
        self.todos[nuevo_id] = todo
        return nuevo_id

    def pending_todos(self) -> list[Todo]:
        pending_todos = [todo for todo in self.todos.values() if todo.completed == False]
        return pending_todos

    def completed_todos(self) -> list[Todo]:
        completed_todo = [todo for todo in self.todos.values() if todo.completed == True]
        return completed_todo

    def tags_todo_count(self) -> dict[str, int]:
        tags_count: dict[str, int] = dict()
        for todo in self.todos.values():
            for tag in todo.tags:
                if tag in tags_count:
                    tags_count[tag] += 1
                else:
                    tags_count[tag] = 1
        return tags_count
