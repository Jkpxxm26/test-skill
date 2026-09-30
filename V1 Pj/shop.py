
class Defualt_machine:
    def __init__(self):  
        self.soft_drink = ["Cola", "Est", "Pepsi", "Fanta"]
        self.nomal_drink = ["Water", "Mineral", "Milk"]
        self.all_drink = self.soft_drink + self.nomal_drink
        self.food = ["ไข่เจียว", "ไข่ดาว", "ไข่ลวก"]
        self.all_menu = self.all_drink + self.food
        
        while True:
            self.item = input("สินค้าที่ต้องการซื้อ: ")
            try:
                # ถ้าป้อน "abc" บรรทัดนี้จะพังทันที แต่จะถูกดักจับโดยคำสั่งด้างล่าง ไม่โชว์ Error สีแดง
                self.amount = int(input("จำนวนสินค้า: ")) 
            except ValueError:
                print("กรุณากรอกจำนวนสินค้าเป็นตัวเลขเท่านั้น! Please try again!\n")
                continue

            if self.amount <= 0:
                print("จำนวนสินค้าต้องมากกว่า 0! Please try again!\n")
                continue
                
            if self.item not in self.all_drink + self.food:
                print("Sorry, My shop not have this.\n")
                continue
            else:
                print("บันทึกข้อมูลเรียบร้อย!")
                break
                  
    def cal_item (self):
        
        if self.item in self.soft_drink:
            price = 12
                        
        elif self.item in self.nomal_drink:
            price = 8
                        
        elif self.item in self.food:
            price = 5

        self.result = self.amount * price #----------------------(1)
        
        if self.item in self.all_drink:
            unit = "ขวด"
        else:
            unit = "จาน"
            
        text_box = f"ลูกค้าซื้อ {self.item} จำนวน {self.amount} {unit} ราคาที่ต้องจ่าย {self.result} บาท\n"
            
        with open("data_shop.txt", "a", encoding="utf-8") as Data:
            Data.write(text_box)
        
        return text_box
        
user = Defualt_machine()
print(user.cal_item())
        
        
    

