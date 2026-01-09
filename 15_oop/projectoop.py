class Room:
    def __init__(self,room_number,room_type,price_per_day,is_available):
        self.room_number = room_number
        self.room_type = room_type
        self.price_per_day=price_per_day
        self.is_available=is_available

    def display_room(self):
         if (self.is_available == True):
          return f'''Room number{self.room_number}   '''
         pass
         
    def book_room(self):
        pass
 
    def cheackout_room(self):
        pass



class Customer:
    def __init__(self,customer_id,name,phone):
        self.customer_id=customer_id
        self.name=name
        self.phone=phone

    def __repr__(self):
        return f"Customer id: {self.customer_id} name:{self.name} phone: {self.phone}"
    

class Booking:
    def __init__(self,booking_id,customer,room,days,total_amount):
        self.booking_id = booking_id
        self.room = room          # HAS-A relationship
        self.customer = customer  # HAS-A relationship
        self.days=days
        self.total_amount=total_amount


    def calculate_bill():
        pass

    def show_booking():
        pass 

class  Hotel:
    def __init__(self,list_of_rooms,list_of_bookings):
        self.list_of_rooms = list_of_rooms
        self.list_of_bookings = list_of_bookings

    def add_room():
     pass
    def show_available_rooms():
     pass
    def book_room():
     pass
    def checkout():
     pass
    def show_all_bookings():
     pass

