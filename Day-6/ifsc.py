'''ifsc=(str,input().lower().split())
if len(ifsc)==11:
    if ifsc[:4].isalpha():
        if ifsc[4]==0:
            print("valid ifsc code")
        else:
            print("Invalid — 5th character must be '0'")
    else:
        print("Invalid — First 4 characters must be alphabets (length check fails)")
else:
    print("invalid ifsc")
'''
ifsc=(str,input().lower().split())
if len(ifsc)==11 and ifsc[:4].isalpha() and ifsc==4:
    print("Valid ifsc code")
else:
    print("invalid")
