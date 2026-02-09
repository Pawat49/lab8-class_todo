from abc import ABC, abstractmethod
import datetime

class Dorm:

    def __init__(self,name):
        self.__name = name
        self.__building_list = []
        self.__applicant_list = []
        self.__resident_list = []
        self.__os_staff_list = []
        self.__maintenace_technician_list = []
        self.__system_admin_list = []

    def verify_identity(self,email,password):
        ...

    def add_resident(self,resident):
        self.__resident_list.append(resident)
        
    def add_operation_staff(self,operation_staff):
        self.__os_staff_list.append(operation_staff)

class Profile(ABC):
    
    def __init__(self,profile_id,name,email,phone_number):
        self.__profile_id = profile_id
        self.__name = name
        self.__profile_image = None
        self.__email = email
        self.__phone_number = phone_number
        self.__date_create = datetime.datetime.now()
        self.__last_login = datetime.datetime.now()
        self.__general_data = ""
        self.__password = ""

    def image_setting(self,profile_image):
        self.__profile_image = profile_image

    @property
    def id(self):
        return self.__profile_id
    
    @property
    def name(self):
        return self.__name
    
    @property
    def password(self):
        return self.__password
    
    @property
    def data(self):
        return self.__general_data
    
    @name.setter
    def name_setting(self,name):
        self.__name = name

    @password.setter
    def password_setting(self,password):
        self.__password = password

    @data.setter
    def data_setting(self,data):
        self.__general_data = data

    def deactivate_account(self):
        pass

    def audit_log(self):
        pass
        

class Staff(Profile):
    def __init__(self,staff_id,name,email,phone_number,building_resposibility,role_id):
        super().__init__(staff_id,name,email,phone_number,building_resposibility,role_id)
        self.__staff_id = staff_id
        self.__name = name
        self.__email = email
        self.__phone_number = phone_number
        self.__building_reposibility = building_resposibility
        self.__role_id = role_id
        
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
        
class User(Profile):

    def __init__(self,profile_id,name,email,phone_number):
        super().__init__(profile_id,name,email,phone_number)
        self.__record_list = []
        self.__invoice_list = []

    def sign_in(self,email):
        pass

    def login(self):
        pass

    def view_room_list(self):
        pass

    def view_detail(self):
        pass

    def serch_room(self):
        pass

    def serch_room_filter(self):
        pass

class Resident(User):
    
    def __init__(self, name, email, phone_number):
        super().__init__(name, email, phone_number)
        self.__address = None
        self.__room_id = None
        self.__moving_indate = None
        self.__contract = None
        self.__insurance_cost = None
        self.__speacial_condition = None
        self.__invoice_record = None
        self.__outstanding_balance = None
        self.__maintenance_status = None
        self.__account_balance = None
        self.__status = None
        self.__status_log = []

    def view_invoice(self):
        print(self.__invoice_record)

    def download_invoice(self):
        pass

    def pay_invoice(self):
        pass

    def maintenance_request(self):
        pass

    def change_contract(self):
        pass

    def refund(self):
        pass

    def validate_account_status(self):
        pass

    def change_status(self):
        pass

class Invoice:
    
    def __init__(self,invoice_type,room_cost,electricity_cost,water_cost,parking_slot_cost,share_facility_cost,maintenance_cost,discount_cost):
        pass

class Discount:
    
    def __init__(self,type):
        self.__type = type

    def create_discount_type(self,type):
        if type == "STUDENT" or type == "CORPORATE":
            return Student_Discount(type)
        elif type == "EARLY":
            return Early_Discount(type)
        elif type == "LONGTERM":
            return Long_Term_Discount(type)


class Student_Discount(Discount):
    # นักศึกษา: ลดค่าเช่า 3% (ต้องยืนยันสถานะทุกเทอม)
    # องค์กร: ลดค่าเช่า 8% แต่ขั้นต่ำ 5 ห้อง และสัญญารายปี
    discount = 0.03

class Early_Discount(Discount):
    # ชำระบิลก่อนวันที่ 5 ของเดือน ลดค่าบริการส่วนกลาง 100 บาท
    discount = 100

class Long_Term_Discount(Discount):
    # ทำสัญญา 12 เดือน ลดค่าเช่า 5% ตลอดสัญญา
    discount = 0.05

def test():
    print("Hello World")
    dorm = Dorm("Ducky")
    kenny = Resident("kenny", "ken@gmail.com", "ken", "1234567890")
    # (staff_id,name,email,phone_number,building_resposibility,role_id)
    gong = Operation_Staff("6767676767","gong_inwzaa","gonginwzaa007@gmail.com","67686970","A01","1234567890")
    gong.password_setting("67766776")
    dorm.add_resident(kenny)
    dorm.add_operation_staff(gong)
    gong.create_invoice()
    
    

if __name__ == "__main__":
    test()
