def new_password(oldpassword,newpassword):
    if oldpassword != newpassword and len(newpassword) > 6:
        print(True)
    else:
        print(False)

new_password("tychovdw","tychovanderwerff")