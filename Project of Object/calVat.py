def Vat(numplate, excu_plate, result, hours, minute):
    total_hours = hours
    if 50 <= minute < 60:
        total_hours += 1    
            
    price_hours = 20 if total_hours >= 1 else 0

    if numplate == excu_plate:
        vat = 1.05
        bonus = 50
        result = round((result * (100 - bonus)) / 100, 2)
        result_price = round(result / vat, 2)
        result_vat = round(result - result_price, 2)
        result_time = total_hours * price_hours
        totalAll = (result_price + result_vat) + result_time
        return result_price, result_vat, result_time, totalAll

    elif numplate != excu_plate:
        vat = 1.07
        total_hours = hours
        if 50 <= minute < 60:
            total_hours += 1    
                        
        price_hours = 20 if total_hours >= 1 else 0
            
        result_price = round(result / vat, 2)  # ราคาอาหารก่อน VAT
        result_vat = round(result - result_price, 2) # ยอด VAT 7%
        result_time = total_hours * price_hours
        totalAll = (result_price + result_vat) + result_time
        return result_price, result_vat, result_time, result

# def Vat7(result, hours, minute):
#     vat = 1.07
#     total_hours = hours
#     if 50 <= minute < 60:
#         total_hours += 1    
                
#     price_hours = 20 if total_hours >= 1 else 0
    
#     result_price = round(result / vat, 2)  # ราคาอาหารก่อน VAT
#     result_vat = round(result - result_price, 2) # ยอด VAT 7%
#     result_time = total_hours * price_hours
#     result = result + result_time