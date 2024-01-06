def student_num():
	return int(input("Enter student number: "))

def student_info(std,course,num):
	for j in range(num):
		print("---")
		s_id = input("Enter student id: ")
		s_name = input("Enter student name: ")
		s_DoB = input("Enter student DoB: ")
		std[s_id] = {"SName": s_name, "SDoB": s_DoB}
		for i in course:
			std[s_id].update({course[i]["CName"]:""})

def course_num():
	return int(input("Enter course number: "))

def course_info(course,num):
	for i in range(num):
		c_id = input("Enter course id: ")
		c_name = input("Enter course name: ")
		course[c_id] = {"CName": c_name}
		print("---")


def select_course_n_input_marks(student, course):
	print("---")
	c_id = input("Enter course id: ")
	again = True
	while again == True:
		if c_id in course:
			again = False
			for i in student:
				print("---")
				print("Enter", student[i]["SName"], "mark: ")
				s_mark = input()
				# course[c_id]["Student"][i].update({"Mark": s_mark})
				student[i].update({course[c_id]["CName"]:s_mark})
		else:
			c_id = input("Enter valid course id: ")

def show_mark_from_chosen_course(student, course):
	print("---")
	user = input("Enter a course id to see student's marks: ")

	while True:
		if user in course:
			print("DISPLAYING STUDENT MARKS IN COURSE:", course[user]["CName"])
			for i in student:
				print(student[i]["SName"], student[i][course[user]["CName"]])
			return False
		else:
			user = input("Enter a valid course id to see student's marks: ")

def list_course(course):
	print("---")
	print("AVAILABLE COURSE(S):" )
	for i in course:
		print( course[i]["CName"])

def list_student(student, course):
	print("---")
	print("STUDENT INFO:")
	for i in student:
		print("---")
		print(student[i]["SName"],student[i]["SDoB"])
		for j in course:
			print(course[j]["CName"],student[i][course[j]["CName"]])


def main():

	student = {}
	course = {}
	choose = ("""0. Exit
	1. Input number of course
	2. Input course information (ID, Name)
	3. Input number of student
	4. Input student information (ID, Name, DoB)
	5. Select a course ID and input student marks
	6. Display course list
	7. Display student list
	8. show mark from a course""")

	print("---")
	print("What do you want to do?")
	print("---")
	print(choose)
	print("---")

	done = []

	again = True
	while again == True:
		user = input("CHOOSE AN OPTION: ")
		print("---")
		if user == "0":
			again = False

		elif user == "1":
			if "1" in done:
				print("You already did this")
			else:
				course_number = course_num()
				print("---")
				done.append("1")

		elif user == "2":
			if "2" in done:
				print("You already did this")
			elif "1" in done:
				course_info(course,course_number)
				print("---")
				done.append("2")
			else:
				print("Must input number of course first")
				print("---")

		elif user == "3":
			if "3" in done:
				print("You already did this")
			elif "2" in done:
				student_number = student_num()
				print("---")
				done.append("3")
			else:
				print("Must input course information first")
				print("---")

		elif user == "4":
			if "4" in done:
				print("You already did this")
			elif "3" in done:
				student_info(student,course,student_number)
				print("---")
				done.append("4")
			else:
				print("Must input number of student first")
				print("---")

		elif user == "5":
			if "4" in done:
				select_course_n_input_marks(student, course)
				print("---")
			else:
				print("First 4 options must be done to continue")
				print("---")

		elif user == "6":
			if "4" in done:
				list_course(course)
				print("---")
			else:
				print("First 4 options must be done to continue")
				print("---")


		elif user == "7":
			if "4" in done:
				list_student(student, course)
				print("---")
			else:
				print("First 4 options must be done to continue")
				print("---")

		elif user == "8":
			if "4" in done:
				show_mark_from_chosen_course(student, course)
				print("---")
			else:
				print("First 4 options must be done to continue")
				print("---")

		else:
			print("Please enter a valid option")

main()