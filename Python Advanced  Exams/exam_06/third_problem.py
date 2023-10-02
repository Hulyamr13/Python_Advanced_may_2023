def gather_credits(credits_needed, *courses):
    enrolled_courses = []
    gathered_credits = 0

    for course in courses:
        course_name, course_credits = course

        if gathered_credits >= credits_needed:
            break

        if course_name not in enrolled_courses:
            gathered_credits += course_credits
            enrolled_courses.append(course_name)

    if gathered_credits >= credits_needed:
        enrolled_courses.sort()
        return f"Enrollment finished! Maximum credits: {gathered_credits}.\nCourses: {', '.join(enrolled_courses)}"
    else:
        credits_shortage = credits_needed - gathered_credits
        return f"You need to enroll in more courses! You have to gather {credits_shortage} credits more."


print(gather_credits(
    80,
    ("Basics", 27),
))
print(gather_credits(
    80,
    ("Advanced", 30),
    ("Basics", 27),
    ("Fundamentals", 27),
))
print(gather_credits(
    60,
    ("Basics", 27),
    ("Fundamentals", 27),
    ("Advanced", 30),
    ("Web", 30)
))


