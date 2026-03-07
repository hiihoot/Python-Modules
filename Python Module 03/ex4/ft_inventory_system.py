import sys


def up_len(text: str):
    ln = 0
    for i in text:
        if i == ":":
            return ln
        ln += 1


def main():
    print("=== Inventory System Analysis ===")
    argv = sys.argv[1:]
    data = {}
    scarce = {}
    moderate = {}

    most_abundant_value = 0
    most_abundant_name = ""
    last_abundant_value = 0
    last_abundant_name = ""
    restock_needed = ""

    for i in argv:
        data[i[:up_len(i)]] = i[up_len(i) + 1:]
    total_items = 0
    items = len(data)
    for v in data.values():
        total_items += int(v)
    print(f"Total items in inventory: {total_items}")
    print(f"Unique item types: {items}")
    print("\n=== Current Inventory ===")
    for k, v in data.items():
        percentage = (int(v)/total_items) * 100
        print(f"{k}: {v} units ({percentage:.1f}%)")
        if (int(v) > most_abundant_value):
            most_abundant_value = int(v)
            most_abundant_name = k
        else:
            last_abundant_value = int(v)
            last_abundant_name = k
        if (percentage < 30):
            scarce[k] = v
            if int(v) == 1:
                restock_needed += k + ", "
        else:
            moderate[k] = v

    print("\n=== Inventory Statistics ===")
    print(f"Most abundant: {most_abundant_name} ({most_abundant_value} units)")
    print(f"Last abundant: {last_abundant_name} ({last_abundant_value} units)")

    print("\n=== Item Categories ===")
    print(f"Moderate: {moderate}")
    print(f"Scarce: {scarce}")

    print("\n=== Management Suggestions ===")
    print(f"Restock needed: {restock_needed[:-2]}")
    print("\n=== Dictionary Properties Demo ===")
    dic_values = ""
    dic_keys = ""
    for k in data.keys():
        items -= 1
        if items <= 0:
            dic_values += data[k]
            dic_keys += k
        else:
            dic_values += data[k] + ", "
            dic_keys += k + ", "
    print(f"Dictionary keys: {dic_keys}")
    print(f"Dictionary value: {dic_values}")
    name = "sword"
    for k in data.keys():
        if k == name:
            print(f"Sample lookup - '{k}' in inventory: True")


if __name__ == "__main__":
    main()
