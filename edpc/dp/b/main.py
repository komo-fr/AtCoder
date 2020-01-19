#!/usr/bin/env python3

N, K = list(map(int, input().split()))
h_list = list(map(int, input().split()))
dp_list = [float("inf")] * N
dp_list[0] = 0

for i in range(1, N):
    # j番目の足場からi番目の足場に飛ぶ

    for j in range(max(i - K, 0), i + 1):

        # j番目の足場までの最適コスト
        cum_cost = dp_list[j]

        # j番目の足場から飛んだ場合のコスト
        cost = dp_list[j] + abs(h_list[j] - h_list[i])

        # 最適コストで更新
        dp_list[i] = min(dp_list[i], cost)

ans = dp_list[-1]
print(ans)
