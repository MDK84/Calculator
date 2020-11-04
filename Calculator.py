from hashlib import sha256
from time import sleep

print(" ***   Welcome    *** ")
print("   ***************   ")
print(" ***  Calculator  *** ")
print("   ***************   ")

class Calculator:

    def user_name(self):
        a = "c449ca1b7e7a0741722932d0a7ef67a2768e4c2efdb1748fe6992dc7546f8536"
        b = "084648f05e64f3acf37fdfed2d7cfae7f3d04718f70bb1d814a8ac01f8016618"
        c = '8fa7d0e5166874fe1af6048e625b89c18b09b800da10d31485cdb686b845179a'
        
        self.UserName = str(input("Enter your name please = "))
        while self.UserName == '':
            print("Answer Error")
            print("Enter a name please")
            self.UserName = str(input("Enter your name please = "))
            if self.UserName != "":
                break

        hash = sha256()
        hash.update(self.UserName.encode("utf-8"))
        hash_dejban = hash.hexdigest()
        
        #admins
        if hash_dejban == a or hash_dejban == b or hash_dejban == c:
            print("Hello Admin!")
            self.UserName = "Admin"
        else:
            print("Hello", self.UserName, "!")

    def NumCalculator(self):
        self.user_name()
        #Enter Number and Fix error!
        try:
            self.Answer1 = int(input("Enter first number please = "))
            self.Answer2 = int(input("Enter second number please = "))
        except:
            print("Answer Error")
            print("Your answer is not found in program")
            print("Enter correct answer please")
            time.sleep(0.5)
            self.Answer1 = int(input("Enter first number please = "))
            self.Answer2 = int(input("Enter second number please = "))

        self.operator = str(input("Which is your request? \n1.\t+  \n2. \t -   \n3. \t x   \n4. \t/ = "))

        while self.operator != "1" and self.operator != "2" and self.operator != "3" and self.operator != "4":
            print("Your answer not found in program")
            print("Enter correct answer please")
            sleep(0.5)
            self.operator = str(input("Which is your request? \n1.\t+  \n2. \t-   \n3. \tx   \n4. \t/ = "))
            if self.operator == '1' or self.operator == '2' or self.operator == '3' or self.operator == '4':
                break

        if self.operator == "1":
            print(self.Answer1 , "+" , self.Answer2 , "=" , self.Answer1 + self.Answer2)
            sleep(0.5)

        if self.operator == "2":
            print(self.Answer1 , "-" , self.Answer2 , "=" , self.Answer1 - self.Answer2)
            sleep(0.2)

        if self.operator == "3":
            print(self.Answer1 , "x" , self.Answer2 , "=" , self.Answer1 * self.Answer2)
            sleep(0.5)

        if self.operator == "4":
                while self.Answer2 == 0 :
                    print("Zero Error")
                    print("No number can be divided by zero")
                    print("Enter correct answer please")
                    sleep(0.5)
                    self.Answer2 = int(input("Enter second number please = "))
                    if self.Answer2 != 0:
                            break
                print(self.Answer1 , "/" , self.Answer2 , "=" , self.Answer1 / self.Answer2 )
                sleep(0.5)

        self.operator = str(input("If you want to continue?  1.Yes    2.No = "))
        while self.operator != "1" and self.operator != "2":
            print("Your answer not found in program")
            print("Enter correct answer please")
            sleep(0.5)
            self.operator = str(input("If you want to continue?  1.Yes    2.No = "))
            if self.operator == "1" or self.operator == "2":
                break
        #پاسخ بله
        while self.operator == "1":
            try:
                self.Answer1 = int(input("Enter first number please = "))
                self.Answer2 = int(input("Enter second number please = "))
            except:
                print("Answer Error")
                print("Your answer is not found in program")
                print("Enter correct answer please")
                sleep(0.5)
                self.Answer1 = int(input("Enter first number please = "))
                self.Answer2 = int(input("Enter second number please = "))

            self.operator = str(input("Which is your request? \n1.\t+  \n2. \t-   \n3. \tx   \n4. \t/ = "))

            while self.operator != "1" and self.operator != "2" and self.operator != "3" and self.operator != "4":
                print("Your answer not found in program")
                print("Enter correct answer please")
                time.sleep(2)
                self.operator = str(input("Which is your request? \n1.\t+  \n2. \t-   \n3. \tx   \n4. \t/ = "))
                if self.operator == '1' or self.operator == '2' or self.operator == '3' or self.operator == '4':
                    break

            if self.operator == "1":
                print(self.Answer1 , "+" , self.Answer2 , "=" , self.Answer1 + self.Answer2)
                sleep(0.5)

            if self.operator == "2":
                print(self.Answer1 , "-" , self.Answer2 , "=" , self.Answer1 - self.Answer2)
                sleep(0.5)

            if self.operator == "3":
                print(self.Answer1 , "x" , self.Answer2 , "=" , self.Answer1 * self.Answer2)
                sleep(0.5)

            if self.operator == "4":
                while self.Answer2 == 0 :
                    print("Zero Error")
                    print("No number can be divided by zero")
                    print("Enter correct answer please")
                    sleep(0.5)
                    self.Answer2 = int(input("Enter second number please = "))
                    if self.Answer2 != 0:
                            break
                print(self.Answer1 , "/" , self.Answer2 , "=" , self.Answer1 / self.Answer2 )
                sleep(0.5)

            self.operator = str(input("If you want to continue?  1.Yes    2.No = "))
            while self.operator != "1" and self.operator != "2":
                print("Your answer not found in program")
                print("Enter correct answer please")
                sleep(0.5)
                self.operator = str(input("If you want to continue?  1.Yes    2.No = "))
                if self.operator == "1" or self.operator == "2":
                    break
            if self.operator == "2":
                break
        #پاسخ خیر
        if self.operator == "2":
            print("")
            print("***  Thanks for using this program  ***")
            print("***             Goodbye             ***")
            print("*** ", self.UserName, " ***")
            sleep(5)

if __name__ == "__main__":
        start = Calculator()
        start.NumCalculator()
