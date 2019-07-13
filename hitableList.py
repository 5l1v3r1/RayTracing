from hitable import Hitable


class HitableList(Hitable):
    def __init__(self, list):
        self.list = list

    def hit(self, r, tMin, tMax):
        closestSoFar = tMax
        rec = None
        for h in self.list:
            tempRec = h.hit(r, tMin, closestSoFar)
            if tempRec is not None:
                closestSoFar = tempRec.t
                rec = tempRec
        return rec