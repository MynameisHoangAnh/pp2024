from domains.school import School
import input
import output

def main():
    school_obj = school.School()
    input.input_students(school_obj)
    input.input_courses(school_obj)
    input.input_marks_for_course(school_obj)
    school_obj.sort_students_by_gpa()
    output.display_ui(school_obj)

if __name__ == "__main__":
    main()
