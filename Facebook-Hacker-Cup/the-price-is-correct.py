# Facebook Hacker Cup 2016 Qualification Round
# The price is correct

games = int(input())


for game in range(games):
    volume, maxi = [int(x) for x in input().split()]
    case = [int(x) for x in input().split()]

    ANS = 0
    i, j = 0, 0
    window_sum = sum(case[i:j])
    while i < volume > j:
        if window_sum <= maxi and j >= i:
            ANS += j-i
            if j < volume:
                window_sum += case[j]
                j += 1
            else:
                break # reached the end
        else:
            window_sum -= case[i]
            i += 1


    print("Case #{}: {}".format(game+1, ANS))


