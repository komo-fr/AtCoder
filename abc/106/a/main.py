#!/usr/bin/env python3

A, B = list(map(int, input().split()))

ans = A * B - (A + B - 1)
print(ans)
