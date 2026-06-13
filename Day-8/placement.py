class Student:
    def __init__(self, student_id, student_name, attendance):
        self.student_id = student_id
        self.student_name = student_name
        self.attendance = attendance


class Assessment:
    def __init__(self, assessment_score):
        self.assessment_score = assessment_score


class PlacementManager:
    def __init__(self):
        self.students = []

    def add_student(self, student, assessment):
        self.students.append((student, assessment))

    def check_eligibility(self, student, assessment):
        if student.attendance >= 75 and assessment.assessment_score >= 60:
            return "ELIGIBLE"
        return "NOT ELIGIBLE"

    def generate_report(self):
        for student, assessment in self.students:
            status = self.check_eligibility(student, assessment)
            print("=" * 50)
            print("          PLACEMENT ELIGIBILITY REPORT")
            print("=" * 50)
            print(f"\nStudent ID       : {student.student_id}")
            print(f"Student Name     : {student.student_name}")
            print(f"\nAttendance       : {student.attendance}%")
            print(f"Assessment Score : {assessment.assessment_score}")
            print(f"Placement Status : {status}")
            print("=" * 50)
student = Student("S101", "ram", 85)
assessment = Assessment(78)
placement = PlacementManager()
placement.add_student(student, assessment)
placement.generate_report()