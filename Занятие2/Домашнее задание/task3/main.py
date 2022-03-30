A, B, C = int(input('Enter A: ')), int(input('Enter B: ')), int(input('Enter C: '))
if A < 45 and (B >= 45 and C >= 45):
    print(True)
elif B < 45 and (A >= 45 and C >= 45):
    print(True)
elif C < 45 and (A >= 45 and B >= 45):
    print(True)
else:
    print(False)
