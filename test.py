import time

class Defualt_Rt:
    def __init__(self, time):
        self.num_plate = input("เลขทะเบียนรถ: ")
        self.excu_plate = "sss-111" #------------(1)
        self.time = time #------(จำนวนชม.จอดรถ)
        self.menu = ["สปาเก็ตตี้", "ข้าวผัดมันเนื้อ", "เนื้อริบอาย"]
        self.A_drink = ["Red vine", "Champagne", "Vine"]
        self.soft_drink = ["Cola", "Est", "Fanta"]
        self.nm_drink = ["Water", "Mineral"]
        self.all_drink = self.A_drink + self.soft_drink + self.nm_drink
        self.all_menu = self.menu + self.A_drink + self.all_drink
        
        while True:
            self.user_input = input("อาหารที่ต้องการสั่ง: ")
            if self.user_input not in self.all_menu:
                print("Sorry, My rest not have this.")
                time.sleep(1)
                print("Please choise again!")
                time.sleep(1)
                continue
            try:
                self.amount = int(input("จำนวนที่ต้องการสั่ง: "))
            except ValueError:
                print("ใส่ตัวเลขเท่านั้น")
                print("Please try again!")
                continue
            
            if self.amount <= 0:
                print("ขั้นต่ำ 1ชิ้น")
                time.sleep(1)
                print("Please choise again!")
                time.sleep(1)
                continue
            else:
                break
    
    def cal_menu(self):
        if self.user_input in self.menu:
            price = 50
            if self.menu == "เนื้อริบอาย":
                price = 150
                
        elif self.user_input in self.A_drink:
            price = 120
            if self.A_drink == "Champagne":
                price = 250
                
        elif self.user_input in self.soft_drink:
            price = 12
        
        elif self.user_input in self.nm_drink:
            price = 10
            if self.nm_drink == "Mineral":
                price = 20
        
        elif self.time >= 1:
            price_hours = 20
        
        self.result = self.amount * price
        self.result_all = self.result + (self.time * price_hours)
        
        if self.num_plate == self.excu_plate:
            bonus = 50
            self.result = (self.amount * price) * (100 - bonus) / 100
            print("คุณได้ส่วนลด 50%")
            
        if self.user_input in self.menu:
            text = "จาน"
        else:
            text = "ขวด"
        
        print(f"คุณได้สั่ง {self.user_input} จำนวน {self.amount}{text} จอดรถ {self.time} นาที") #------(ปรับแก้ยังไม่เสร็จ)
        return f"ราคารวม {self.result}บาท"

        while True:
            try:
                user_cart = int(input("ใส่เลขบัตร: "))
                user_insert_money = int(input("ใส่จำนวนเงิน: "))            
            except ValueError:
                print("ใส่แต่ตัวเลขเท่านั้น!")
                continue
            if user_insert_money <= 0:
                print("Try again!")
                continue 
            else:
                break
            
        new_result = user_insert_money - self.result
        time.sleep(0.5)
        
        return f"ถอน {new_result}"
        
        
            
            
            
        