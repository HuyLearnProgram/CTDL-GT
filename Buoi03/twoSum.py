import array


def twoSum(nums, target):
    pairs = []

    for i, num in enumerate(nums):
        remain = target - num
        for j, numb in enumerate(nums):
            if numb == remain and [i, j] not in pairs and [j, i] not in pairs:
                pairs.append([i, j])

    return pairs


if __name__ == "__main__":
    nums = [2, 6, 3, 9, 11]
    target = 9
    result = twoSum(nums, target)

    if result:
        for el in result:
            print(el)
    else:
        print("No pairs found.")
