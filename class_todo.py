class Dorm:
    def __init__(self,name):
        self.__name = name
        self.__building_list = []
        self.__resident_list = []

class Staff:
    def __init__(self,staff_id,name,building_resposibility,role_id):
        self.__staff_id = staff_id
        self.__name = name
        self.__building_reposibility = building_resposibility
        self.__role_id = role_id

    def login(self,email,password):
        pass
        
    def log_out(self):
        pass

class Operation_Staff(Staff):
    
    def view_booking_list(self):
        pass

    def confirm_booking_list(self):
        pass
    
    def make_report(self):
        pass

    def calculate_invoice(self,room_cost,electricity_cost,water_cost,parking_slot_cost,share_facility_cost,maintenance_cost,discount_cost):
        
        if discount_cost == 0:

            return room_cost + electricity_cost + water_cost + parking_slot_cost + share_facility_cost + maintenance_cost
        
        else:

            return (room_cost + electricity_cost + water_cost + parking_slot_cost + share_facility_cost + maintenance_cost) - discount_cost
        

    def create_invoice(self,invoice_type,room_cost,electricity_cost,water_cost,parking_slot_cost,share_facility_cost,maintenance_cost,discount_cost):
        
        self.__net_amount = 0
        
        self.__net_amount = self.calculate_invoice(room_cost,electricity_cost,water_cost,parking_slot_cost,share_facility_cost,maintenance_cost,discount_cost)
        
        self.__amount_before_discount = self.__net_amount + discount_cost

        return [invoice_type,room_cost,electricity_cost,water_cost,parking_slot_cost,share_facility_cost,maintenance_cost,discount_cost,self.__amount_before_discount,self.__net_amount]
        
class User:
    pass

class Resident(User):
    pass

class Invoice:
    pass

class Discount:
    pass

def main():
    print("Hello Nigga")

if __name__ == "__main__":
    main()
