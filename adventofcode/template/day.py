def part1(data: list[str]) -> int:
    ans = 0

    print(ans)
    return ans


def part2(data: list[str]) -> int:
    ans = 0

    print(ans)
    return ans


def test_passing():
    with open("test.txt", "r") as f:
        data = f.read().splitlines()
        assert part1(data) == 0
        assert part2(data) == 0
        f.close()


with open("day.txt", "r") as f:
    data = f.read().splitlines()

    part1(data)

    part2(data)

    test_passing()

    f.close()
