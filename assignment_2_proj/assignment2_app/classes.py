# Where we shall write our python classes for Project Details
class Members:
    def __init__(self, name, course, age, ethnicity):
        self.name = name
        self.course = course
        self.age = age
        self.ethnicity = ethnicity

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
        self.supervisor = supervisor
        self.title = title
        self.category = category
        self.topic_num = topic_num
        self.casuarina = casuarina
        self.sydney = sydney
        self.external = external
        self.chemical_engineering = chem_eng
        self.civil_and_structural_engineering = civ_eng
        self.electrical_and_electronics_engineering = elec_eng
        self.mechanical_engineering = mec_eng
        self.computer_science = com_sci
        self.cyber_security = cyber
        self.data_science = data_sci
        self.information_systems_and_data_science = info_sys
        self.software_engineering = soft_eng

    def location(self):
        return {
            "casuarina": self.casuarina,
            "sydney": self.sydney,
            "external": self.external,
        }

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
    False,
    False,
    False,
    False,
    True,
    False,
    False,
    True,
    True,
)

print(proj1.category)

# proj2 = ProjectsClass()
# proj3 = ProjectsClass()
# proj4 = ProjectsClass()
# proj5 = ProjectsClass()
# proj6 = ProjectsClass()
# proj7 = ProjectsClass()




projects_list = []
