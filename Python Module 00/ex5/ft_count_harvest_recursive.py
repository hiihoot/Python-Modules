def ft_count_harvest_recursive():
    day = int(input("Days until harvest: "))

    def counter(curr_day):
        if curr_day > day:
            print("Harvest time!")
            return
        print(f"Day {curr_day}")
        counter(curr_day + 1)
    counter(1)
