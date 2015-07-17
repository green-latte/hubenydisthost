import math

class TerrestrialCoordinate(object):
  """ [TODO] class description
  """
  def __init__(self, x, y):
    self.x = x
    self.y = y

class Ellipsoid(object):
  """ [TODO] class description
  """
  long_radius = 0.0
  short_radius = 0.0
  reciprocal_flat_rate = 0.0
  major_eccentricity = 0.0

  @classmethod
  def constant(cls):
    return cls.long_radius * (1.0 - major_eccentricity)

  # @property
  # def major_eccentricity(self):
  #   lr_sqr = math.pow(self.long_radius, 2)
  #   sr_sqr = math.pow(self.short_radius, 2)
  #   return math.sqrt((lr_sqr - sr_sqr) / 2.0)

class BesselEllipsoid(Ellipsoid):
  """ [TODO] class description
  """
  long_radius = 6377397.155
  short_radius = 6356079.0
  reciprocal_flat_rate = 299.152813
  major_eccentricity = 0.00667436061028297

  def __init__(self):
    super(Ellipsoid, self).__init__()

class GRS80(Ellipsoid):
  """ [TODO] class description
  """
  long_radius = 6378137.0
  short_radius = 6356752.31414
  reciprocal_flat_rate = 298.257222101
  major_eccentricity = 0.00669438002301188

  def __init__(self):
    super(Ellipsoid, self).__init__()

class WGS84(Ellipsoid):
  """ [TODO] class description
  """
  long_radius = 6378137.0
  short_radius = 6356752.314245
  reciprocal_flat_rate = 298.257223563
  major_eccentricity = 0.00669437999019758

  def __init__(self):
    super(Ellipsoid, self).__init__()

class Hubeny(object):
  """ [TODO] class description
  """

  def __init__(self, start, end, ellips):
    """ [TODO] constructor
    """
    self.start = start
    self.end = end
    self.ellipsoid = ellips

  def distance(self):
    """ [TODO] instance method
    """
    dx = math.radians(self.start.x - self.end.x)
    dy = math.radians(self.start.y - self.end.y)
    my = math.radians((self.start.y + self.end.y) / 2.0)
    W = math.sqrt(1.0 - self.ellipsoid.major_eccentricity * math.pow(math.sin(my), 2))
    M = self.ellipsoid.long_radius * (1.0 - self.ellipsoid.major_eccentricity) / math.pow(W, 3)
    N = self.ellipsoid.long_radius / W
    dist = math.sqrt(math.pow(dy*M, 2) + math.pow(dx*N*math.cos(my), 2))
    return dist

if __name__ == '__main__':
  start = TerrestrialCoordinate(140.09111, 36.10056)
  end = TerrestrialCoordinate(130.36208, 33.59532)
  hubeny = Hubeny(start, end, BesselEllipsoid)
  print hubeny.distance()
