"""
Инициализация пакета Class schedule manager.
Предоставляет быстрый доступ к основным классам: Event, Schedul, Teacher.
"""

from .event import Event
from .schedule import Schedule
from .teacher import Teacher

__all__ = ["Event", "Schedule", "Teacher"]

if __name__ == '__main__':

    ...
