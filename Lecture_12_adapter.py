# 12 Design Patterns II

# Adapter


class ICell:
    def get_left_wall(self): pass
    def get_right_wall(self): pass
    def get_up_wall(self): pass
    def get_down_wall(self): pass

class ILabyrinth:
    def get_labyrinth_dict(self): pass


class Cell(ICell):
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

    def get_left_wall(self):
        return self._left
    def get_right_wall(self):
        return self._right
    def get_up_wall(self):
        return self._up
    def get_down_wall(self):
        return self._down


class Labyrinth(ILabyrinth):
    def __init__(self, lab):
        self._labyrinth_dict = lab

    def get_labyrinth_dict(self):
        return self._labyrinth_dict


def allWalls(cell):
    if (isinstance(cell, ICell)):
        return cell.get_left_wall() and cell.get_right_wall() and cell.get_up_wall() and cell.get_down_wall()
    else:
        raise Exception("Not a ICell")



class EnclosedCellsCounterVisitor:
    def __init__(self):
        self._enclosed_cells = 0

    def reset(self):
        self._enclosed_cells = 0

    def visitCell(self, cell):
        if (isinstance(cell, ICell)):
            if (allWalls(cell)):
                self._enclosed_cells += 1
        else:
            raise Exception("Invalid argument: not a cell")

    def visitLabyrinth(self, lab):
        if (isinstance(lab, ILabyrinth)):
            for k, v in lab.get_labyrinth_dict().items():
                self.visit(v)
        else:
            raise Exception("Invalid argument: not a labyrinth")

    def visit(self, lab_item):
        if (isinstance(lab_item, ILabyrinth)):
            self.visitLabyrinth(lab_item)

        if (isinstance(lab_item, ICell)):
            self.visitCell(lab_item)

        if (not isinstance(lab_item, ILabyrinth)
            and not isinstance(lab_item, ICell)):
                raise Exception("Invalid argument: not a cell, not a labyrinth")

    def get_result(self):
        return self._enclosed_cells

######################################33

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


# print(labyrinth.get_labyrinth_dict())
#
# visitor = EnclosedCellsCounterVisitor()
# visitor.visit(labyrinth)
# print(visitor.get_result())



#####################################

# Suppose we can't change these classes:
class GCell:
    def __init__(self, content):
        self._content = content

class GCellLabyrinth:
    def __init__(self, lab):
        self._labyrinth_dict = lab

    def get_labyrinth_dict(self):
        return self._labyrinth_dict

########################################

# We need an adapter:

class GCellAdapter(ICell):
    def __init__(self, gcell):
        if (isinstance(gcell, GCell)):
            self._gcell = gcell
        else:
            raise Exception("Not a GCell.")

    def get_left_wall(self):
        return self._gcell._content.count("l") == 1

    def get_right_wall(self):
        return self._gcell._content.count("r") == 1

    def get_up_wall(self):
        return self._gcell._content.count("u") == 1

    def get_down_wall(self):
        return self._gcell._content.count("d") == 1

class GCellLabyrinthAdapter(ILabyrinth):
    def __init__(self, gcelllab):
        if (isinstance(gcelllab, GCellLabyrinth)):
            self._gcelllab = gcelllab
        else:
            raise Exception("Not a GCell labyrinth.")

    def get_labyrinth_dict(self):
        adapted_dict = dict()
        for k, v in self._gcelllab.get_labyrinth_dict().items():
            adapted_dict[k] = GCellAdapter(v)
        return adapted_dict


##########################################

gcell_lab_dict = {
    (0,0): GCell("lrud"),
    (1,0): GCell("rd"),
    (0,1): GCell("lrud"),
    (1,1): GCell("lr")
    }

gcell_lab = GCellLabyrinth(gcell_lab_dict)

adapted_gcell_lab = GCellLabyrinthAdapter(gcell_lab)

visitor = EnclosedCellsCounterVisitor()
visitor.visit(adapted_gcell_lab)
print(visitor.get_result())
