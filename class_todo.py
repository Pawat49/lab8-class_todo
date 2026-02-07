# Importing the FastApi class
from fastapi import FastAPI
import uvicorn

# Creating an app object
app = FastAPI()

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

        return self.__net_amount
        

class Invoice:
    pass

        


@app.get("/")
async def root():
    return {"message":"hello tonson"}

if __name__ == "__main__":
    uvicorn.run("class_todo:app", host="127.0.0.1", port=8000, log_level="info")
