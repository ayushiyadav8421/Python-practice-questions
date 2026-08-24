otps= ["5632","1111","235621"]
for otp in otps:
    if len(otp)==6 and otp.isdigit():
        for item in otp:
            if item[0]==item[1]==item[2]==item[3]==item[4]==item[5]:
                print("Invaild OTP")
            else:
                print("Invaild OTP")
    else:
        print("Invaild OTP")