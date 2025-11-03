day = int(input("enter your day: "))
#match-case
match day:
    case 1:
        print("day is Monday")
    case 2:
        print("day is Tuesday")
    case 3:
        print("day is Wednesday")
    case 4:
        print("day is Thursday")
    case 5:
        print("day is Friday")
    case 6:
        print("day is Saturday")
    case 7:
        print("day is Sunday")
    case _:
        print("invalid day")