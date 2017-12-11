# dict. keys are strings, values are sets
COURSES = {
    "Python Basics": {"Python", "functions", "variables",
                      "booleans", "integers", "floats",
                      "arrays", "strings", "exceptions",
                      "conditions", "input", "loops"},
    "Java Basics": {"Java", "strings", "variables",
                    "input", "exceptions", "integers",
                    "booleans", "loops"},
    "PHP Basics": {"PHP", "variables", "conditions",
                   "integers", "floats", "strings",
                   "booleans", "HTML"},
    "Ruby Basics": {"Ruby", "strings", "floats",
                    "integers", "conditions",
                    "functions", "input"}
}

# check for 'overlap'
def covers(user_set):
	overlap = []
	for course, topics in COURSES.items():
		print(user_set.intersection(topics))
		if user_set.intersection(topics): # overlap aka intersection
			overlap.append(course)
	print(overlap)
	return overlap

covers({'Python'})
