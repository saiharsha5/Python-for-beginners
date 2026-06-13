score=list(map(int,input("Enter the scores: ").split()))
s=sorted(score, reverse=True)
print (f"Ranked: {s} | Top scorer: {s[0]}")
      