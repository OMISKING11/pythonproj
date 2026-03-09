import math

# secdis.py
# GitHub Copilot

def distance(p1, p2):
    """Return Euclidean distance between points p1 and p2.
    p1, p2: (x, y) tuples or lists of numbers.
    """
    x1, y1 = p1
    x2, y2 = p2
    return math.hypot(x2 - x1, y2 - y1)

def section_point(p1, p2, m=None, n=None, pt=None, external=False):
    """
    If m and n are given, returns the point dividing p1-p2 in m:n.
    If pt is given, returns the ratio (m:n) in which pt divides p1-p2.
    """
    x1, y1 = p1
    x2, y2 = p2
    if pt is not None:
        x, y = pt
        if external:
            denom_x = x2 - x1
            if denom_x == 0:
                raise ValueError("Cannot compute ratio: x2 - x1 is zero")
            m = (x - x1) / (x2 - x1)
            n = (x - x2) / (x1 - x2)
        else:
            denom_x = x2 - x1
            if denom_x == 0:
                raise ValueError("Cannot compute ratio: x2 - x1 is zero")
            m = (x - x1) / (x2 - x1)
            n = 1 - m
        return (m, n)
    else:
        if m is None or n is None:
            raise ValueError("m and n must be provided if pt is not given")
        if external:
            denom = m - n
            if denom == 0:
                raise ValueError("m - n must not be 0 for external division")
            x = (m * x2 - n * x1) / denom
            y = (m * y2 - n * y1) / denom
        else:
            denom = m + n
            if denom == 0:
                raise ValueError("m + n must not be 0 for internal division")
            x = (m * x2 + n * x1) / denom
            y = (m * y2 + n * y1) / denom
        return (x, y)

def _read_point(prompt):
    s = input(prompt + " (format: x y): ").strip()
    x_str, y_str = s.split()
    return (float(x_str), float(y_str))

def main():
    """Interactive loop: choose distance or section repeatedly."""
    while True:
        print("\nChoose operation:")
        print("1) Distance between two points")
        print("2) Section formula")
        print("3) Quit")
        choice = input("Enter 1/2/3: ").strip()
        if choice == "1":
            try:
                p1 = _read_point("Enter point 1")
                p2 = _read_point("Enter point 2")
                d = distance(p1, p2)
                print(f"Distance: {d}")
            except Exception as e:
                print("Error:", e)
        elif choice == "2":
            print("\nSection formula options:")
            print("a) Find coordinates of the point dividing the segment in a given ratio")
            print("b) Find the ratio in which a given point divides the segment")
            sub_choice = input("Enter a/b: ").strip().lower()
            try:
                p1 = _read_point("Enter point 1")
                p2 = _read_point("Enter point 2")
                ext = input("External division? (y/N): ").strip().lower() == "y"
                if sub_choice == "a":
                    m = float(input("Enter m (first weight): ").strip())
                    n = float(input("Enter n (second weight): ").strip())
                    pt = section_point(p1, p2, m=m, n=n, external=ext)
                    print(f"Section point: {pt}")
                elif sub_choice == "b":
                    pt = _read_point("Enter the dividing point")
                    ratio = section_point(p1, p2, pt=pt, external=ext)
                    print(f"Ratio (m:n) in which the point divides the segment: {ratio[0]} : {ratio[1]}")
                else:
                    print("Invalid option.")
            except Exception as e:
                print("Error:", e)
        elif choice == "3":
            break
        else:
            print("Invalid choice. Enter 1, 2, or 3.")

if __name__ == "__main__":
    main()