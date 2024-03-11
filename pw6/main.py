from domains.school import School
import input
import output
import pickle
import zipfile  

def compress_data(data, filename):
    
    with zipfile.ZipFile(filename, 'w', zipfile.ZIP_DEFLATED) as zip_file:
        zip_file.writestr("data.pickle", pickle.dumps(data))

def decompress_and_load_data(filename):
    
    with zipfile.ZipFile(filename, 'r') as zip_file:
        data = pickle.loads(zip_file.read("data.pickle"))
    return data

def main():
    if os.path.isfile("students.dat"):
        print("Found existing data archive. Decompressing...")
        school_obj = decompress_and_load_data("students.dat")
    else:
        school_obj = school.School()
        input.input_students(school_obj)
        input.input_courses(school_obj)
        input.input_marks_for_course(school_obj)

    school_obj.sort_students_by_gpa()
    output.display_ui(school_obj)

    # Compress data before closing
    compress_data(school_obj, "students.dat")

if __name__ == "__main__":
    main()
