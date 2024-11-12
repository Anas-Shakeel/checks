""" Defines Task data model """

from datetime import datetime


class Task:
    last_id = 0

    def __init__(self, description: str,
                 task_id: int = None,
                 completed: bool = False,
                 created_at=None,
                 completed_at=None) -> None:
        self.id = task_id or Task.get_next_id()
        self.description = description
        self.completed = completed
        self.created_at = created_at or datetime.now().isoformat()
        self.completed_at = completed_at

    @classmethod
    def from_dict(cls, data: dict):
        """ Convert `data` dictionary to Task object. """
        cls.update_last_id(data["id"])
        return cls(
            id=data['id'],
            description=data['description'],
            completed=data['completed'],
            created_at=data['created_at'],
            completed_at=data.get('completed_at')
        )

    def to_dict(self) -> dict:
        """ Convert Task object to a dictionary """
        return {
            "id": self.id,
            "description": self.description,
            "completed": self.completed,
            "created_at": self.created_at,
            "completed_at": self.completed_at
        }

    @classmethod
    def get_next_id(cls):
        cls.last_id += 1
        return cls.last_id

    @classmethod
    def update_last_id(cls, task_id):
        cls.last_id = max(cls.last_id, int(task_id))
