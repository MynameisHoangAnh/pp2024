import curses

def display_ui(school):
    stdscr = curses.initscr()  # Initialize curses screen
    curses.noecho()
    curses.cbreak()

    while True:
        stdscr.clear()  # Clear the screen
        stdscr.addstr(0, 0, "School Management System")
        stdscr.addstr(2, 0, "1. List students")
        stdscr.addstr(3, 0, "2. List courses")
        stdscr.addstr(4, 0, "3. View student marks")
        stdscr.addstr(5, 0, "4. Exit")
        stdscr.refresh()

        choice = stdscr.getch()  # Get user input
        if choice == ord('1'):
            school.list_students()  # Implement UI for listing students
        elif choice == ord('2'):
            school.list_courses()  # Implement UI for listing courses
        elif choice == ord('3'):
            school.list_marks()
                # Implement UI for viewing student marks (see previous explanations)
        else:
            break  # Exit the loop

    curses.endwin()  # Restore terminal settings   
