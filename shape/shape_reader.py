import shapefile


def sread():
    sf = shapefile.Reader("fm")
    shapes = sf.shapes()
    print type(shapes)

if __name__ == '__main__':
    sread()



