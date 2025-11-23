class EventSlotBookingSystem:
    def __init__(self, slots_per_day):
        self.slots_per_day = slots_per_day
        self.total_slots = slots_per_day * 3
        self.institutions = {}  # {institution_name: {"total": x, "students": []}}
        self.allocations = {"Da y1": [], "Day2": [], "Day3": []}
    def register_institution(self, name, expected_count):
        self.institutions[name] = {"total": expected_count, "students": []}
    def register_student(self, institution, name, reg_no, preferred_day):
        if institution not in self.institutions:
            print(f"Institution '{institution}' not registered.")
            return
        max_per_day = self.institutions[institution]["total"] * 0.5
        day_count = sum(1 for s in self.allocations[preferred_day] if s['institution'] == institution)
        if day_count < max_per_day and len(self.allocations[preferred_day]) < self.slots_per_day:
            student = {
                "name": name,
                "reg_no": reg_no,
                "institution": institution,
                "day": preferred_day
            }
            self.institutions[institution]["students"].append(student)
            self.allocations[preferred_day].append(student)
        else:
            print(f"Slot not available on {preferred_day} for {institution}.")
    def show_institution_counts(self):
        print("\nInstitution-wise Count per Day:")
        for inst in self.institutions:
            counts = {
                day: sum(1 for s in self.allocations[day] if s['institution'] == inst)
                for day in self.allocations
            }
            print(f"{inst}: {counts}")
    def get_students_by_day(self, institution, day):
        students = [
            s for s in self.allocations[day]
            if s['institution'] == institution
        ]
        print(f"\nStudents from {institution} on {day}:")
        for s in students:
            print(f"{s['name']} ({s['reg_no']})")

if __name__ == "__main__":
    system = EventSlotBookingSystem(slots_per_day=5)
 
    # Register institutions
    system.register_institution("ABC College", 8)
    system.register_institution("XYZ Institute", 6)
    
    # Student registrations
    system.register_student("ABC College", "Ravi", "1001", "Day1")
    system.register_student("ABC College", "Kiran", "1002", "Day1")
    system.register_student("XYZ Institute", "Meena", "2001", "Day2")
    
    # Show institution-wise counts
    system.show_institution_counts()
    
    # Get list for a given day and institution
    system.get_students_by_day("ABC College", "Day1")
    system.get_students_by_day("XYZ Institute", "Day2")
