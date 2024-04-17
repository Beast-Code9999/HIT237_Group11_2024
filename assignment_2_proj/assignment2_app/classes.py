# Where we shall write our python classes for Project Details
class Member:
    def __init__(self, name, id, course, age, nationality, img):
        self.name = name
        self.id = id
        self.course = course
        self.age = age
        self.nationality = nationality
        self.img = img

# use tuples here

Jason = Member(
    "Jason Khung Siong Lay",
    "(S365475)",
    "Bachelor of Coomputer Science (second year)",
    "21-years-old",
    "Timorese",
    "FB_IMG_1709708766525.jpg",
)
Micia = Member(
    "Micia Correia Gusmao",
    "(S367733)",
    "Bachelor of Coomputer Science (second year)",
    "19-years-old",
    "Indian",
    "micia-pic.jpg",
)
Tirth = Member(
    "Tirth Jyotikar",
    "(S361950)",
    "Bachelor of Information Technology (second year)",
    "20-years-old",
    "Indian",
    "Tirth.jpg",
)
Zandro = Member(
    "Zandro Uriel Getuya",
    "(S366139)",
    "Bachelor of Information Technology (second year)",
    "19-years-old",
    "Filipino",
    "Zandro.jpeg",
)

members_list = [Jason.__dict__, Micia.__dict__, Tirth.__dict__, Zandro.__dict__]


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
        location,
    ):
        self.supervisor = supervisor
        self.title = title
        self.category = category
        self.topic_num = topic_num
        self.casuarina = casuarina
        self.sydney = sydney
        self.external = external
        self.location = location
    

proj1 = ProjectsClass(
    "Bharanidharan Shanmugam",
    "Machine Learning Approaches for Cyber Security",
    "Artificial Intelligence, Machine learning and Data Science",
    1,
    True,
    True,
    True,
    "Internal - Casuarina, Internal - Sydney, External"
)
proj2 = ProjectsClass(
    "Yakub Sebastian",
    "Informetrics applications in multidisciplinary domain",
    "Artificial Intelligence, Machine learning and Data Science",
    9,
    True,
    True,
    True,
    "Internal - Casuarina, Internal - Sydney, External",
)
proj3 = ProjectsClass(
    "Sami Azam",
    "Development of a Virtual Reality System to Test Binaural Hearing",
    "Biomedical Engineering and Health Informatics",
    16,
    True,
    False,
    True,
    "Internal - Casuarina, External",
)
proj4 = ProjectsClass(
    "Sami Azam",
    "Current trends on cryptomining and its potential impact on cryptocurrencies",
    "Cyber Security",
    41,
    True,
    True,
    True,
    "Internal - Casuarina, Internal - Sydney, External",
)
proj5 = ProjectsClass(
    "Asif Karim",
    "Artificial Intelligence in Health Informatics",
    "Artificial Intelligence, Machine Learning and Data Science",
    176,
    True,
    True,
    True,
    "Internal - Casuarina, Internal - Sydney, External",
)
proj6 = ProjectsClass(
    "Asif Karim",
    "Unsupervised Model Development from Autism Screening Data ",
    "Artificial Intelligence, Machine Learning and Data Science",
    180,
    True,
    True,
    True,
    "Internal - Casuarina, Internal - Sydney, External",
)
proj7 = ProjectsClass(
    "Bharanidharan Shanmugam",
    "Applying Artificial Intelligence to solve real world problems",
    "Artificial Intelligence, Machine Learning and Data Science",
    226,
    True,
    True,
    True,
    "Internal - Casuarina, Internal - Sydney, External",
)

projects_list = [proj1.__dict__, proj2.__dict__, proj3.__dict__, proj4.__dict__, proj5.__dict__, proj6.__dict__, proj7.__dict__]

# print(proj1.location())
# print(proj1.__dict__)
print(projects_list)


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




