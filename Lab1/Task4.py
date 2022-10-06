import argparse

def main():
    parser = argparse.ArgumentParser()

    parser.add_argument("-W",  type=int)
    parser.add_argument("-w", nargs="+", type=int)
    
    args = parser.parse_args()
    
    capacity = args.W
    bricks = args.w

    if sum(bricks) <= capacity:
        print(sum(bricks))
        
    elif any(brick == capacity for brick in bricks):
        print(capacity)
        
    else:
        temp = bricks.copy()
        optimal_weight = 0
        while True:
            min_max_value = max(temp)
            if min_max_value > capacity:
                 temp.remove(min_max_value)
            else:
                optimal_weight += min_max_value
                break
        
        bricks.remove(min_max_value)
        for i in bricks:
            if optimal_weight + i > capacity:
                continue
            else:
                optimal_weight += i
        
        print(optimal_weight)
        
if __name__ == '__main__':
    main()
