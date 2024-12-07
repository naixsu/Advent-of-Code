print(
    "Score: ",
    sum(
        abs(int(x1[:5]) - int(x2[8:-1]))
        for x1, x2 in zip(
            sorted(open("day_2/test.txt").readlines(), key=lambda x: int(x.split()[0])),
            sorted(open("day_2/test.txt").readlines(), key=lambda x: int(x.split()[1])),
        )
    ),
    "\nDistance: ",
    sum(
        int(vl1[:5])
        * sum(
            1 for vl2 in open("day_2/test.txt").readlines() if int(vl2[8:-1]) == int(vl1[:5])
        )
        for vl1 in open("day_2/test.txt").readlines()
    ),
)