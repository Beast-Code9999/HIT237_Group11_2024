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
    "Jason.jpg",
)
Micia = Member(
    "Micia Correia Gusmao",
    "(S367733)",
    "Bachelor of Coomputer Science (second year)",
    "19-years-old",
    "Indian",
    "Micia.jpg",
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
        fields,
        description,
        slug
    ):
        self.supervisor = supervisor
        self.title = title
        self.category = category
        self.topic_num = topic_num
        self.casuarina = casuarina
        self.sydney = sydney
        self.external = external
        self.location = location
        self.fields = fields 
        self.description = description
        self.slug = slug

proj1 = ProjectsClass(
    "Bharanidharan Shanmugam",
    "Machine Learning Approaches for Cyber Security",
    "Artificial Intelligence, Machine learning and Data Science",
    1,
    True,
    True,
    True,
    "Internal - Casuarina, Internal - Sydney, External",
    "Computer Science, Information Systems and Data Science, Software Engineering",
    "As we use internet more, the data produced by us is enormous. But are these data being secure? The goal of applying machine learning or intelligence is to better risk modelling and prediction and for an informed decision support. Students will be working with either supervised or unsupervised machine learning approaches to solve the problem/s in the broader areas of Cyber Security.",
    "project-1"
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
    "Computer Science, Cyber Security, Data Science, Information Systems and Data Science, Software Engineering",
    "Informetrics studies are concerned with the quantitative aspects of information. The applications of advanced machine learning, information retrieval, network science and bibliometric techniques on various information artefact have contributed fresh insights into the evolutionary nature of research fields. This project aims at discovering informetric properties of multidisciplinary research literature using various machine learning, network analysis, data visualisation and data wrangling tools.",
    "project-9"

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
    "Electrical and Electronics Engineering, Computer Science, Software Engineering",
    "A virtual reality system could be used to objectively test the binaural hearing ability of humans (the ability to hear stereo and locate the direction and distance of sound). This project aims to design, implement and evaluate a VR system using standard off the shelf components (VR goggle and headphones) and standard programming techniques.",
    "project-16"

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
    "Computer Science, Cyber Security, Software Engineering",
    "Cryptomining is the process of mining crypto currencies by running a sequence of algorithms. Traditionally, to mine new crypto coins, a person (or group of people) would buy expensive computers and spend a lot of time and money running them to perform the difficult calculations to generate crypto coins. Some website owners have started taking a different approach; they have put the software which runs those difficult calculations into their website's Javascript. This then causes the computers belonging to the visitors of their website to run those calculations for them, instead of running them themselves. In other words, when you visit a website with an embedded crypto-miner in it, your computer and electricity is used to try to generate crypto-coins for the owners of that website. Although there are various measures being applied to stop these illegitimate minings, the trend is still increasing. This research aims to find out potential gaps in current methodologies and develop a solution that can fulfil the gap. It also aims to find out: \\n • What type crypto mining methodologies are being applied? \\n • Apart from crypto-mining, what other security risks may it introduce? For example: cryptojacking \\n • How current web standards are tackling this problem?",
    "project-41"
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
    "Electrical and Electronics Engineering, Computer Science, Data Science, Software Engineering",
    "The project aims to use multiple publicly available health datasets to formulate a different dataset that may have features from the original set along with new ones developed through feature engineering. The dataset will then be used to build predictive model based on both general and deep learning based algorithm. The findings will be analysed and compared to similar research works.",
    "project-176"
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
    "Electrical and Electronics Engineering, Computer Science, Data Science, Software Engineering",
    "The proposed system will present a two-cluster solution from a given dataset which will group toddlers based on multiple common medical traits. In depth literature survey of similar studies, both supervised and unsupervised will be carried out before the cluster-based model is implemented. The solution will be validated using both External and Internal validation measures and statistical significance tests.",
    "project-180"
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
    "Chemical Engineering, Electrical and Electronics Engineernig, Mechanical Engineering, Computer Science, Cyber Security, Data Science, Information Systems and Data Science, Software Engineering",
    "Artificial Intelligence has been used in many applications to solve certain problems through out the academia and the industry – from electricity to writing text. AI has a multitude of applications and this project will pick up a problem and explore the applications of AI with minimal human intervention. Examples of applications include -building a bot, predicting the power usage, spam filtering and the list is endless.",
    "project-226"
)

projects_list = [proj1.__dict__, proj2.__dict__, proj3.__dict__, proj4.__dict__, proj5.__dict__, proj6.__dict__, proj7.__dict__]

# print(proj1.location())
# print(proj1.__dict__)
print(projects_list)


# class ProjectsCategoryClass:
#     def __init__(
#         self,
#         chem_eng,
#         civ_eng,
#         elec_eng,
#         mec_eng,
#         com_sci,
#         cyber,
#         data_sci,
#         info_sys,
#         soft_eng,
#     ):
#         self.chemical_engineering = chem_eng
#         self.civil_and_structural_engineering = civ_eng
#         self.electrical_and_electronics_engineering = elec_eng
#         self.mechanical_engineering = mec_eng
#         self.computer_science = com_sci
#         self.cyber_security = cyber
#         self.data_science = data_sci
#         self.information_systems_and_data_science = info_sys
#         self.software_engineering = soft_eng




