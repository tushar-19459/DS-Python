class Event:
    def __init__(self,n):
        self.n = n
        self.collage_data = {}
        self.event_seats  ={}

    class Student:
        def __init__(self,name,usn):
            self.name = name
            self.usn = usn

    def institution_register(self,collage_name,no_std_planed):
        self.collage_data[collage_name]=no_std_planed
        self.event_seats[collage_name]={
            'day1':[],
            'day2':[],
            'day3':[],
        }

    def student_register(self,name,usn,day):
        self.event_seats
    
    def get_count(self):
        print(self.event_seats)