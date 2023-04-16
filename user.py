pr_st = [
	873810534,
	208967221
]

def is_coder(user_id):
	print(user_id)
	if user_id in pr_st:
		return True
	else:
		return False

def get_student_id(user_id):
	for programmer in pr_st:
		if programmer == user_id:
			return pr_st[programmer]

def get_coder_id(user_id):
	students = list(pr_st.values())
	for student in students:
		if  student == user_id:
			pos = students.index(student)
			return list(pr_st.keys())[pos]

# Отправка документом
# Указатель от кого пришло задание
