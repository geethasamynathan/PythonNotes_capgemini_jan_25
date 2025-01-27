# Python filter() function
# Sometimes, you need to iterate over elements of a list and select some of them based on specified criteria.

# # example without filter 
# scores = [70, 60, 80, 90, 50]

# filtered = []

# for score in scores:
#     if score >= 70:
#         filtered.append(score)

# print(filtered)


# # example using  filter method
# scores = [70, 60, 80, 90, 50]
# filtered = filter(lambda score: score >= 70, scores)

# print(list(filtered))


# filter() function to filter a list of tuples

countries = [
    ['China', 1394015977],
    ['United States', 329877505],
    ['India', 1326093247],
    ['Indonesia', 267026366],
    ['Bangladesh', 162650853],
    ['Pakistan', 233500636],
    ['Nigeria', 214028302],
    ['Brazil', 21171597],
    ['Russia', 141722205],
    ['Mexico', 128649565]
]

populated = filter(lambda c: c[1] > 300000000, countries)

print(list(populated))
