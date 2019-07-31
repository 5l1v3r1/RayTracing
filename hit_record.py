class HitRecord:
    def __init__(self, t=None, p=None, normal=None):
        """
        :type t: float
        :type p: Vector
        :type normal: Vector
        """
        self.t = t
        self.p = p
        self.normal = normal
