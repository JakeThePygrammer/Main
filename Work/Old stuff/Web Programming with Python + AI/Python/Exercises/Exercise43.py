def test_points(points=0):
    if points <= 50:
        return "Failed."
    else:
        return "Passed."

points = int(input("Enter test score : "))
print(test_points(points))