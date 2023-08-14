def get_line(x0, y0, x1, y1):
    points = []

    dx = abs(x1 - x0)
    dy = abs(y1 - y0)
    inclinacion = dy > dx

    if inclinacion:
        x0, y0 = y0, x0
        x1, y1 = y1, x1
        dx, dy = dy, dx

    if x0 > x1:
        x0, x1 = x1, x0
        y0, y1 = y1, y0

    p = 2 * dy - dx
    y = y0

    for x in range(x0, x1 + 1):
        if inclinacion:
            points.append((y, x))
        else:
            points.append((x, y))
        
        if p >= 0:
            y += 1 if y0 < y1 else -1
            p -= 2 * dx
        
        p += 2 * dy

    return points

if __name__ == "__main__":
    print(get_line(2, 2, 10, 5))