#https://leetcode.com/problems/kids-with-the-greatest-number-of-candies/description/
def kidsWithCandies(candies: list[int], extraCandies: int) -> list[bool]:
    # Find the maximum number of candies any kid currently has
    maxCandies = max(candies)

    result = []
    for candy in candies:

        if candy + extraCandies >= maxCandies:
            result.append(True)
        else:
            result.append(False)

    return result

candies = [2, 3, 5, 1, 3]
extraCandies = 3
result = kidsWithCandies(candies, extraCandies)
print(result)  
