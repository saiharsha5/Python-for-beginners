score=list(map(int,input("Enter the score: ").split()))
avg=sum(score)/len(score)
print(f"Average nps score: {avg:.2f}")