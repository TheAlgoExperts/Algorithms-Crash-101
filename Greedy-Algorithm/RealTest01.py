"""
실전 문제 

큰수의 법칙 

첫번째 라인에 n,m,k 로 공백으로 구분하여 입력 받고, 

두번째 라인에는 하나의 배열을 공백으로 구분하여 입력받는다. 

n개의 배열에 있는 수 중에 하나를 골라, m 번씩 더하는데, 배열중 하나의 숫자는 k 번 밖에 더하지 못한다. 

만들수 있는 가장 큰 수를 구하라.
"""


def solution():

    number = 0

    n, m, k = map(int, input().split())

    data = list(map(int, input().split()))

    data.sort()

    return number
