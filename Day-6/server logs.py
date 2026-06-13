log=list(map(int, input("Enter the logs: ").split()))
print(f"Last 5 logs: {log[-5:]}| critical error found: {True if 500 in log[-5:] else False}")