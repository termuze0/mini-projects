import matplotlib.pyplot as plt

def visualize_array(arr, title):
    plt.bar(range(len(arr)), arr)
    plt.title(title)
    plt.show()
    
def three_way_merge_sort_visualized(arr, depth=0):
    if len(arr) < 2:
        return arr

    visualize_array(arr, f"Splitting: {arr}")
    
    one_third = len(arr) // 3
    two_third = 2 * one_third
    
    left = arr[:one_third]
    middle = arr[one_third:two_third]
    right = arr[two_third:]
    
    left = three_way_merge_sort_visualized(left, depth+1)
    middle = three_way_merge_sort_visualized(middle, depth+1)
    right = three_way_merge_sort_visualized(right, depth+1)
    
    merged = merge_three(left, middle, right)
    
    visualize_array(merged, f"Merging: {merged}")
    return merged
