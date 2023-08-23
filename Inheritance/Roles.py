from enum import Enum


class Roles(Enum):
    MANAGER = 1
    SECRETARY = 2
    ENGINEER = 3
    DIRECTOR = 4


Roles = Enum('Roles', ['MANAGER', 'SECRETARY', 'ENGINEER', 'DIRECTOR'])
