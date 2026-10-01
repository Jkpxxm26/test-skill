import time

class Defualt_Rt:
    def __init__(self):
        self.num_plate = input("เลขทะเบียนรถ: ")
        self.excu_plate = "sss-111"
        self.menu = ["สปาเก็ตตี้", "ข้าวผัดมันเนื้อ", "เนื้อริบอาย"]
        self.A_drink = ["Red wine", "Champagne", "Wine"]
        self.soft_drink = ["Cola", "Est", "Fanta"]
        self.nm_drink = ["Water", "Mineral"]
        self.all_drink = self.A_drink + self.soft_drink + self.nm_drink
        self.all_menu = self.menu + self.all_drink

    def cal_menu(self, hours, minute):
#------- รับข้อมูล อาหาร / จำนวน
        while True:
            self.user_input = input("อาหารที่ต้องการสั่ง: ").strip().title()
            
            if self.user_input not in self.all_menu:
                print("Sorry, My rest not have this.")
                time.sleep(1)
                print("Please choose again!\n")
                continue
            try:
                self.amount = int(input("จำนวนที่ต้องการสั่ง: "))
            except ValueError:
                print("ใส่ตัวเลขเท่านั้น! Please try again!\n")
                continue
            
            if self.amount <= 0:
                print("ขั้นต่ำ 1 ชิ้น! Please choose again!\n")
                continue
            else:
                break

#-------คำนวณราคาอาหารแยกตามประเภท
        if self.user_input in self.menu:
            if self.user_input == "เนื้อริบอาย":
                price = 120
            else:
                price = 50

        elif self.user_input in self.A_drink:
            if self.user_input == "Champagne":
                price = 250
            else:
                price = 200

        elif self.user_input in self.soft_drink:
            price = 20

        elif self.user_input in self.nm_drink:
            if self.user_input == "Mineral":
                price = 20
            else:
                price = 10
        else:
            price = 0

#-------ราคาจอดรถรายชั่วโมง
        total_hours = hours
        if minute > 0:
            total_hours += 1
            
        price_hours = 20 if total_hours >= 1 else 0

#-------คำนวณราคาอาหาร + ราคาจอดรถ
        self.result_price = (self.amount * price)
        self.result_time = (total_hours * price_hours)
        self.result = self.result_price + self.result_time

#-------ส่วนลด      
        bonus_text = ""
        if self.num_plate == self.excu_plate:
            bonus = 50
            self.result = self.result * (100 - bonus) // 100
            bonus_text = "ยินดีด้วย คุณได้ส่วนลด 50%!"

        text = "จาน" if self.user_input in self.menu else "ขวด"

        if minute == 0:
            text_box = f"คุณได้สั่ง {self.user_input} จำนวน {self.amount} {text} จอดรถ {hours} ชั่วโมง"
        else:
            text_box = f"คุณได้สั่ง {self.user_input} จำนวน {self.amount} {text} จอดรถ {hours} ชั่วโมง {minute} นาที"

        print("\n" + text_box)
        if self.num_plate == self.excu_plate:
            print(bonus_text)
        time.sleep(0.5)

        print(f"|ราคารวมสุทธิ {self.result} บาท|\n")
        time.sleep(1)

#-------ระบบจ่ายเงิน (Cash / Card)
        print("ต้องการจ่ายเงินรูปแบบไหน")
        self.Cash_card = input("Cash / Card? : ").strip().capitalize()
        
#-------(Card)
        if self.Cash_card == "Card":
            while True:
                try:
                    self.user_cart = int(input("ใส่เลขบัตรเครดิต: "))
                    self.user_insert_money = int(input("ใส่จำนวนเงิน: "))            
                except ValueError:
                    print("ใส่แต่ตัวเลขเท่านั้น!\n")
                    continue

                if self.user_insert_money < self.result:
                    print("ยอดเงินไม่เพียงพอในบัตร!\n")
                    time.sleep(1)
                    yes_no = input("ต้องการเปลี่ยนบัตรเพื่อทำรายการต่อไหม? (Yes/No): ").strip().capitalize()
                    if yes_no == "Yes":
                        continue
                    else:
                        return "|ยกเลิกรายการสั่งซื้อ|"
                else:
                    break    
                
            new_result = self.user_insert_money - self.result
            time.sleep(1)
            print("|ระบบกำลังประมวลผลบัตรเครดิต...|")
            time.sleep(1.5)
            return f"|ชำระสำเร็จ กำลังทอนเงิน {new_result} บาท|"
            
#-------(Cash)
        elif self.Cash_card == "Cash":
            self.cash_user = 0
            while True:
                try:
                    self.pay_cash = int(input("หยอดเงิน/ใส่เงินสด: "))
                except ValueError:
                    print("กรุณาใส่เป็นตัวเลขเงินเท่านั้น!")
                    continue
                    
                self.cash_user = self.cash_user + self.pay_cash

                if self.cash_user < self.result:
                    print(f"ยังขาดเงินอีก {self.result - self.cash_user} บาท")
                    continue
                else:
                    break

            new_result = self.cash_user - self.result
            time.sleep(1)
            print("\n|ทำรายการชำระเงินสดสำเร็จ ขอบคุณครับ/ค่ะ|")
            return f"|รับเงินมา {self.cash_user} บาท | เงินทอนของคุณคือ {new_result} บาท|"

user1 = Defualt_Rt()
print(user1.cal_menu(2, 15))

class rest_systhem(Defualt_Rt):
    def __init__(self):
        super().__init__()
        self.owner = "Prem"
