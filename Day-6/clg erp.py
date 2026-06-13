attendance=list(map(str,input("Enter the attendance: ").lower().split()))
print(f"Number of absents are {attendance.count('absent')}")