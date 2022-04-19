def orientation(point1, point2, point3):
    # given three points p1, p2, p3 check orientation of (p1, p2) and (p2, p3)

    # return values:
    # 0: collinear points
    # 1: clockwise points
    # 2: counterclockwise points

    # slope between point 1 and 2: s12 = (y2 - y1)/(x2 - x1)
    # slope between point 2 and 3: s23 = (y3 - y2)/(x3 - x2)
    # if s12 > s23 => clockwise orientation
    # thus clockwise iff value = (y2 - y1)*(x3 - x2) - (y3 - y2)*(x2 - x1) > 0
    # counterclockwise iff value < 0
    # collinear iff value == 0

    result = None
    orientation_value = (float(point2.y - point1.y) * (point3.x - point2.x)) - (
            float(point2.x - point1.x) * (point3.y - point2.y))

    if orientation_value > 0:
        result = 1
    elif orientation_value < 0:
        result = 2
    elif orientation_value == 0:
        result = 0

    return result


def liesOnSegment(p1, p2, q):
    # given three collinear points p1, p2, q, check if
    # point q lies on segment (p1, p2)

    if ((q.x <= max(p1.x, p2.x)) and (q.x >= min(p1.x, p2.x)) and
            (q.y <= max(p1.y, p2.y)) and (q.y >= min(p1.y, p2.y))):
        return True
    return False


def intersects(p1, p2, q1, q2):
    # two segments (p1, p2) and (q1, q2) intersects iff one of the following two conditions is verified:

    # 1)  (p1, p2, q1) and (p1, p2, q2) have different orientations and (q1, q2, p1)
    # and (q1, q2, p2) have different orientations.

    # 2)  (p1, p2, q1), (p1, p2, q2), (q1, q2, p1), and (q1, q2, p2) are all collinear and
    # the x-projections of (p1, q1) and (p2, q2) intersect
    # the y-projections of (p1, q1) and (p2, q2) intersect

    result = False

    # find all orientations:
    orientation1 = orientation(p1, p2, q1)
    orientation2 = orientation(p1, p2, q2)
    orientation3 = orientation(q1, q2, p1)
    orientation4 = orientation(q1, q2, p2)

    # check case 1):
    if (orientation1 != orientation2) and (orientation3 != orientation4):
        result = True

    # check case 2) for each triplet
    elif orientation1 == 0 and liesOnSegment(p1, p2, q1):
        result = True
    elif (orientation2 == 0) and liesOnSegment(p1, p2, q2):
        result = True
    elif (orientation3 == 0) and liesOnSegment(q1, q2, p1):
        result = True
    elif (orientation4 == 0) and liesOnSegment(q1, q2, p2):
        result = True

    return result
