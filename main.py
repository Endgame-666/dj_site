def get_cells(x1, y1, x2, y2):
    cells = set()
    for x in range(x1, x2):
        for y in range(y1, y2):
            cells.add((x, y))
    return cells


def expand(prev, w, h):
    expanded = set()
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    for (x, y) in prev:
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 1 <= nx <= w and 1 <= ny <= h:
                expanded.add((nx, ny))
    return expanded


def solve():
    w, h = list(map(int, input().split()))
    n = int(input())

    if n == 0:
        print("Yes")
        return

    x1, y1, x2, y2 = list(map(int, input().split()))
    cur = get_cells(x1, y1, x2, y2)

    for _ in range(n - 1):
        x1, y1, x2, y2 = list(map(int, input().split()))
        next_frame = get_cells(x1, y1, x2, y2)
        reachable = expand(cur, w, h)
        next_possible = reachable & next_frame

        if not next_possible:
            print("Yes")
            return

        cur = next_possible

    print("Yes")

solve()

