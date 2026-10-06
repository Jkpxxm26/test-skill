# แผนอัพเดตระบบในอนาคต 
# (1) เพิ่มข้อมูลData ที่ลูกค้าสั่งเข้าไฟล์ txt เขียนได้ อ่านได้ --- เสร็จ
# (2) ระบบนาที --- เสร็จ
# (3) ระบบถ้าจ่ายเงินจำนวนเงินน้อยกว่าราคาอาหารรวม ให้สามารถจ่ายเงินเพิ่มได้ จนกว่าจะครบ --- เสร็จ
# (4) ระบบ Vat 7% --- เสร็จ
# (5) จัดโค๊ดให้เรียบร้อย / อันไหนเปลี่ยนเป็น Modulได้ เปลี่ยน
# (6) คำนวณรายได้ยอดขาย จากประวัติการสั่ง

import time
from pathlib import Path

class Defualt_Rt:
    def __init__(self):
        self.num_plate = input("[เลขทะเบียนรถ]: ")
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
            self.user_input = input("[อาหารที่ต้องการสั่ง]: ").strip().capitalize()
            
            if self.user_input not in self.all_menu:
                print("Sorry, My rest not have this.")
                time.sleep(1)
                print("Please choose again!\n")
                continue
            try:
                self.amount = int(input("[จำนวนที่ต้องการสั่ง]: "))
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

#-------คำนวณราคาอาหาร + ราคาจอดรถ  
        import calVat   
        total_food_price = self.amount * price
        calVat.Vat(self.num_plate, self.excu_plate, total_food_price, hours, minute) #---> เรียกใช้ฟังก์ชั่นในโมดูล


#------- สร้างตัวแปรมารับค่า 4 ตัวที่รีเทิร์นออกมาจากโมดูล
        res_price, res_vat, res_time, total_all = calVat.Vat(self.num_plate, self.excu_plate, total_food_price, hours, minute)


#-------ส่วนลด (excu_plate)   
        import calVat
        bonus_text = ""
        calVat.Vat(self.num_plate, self.excu_plate, total_food_price, hours, minute)
        bonus_text = "ยินดีด้วย คุณได้ส่วนลด 50%!"

        text = "จาน" if self.user_input in self.menu else "ขวด"

        if minute == 0:
            text_box = f"คุณได้สั่ง {self.user_input} จำนวน {self.amount} {text} จอดรถ {hours} ชั่วโมง"

        else:
            text_box = f"คุณได้สั่ง {self.user_input} จำนวน {self.amount} ราคา {total_all} บาท {text} จอดรถ {hours} ชั่วโมง {minute} นาที"

        print("\n" + text_box)
        if self.num_plate == self.excu_plate:
            print(bonus_text)
        time.sleep(0.5)

        print(f"|ราคาอาหารก่อนรวมVat: {res_price} / Vat: {res_vat}บาท|\n")
        time.sleep(1)
        print(f"|ราคารวมสุทธิ {total_all} บาท|\n")
        time.sleep(1)

#-------ระบบจ่ายเงิน (Cash / Card)
        text_end = ""

        while True:
            print("ต้องการจ่ายเงินรูปแบบไหน")
            self.Cash_card = input("Cash / Card? : ").strip().capitalize()
            
    #-------(Card)
            if self.Cash_card == "Card":
                while True:
                    self.user_cart = input("ใส่เลขบัตรเครดิต: ")
                    try:
                        self.user_insert_money = float(input("ใส่จำนวนเงิน: "))            
                    except ValueError:
                        print("ใส่แต่ตัวเลขเท่านั้น!\n")
                        continue

                    if self.user_insert_money < total_all:
                        print("ยอดเงินไม่เพียงพอในบัตร!\n")
                        time.sleep(1)
                        yes_no = input("ต้องการเปลี่ยนบัตรเพื่อทำรายการต่อไหม? (Yes/No): ").strip().capitalize()
                        if yes_no == "Yes":
                            continue
                        else:
                            text_end =  "|ยกเลิกรายการสั่งซื้อ|"
                            break
                    else:
                        break    

                time.sleep(1)
                print("|ระบบกำลังประมวลผลบัตรเครดิต...|")
                time.sleep(1.5)
                text_end =  f"|ชำระสำเร็จ!|"
                break
                
    #-------(Cash)
            elif self.Cash_card == "Cash":
                self.cash_user = 0
                while True:
                    try:
                        self.pay_cash = float(input("หยอดเงิน/ใส่เงินสด: "))
                    except ValueError:
                        print("กรุณาใส่เป็นตัวเลขเงินเท่านั้น!")
                        continue
                        
                    self.cash_user = round(self.cash_user + self.pay_cash, 2)

                    if self.cash_user < total_all:
                        remaining = round(total_all - self.cash_user, 2)
                        print(f"ยังขาดเงินอีก {remaining} บาท")
                        continue
                    else:
                        break

                new_result = round(self.cash_user - total_all, 2)
                time.sleep(1)
                print("\n|ทำรายการชำระสำเร็จ ขอบคุณครับ/ค่ะ|")
                text_end = f"|รับเงินมา {self.cash_user:.2f} บาท | เงินทอนของคุณคือ {new_result:.2f} บาท|"
                break
            
            else:
                print("วิธีการชำระเงินไม่ถูกต้อง")
                time.sleep(1)
                print("โปรดเลือกใหม่!\n")
                continue

#------- เก็บข้อมูลการสั่งซื้อลูกค้า
        file_path = Path(__file__).parent / "Order.txt"
        Order_text = ""
        Order_text = f"{self.num_plate} สั่ง {self.user_input} จำนวน {self.amount}{text} | {total_all}บาท ชำระเงินแบบ {self.Cash_card} | \n"

        with file_path.open("a", encoding="utf-8") as Order_data:
            Order_data.write(Order_text)

        return text_end

#--- ยังไม่เสร็จ
    @staticmethod
    def Read_data():
        file_path = Path(__file__).parent / "Order.txt"

        with file_path.open("r", encoding="utf-8") as order_data:
            result = order_data.readlines()

        return len(result)


# user1 = Defualt_Rt()
# print(user1.cal_menu(2, 15))

class Rest_systhem(Defualt_Rt):
    def __init__(self):
        super().__init__()
        self.owner = "Prem"

    @staticmethod
    def check_order():
        total_order = Defualt_Rt.Read_data()
        print(f"มียอด Order ทั้งหมด: {total_order}")

user2 = Rest_systhem()
print(user2.cal_menu(3, 43))
# Rest_systhem.check_order()
