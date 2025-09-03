def sort_on(items):
    return items["count"]


def sort_arr(arr):
    arr.sort(reverse=True, key=sort_on)
    return arr