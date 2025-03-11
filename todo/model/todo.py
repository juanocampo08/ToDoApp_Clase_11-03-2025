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


