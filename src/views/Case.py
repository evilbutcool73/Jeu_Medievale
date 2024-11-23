from ..views.Type import TYPE

class Case:
    def __init__(self, x=0, y=0, type=TYPE.plaine, villageproprio=None, lhabitant=None) -> None:
        self.x = x
        self.y = y
        self.type = type
        self.villageproprio = villageproprio
        self.lhabitant = lhabitant