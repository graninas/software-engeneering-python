# 12 Design Patterns II

### Visitor

class Cell:
    def __init__(self, l, r, u, d):
        self._left = l
        self._right = r
        self._up = u
        self._down = d

    def setLeftWall(self, opened):
        self._left = opened

    def setRightWall(self, opened):
        self._right = opened

    def setUpWall(self, opened):
        self._up = opened

    def setDownWall(self, opened):
        self._down = opened


class Labyrinth:
    def __init__(self, lab):
        self._labyrinth_dict = lab

    def get_labyrinth_dict(self):
        return self._labyrinth_dict

internal_labyrinth_dict = {
  (0,0): Cell(True, True, True, True),
  (1,0): Cell(True, True, False, True),
  (0,1): Cell(True, True, True, True),
  (1,1): Cell(True, True, True, False)
  }

labyrinth_dict = {
  (0,0): Cell(True, True, True, True),
  (1,0): Cell(True, True, True, True),
  (0,1): Cell(True, True, True, True),
  (1,1): Labyrinth(internal_labyrinth_dict)
  }

labyrinth = Labyrinth(labyrinth_dict)


def allWalls(cell):
    return cell._left and cell._right and cell._up and cell._down


class EnclosedCellsCounterVisitor:
    def __init__(self):
        self._enclosed_cells = 0

    def reset(self):
        self._enclosed_cells = 0

    def visitCell(self, cell):
        if (isinstance(cell, Cell)):
            if (allWalls(cell)):
                self._enclosed_cells += 1
        else:
            raise Exception("Invalid argument: not a cell")

    def visitLabyrinth(self, lab):
        if (isinstance(lab, Labyrinth)):
            for k, v in lab.get_labyrinth_dict().items():
                self.visit(v)
        else:
            raise Exception("Invalid argument: not a labyrinth")

    def visit(self, lab_item):
        if (isinstance(lab_item, Labyrinth)):
            self.visitLabyrinth(lab_item)

        if (isinstance(lab_item, Cell)):
            self.visitCell(lab_item)

        if (not isinstance(lab_item, Labyrinth)
            and not isinstance(lab_item, Cell)):
                raise Exception("Invalid argument: not a cell, not a labyrinth")

    def get_result(self):
        return self._enclosed_cells



class CellWallVisitor:
    def __init__(self): pass

    def visitCell(self, cellOpened, cell):
        if (isinstance(cell, Cell)):
            cell.setLeftWall(cellOpened)
            cell.setRightWall(cellOpened)
            cell.setUpWall(cellOpened)
            cell.setDownWall(cellOpened)
        else:
            raise Exception("Invalid argument: not a cell")

    def visitLabyrinth(self, cellOpened, lab):
        if (isinstance(lab, Labyrinth)):
            for k, v in lab.get_labyrinth_dict().items():
                self.visit(v, cellOpened)
        else:
            raise Exception("Invalid argument: not a labyrinth")

    def visit(self, cellOpened, lab_item):
        if (isinstance(lab_item, Labyrinth)):
            self.visitLabyrinth(cellOpened, lab_item)

        if (isinstance(lab_item, Cell)):
            self.visitCell(cellOpened, lab_item)


print(labyrinth.get_labyrinth_dict())

visitor = EnclosedCellsCounterVisitor()
visitor.visit(labyrinth)
print(visitor.get_result())

wallVisitor = CellWallVisitor()         # bug?
wallVisitor.visit(False, labyrinth)

visitor.reset()
visitor.visit(labyrinth)
print(visitor.get_result())
