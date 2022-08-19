class Grid:
    nx = 0
    ny = 0
    nz = 0
    properties = {}

    def __init__(self, nx, ny, nz):
        self.nx = nx
        self.ny = ny
        self.nz = nz

    # def get_property()


class Property:
    name = ""
    values = []

    def __init__(self, name, values):
        self.name = name
        self.valus = values
