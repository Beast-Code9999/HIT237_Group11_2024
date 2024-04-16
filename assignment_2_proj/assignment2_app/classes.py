# Where we shall write our python classes for Project Details
class Member:
    def __init__(self, name, course, age, ethnicity):
        self.name = name
        self.course = course
        self.age = age
        self.ethnicity = ethnicity

# use tuples here

class ProjectsClass:
    def __init__(
        self,
        supervisor,
        title,
        category,
        topic_num,
        casuarina,
        sydney,
        external,
    ):
        self.supervisor = supervisor
        self.title = title
        self.category = category
        self.topic_num = topic_num
        self.casuarina = casuarina
        self.sydney = sydney
        self.external = external

    def location(self):
        location_array = []

        if self.casuarina == True:
            location_array.append("Casuarina")
        if self.sydney == True:
            location_array.append("Sydney")
        if self.external == True:
            location_array.append("External")

        return location_array


class ProjectsCategoryClass:
    def __init__(
        self,
        chem_eng,
        civ_eng,
        elec_eng,
        mec_eng,
        com_sci,
        cyber,
        data_sci,
        info_sys,
        soft_eng,
    ):
        self.chemical_engineering = chem_eng
        self.civil_and_structural_engineering = civ_eng
        self.electrical_and_electronics_engineering = elec_eng
        self.mechanical_engineering = mec_eng
        self.computer_science = com_sci
        self.cyber_security = cyber
        self.data_science = data_sci
        self.information_systems_and_data_science = info_sys
        self.software_engineering = soft_eng



    def fields(self):
        return {
            "Chemical Engineering": self.chemical_engineering,
            "Civil and Structural Engineering": self.civil_and_structural_engineering,
            "Electrical and Electronics Engineering": self.electrical_and_electronics_engineering,
            "Mechanical Engineering": self.mechanical_engineering,
            "Computer Science": self.computer_science,
            "Cyber Security": self.cyber_security,
            "Data Science": self.data_science,
            "Information Systems and Data Science": self.information_systems_and_data_science,
            "Software Engineering": self.software_engineering,
        }
    

proj1 = ProjectsClass(
    "Bharanidharan Shanmugam",
    "Machine Learning Approaches for Cyber Security",
    "Artificial Intelligence, Machine learning and Data Science",
    9,
    True,
    True,
    True,
)
proj2 = ProjectsClass(
    "Yakub Sebastian",
    "Machine Learning Approaches for Cyber Security",
    "Artificial Intelligence, Machine learning and Data Science",
    9,
    True,
    True,
    True,
)
proj3 = ProjectsClass(
    "Bharanidharan Shanmugam",
    "Machine Learning Approaches for Cyber Security",
    "Artificial Intelligence, Machine learning and Data Science",
    9,
    True,
    True,
    True,
)
proj4 = ProjectsClass(
    "Bharanidharan Shanmugam",
    "Machine Learning Approaches for Cyber Security",
    "Artificial Intelligence, Machine learning and Data Science",
    9,
    True,
    True,
    True,
)
proj5 = ProjectsClass(
    "Bharanidharan Shanmugam",
    "Machine Learning Approaches for Cyber Security",
    "Artificial Intelligence, Machine learning and Data Science",
    9,
    True,
    True,
    True,
)
proj6 = ProjectsClass(
    "Bharanidharan Shanmugam",
    "Machine Learning Approaches for Cyber Security",
    "Artificial Intelligence, Machine learning and Data Science",
    9,
    True,
    True,
    True,
)
proj7 = ProjectsClass(
    "Bharanidharan Shanmugam",
    "Machine Learning Approaches for Cyber Security",
    "Artificial Intelligence, Machine learning and Data Science",
    9,
    True,
    True,
    True,
)

projects_list = [proj1.__dict__, proj2.__dict__, proj3.__dict__, proj4.__dict__, proj5.__dict__, proj6.__dict__, proj7.__dict__]

# print(proj1.location())
# print(proj1.__dict__)
print(projects_list)

# proj2 = ProjectsClass()
# proj3 = ProjectsClass()
# proj4 = ProjectsClass()
# proj5 = ProjectsClass()
# proj6 = ProjectsClass()
# proj7 = ProjectsClass()




projects_list = []
