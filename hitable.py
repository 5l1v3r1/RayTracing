
class Hitable(object):
	"""This hitable abstract class has a hit function that takes in a ray.
	Most ray tracers have found it convenient to add a valid 
	interval for hits tmin to tmax, so the hit only “counts” if
	tmin < t < tmax"""
	def hit(self, r, tMin, tMax):
	    """
	    type r: Ray
	    type tMin: float
	    type tMax: float
	    """
	    raise NotImplementedError()