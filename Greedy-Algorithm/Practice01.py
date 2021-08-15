# 거스름돈

"""
카운터에서 거스름돈 500원 100원 50원 10원이 무한히 있을경우, 거슬러줘야 할 돈이 N 원일때 거슬러줘야 할 
돈의 최소 갯수를 구하여라.

-> 가장 큰 화폐 단위 부터 돈을 거슬러 준다는 것. 
"""


def solution(n):

    coin_types = [500, 100, 50, 10]

    count = 0

    for coin in coin_types:

        count += n // coin
        n %= coin

    return count

    
