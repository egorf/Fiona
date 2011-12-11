# testing geometry extension, to be called by nosetests

import unittest

from fiona.ogrext import GeomBuilder

def geometry_wkb(wkb):
    return GeomBuilder().build_wkb(wkb)

class PointTest(unittest.TestCase):
    def test_point(self):
        # Hex-encoded Point (0 0)
        wkb = "010100000000000000000000000000000000000000".decode('hex')
        geom = geometry_wkb(wkb)
        self.failUnlessEqual(geom['type'], "Point")
        self.failUnlessEqual(geom['coordinates'], (0.0, 0.0))
class LineStringTest(unittest.TestCase):
    def test_line(self):
        # Hex-encoded LineString (0 0, 1 1)
        wkb = "01020000000200000000000000000000000000000000000000000000000000f03f000000000000f03f".decode('hex')
        geom = geometry_wkb(wkb)
        self.failUnlessEqual(geom['type'], "LineString")
        self.failUnlessEqual(geom['coordinates'], [(0.0, 0.0), (1.0, 1.0)])
class PolygonTest(unittest.TestCase):
    def test_polygon(self):
        # 1 x 1 box (0, 0, 1, 1)
        wkb = "01030000000100000005000000000000000000f03f0000000000000000000000000000f03f000000000000f03f0000000000000000000000000000f03f00000000000000000000000000000000000000000000f03f0000000000000000".decode('hex')
        geom = geometry_wkb(wkb)
        self.failUnlessEqual(geom['type'], "Polygon")
        self.failUnlessEqual(len(geom['coordinates']), 1)
        self.failUnlessEqual(len(geom['coordinates'][0]), 5)
        x, y = zip(*geom['coordinates'][0])
        self.failUnlessEqual(min(x), 0.0)
        self.failUnlessEqual(min(y), 0.0)
        self.failUnlessEqual(max(x), 1.0)
        self.failUnlessEqual(max(y), 1.0)
class MultiPointTest(unittest.TestCase):
    def test_multipoint(self):
        wkb = "0104000000020000000101000000000000000000000000000000000000000101000000000000000000f03f000000000000f03f".decode('hex')
        geom = geometry_wkb(wkb)
        self.failUnlessEqual(geom['type'], "MultiPoint")
        self.failUnlessEqual(geom['coordinates'], [(0.0, 0.0), (1.0, 1.0)])
class MultiLineStringTest(unittest.TestCase):
    def test_multilinestring(self):
        # Hex-encoded LineString (0 0, 1 1)
        wkb = "01050000000100000001020000000200000000000000000000000000000000000000000000000000f03f000000000000f03f".decode('hex')
        geom = geometry_wkb(wkb)
        self.failUnlessEqual(geom['type'], "MultiLineString")
        self.failUnlessEqual(len(geom['coordinates']), 1)
        self.failUnlessEqual(len(geom['coordinates'][0]), 2)
        self.failUnlessEqual(geom['coordinates'][0], [(0.0, 0.0), (1.0, 1.0)])
class MultiPolygonTest(unittest.TestCase):
    def test_multipolygon(self):
        # [1 x 1 box (0, 0, 1, 1)]
        wkb = "01060000000100000001030000000100000005000000000000000000f03f0000000000000000000000000000f03f000000000000f03f0000000000000000000000000000f03f00000000000000000000000000000000000000000000f03f0000000000000000".decode('hex')
        geom = geometry_wkb(wkb)
        self.failUnlessEqual(geom['type'], "MultiPolygon")
        self.failUnlessEqual(len(geom['coordinates']), 1)
        self.failUnlessEqual(len(geom['coordinates'][0]), 1)
        self.failUnlessEqual(len(geom['coordinates'][0][0]), 5)
        x, y = zip(*geom['coordinates'][0][0])
        self.failUnlessEqual(min(x), 0.0)
        self.failUnlessEqual(min(y), 0.0)
        self.failUnlessEqual(max(x), 1.0)
        self.failUnlessEqual(max(y), 1.0)
