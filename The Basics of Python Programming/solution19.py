n = int(input())

augustSet = {str(x) for x in range(1, n + 1)}
beatriceSet = set(input().split())
augustAnswer = set(input().split())

while beatriceSet != {'HELP'}:
    if augustAnswer == {'YES'}:
        augustSet &= beatriceSet
    if augustAnswer == {'NO'}:
        augustSet -= beatriceSet
    beatriceSet = set(input().split())
    if beatriceSet == {'HELP'}:
        break
    augustAnswer = set(input().split())

augustList = list(augustSet)
augustList.sort()
print(* augustList)
