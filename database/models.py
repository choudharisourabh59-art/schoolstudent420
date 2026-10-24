ROLES={"admin","teacher","student","parent"}
ATTENDANCE_STATES={"Present","Absent","Late"}
def validate_marks(marks,maximum):
    marks=float(marks); maximum=float(maximum)
    if maximum<=0 or marks<0 or marks>maximum:
        raise ValueError("Marks must be between zero and maximum marks.")
    return marks
