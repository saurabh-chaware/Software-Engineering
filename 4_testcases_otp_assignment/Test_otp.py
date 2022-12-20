import unittest
import smtplib
import otp_version1 as O1

class BetweenAssertMixin(object):
    def assertBetween(self, x, low, hi):
        if not (low <= x <= hi):
            raise AssertionError('Length of OTP is %r should be in between %r and %r' % (x, low, hi))
        
class Test_otp(unittest.TestCase,BetweenAssertMixin):
    def testcase1(self):
        print("---------TestCase_No.1---------")
        #Checking Email
        Name="Saurabh"
        Email="saurabhchaware358 @gmail.com"
        self.assertIn("@",Email)
        self.assertIn(".",Email)
        self.assertIn("com",Email)

        True_Str1 = "gmail" in Email        
        if True_Str1 :
            print("No Error Found in Email!")
        else:
            self.assertTrue(True_Str1)

        #Checking OTP here
        otp = O1.generate_otp(4)
        self.assertBetween(len(otp),4,8)

        #Calling Sendmail Function here
        O1.send_email(Name,Email)
        print()

    def testcase2(self):
        #Checking Email with wrong email id
        print("<<--------TestCase_No.2------->>")
        Name="Saurabh"
        Email="saurabhchaware358.com"

        self.assertIn("@",Email)
        self.assertIn(".",Email)
        self.assertIn("com",Email)

        True_Str1 = "@" and "." and "com" and "gmail" in Email        
        if True_Str1 :
            print("No Error Found in Email!")
        else:
            self.assertTrue(True_Str1)

        #Checking OTP here
        otp = O1.generate_otp(5)
        self.assertBetween(len(otp),4,8)

        #Calling Sendmail Function here
        O1.send_email(Name,Email)
        print()

    def testcase3(self):
        #Checking Email here
        print("<<-------TestCase_No.3------>>")
        Name="Saurb"
        Email="saurabhchaware358@gmail.com"
        self.assertIn("@",Email)
        self.assertIn(".",Email)
        self.assertIn("com",Email)

        True_Str1 = "gmail" in Email        
        if True_Str1 :
            print("No Error Found in Email!")
        else:
            self.assertTrue(True_Str1)

        #Checking OTP
        # Here we r going to enter invalid otp 
        otp = O1.generate_otp(9)
        self.assertBetween(len(otp),4,8)

        #Calling Sendmail Function here
        O1.send_email(Name,Email)
        
unittest.main()


 
