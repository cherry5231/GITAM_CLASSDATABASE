class GITAM:
  text=  "                                   Welcome to GITAM University                 "
  print(text.upper())
class Campus:
       text2 ="-> GITAM has three campuses in India         "
       print(text2.upper())
       def __init__(self,Campus1):
           self.Campus1=Campus1
           
       def show_info(self):
               print(self.Campus1)
              
Vizag     = Campus("Gitam has its main campus in Visakhapatnam  with a lot of spaceous buildings and is considered as the coolest campus out of three")
Hyderabad = Campus("Gitam has its second campus in Hyderabad which is also very good and has a lot of facilities")
Bangalore = Campus("Gitam has its third campus in Bangalore which is also very good and has a lot of facilities")   
Vizag.show_info()
Hyderabad.show_info()
Bangalore.show_info() 
class school:
    text3 = "->Gitam has 12 Schools total:"
    print( text3.upper() )
    def __init__(self,school1,School2,School3,School4,School5,School6,School7,School8,School9,School10,School11,School12):
        self.school1=school1
        self.School2=School2
        self.School3=School3
        self.School4=School4
        self.School5=School5
        self.School6=School6
        self.School7=School7
        self.School8=School8
        self.School9=School9
        self.School10=School10
        self.School11=School11
        self.School12=School12
    def show_info(self):
        print(self.school1)
        print(self.School2)
        print(self.School3)
        print(self.School4)
        print(self.School5)
        print(self.School6)
        print(self.School7)
        print(self.School8)
        print(self.School9)
        print(self.School10)
        print(self.School11)
        print(self.School12)
Schools =school("School of Technology","School of Business","School of Science","School of Pharmacy","School of Law","School of Architecture","Humanities & Social Sciences","Medicine","Nursing","Physiotherapy","Allied Health Sciences","Public Policy / Education-related institutes")
Schools.show_info()
text4 = "Gitam has many branches for each school, making it one of the universities with the most amount of branches with wide range of courses in India\n"
print(text4.upper() )
class School_of_Technology:
    text5 = "->For School of Technology:"
    print(text5.upper())
  
    def __init__(self,Branch1,Branch2,Branch3,Branch4,Branch5,Branch6,Branch7,Branch8,Branch9,Branch10,Branch11,Branch12,Branch13,Branch14,Branch15,Branch16,Branch17,Branch18):
        self.Branch1=Branch1
        self.Branch2=Branch2
        self.Branch3=Branch3
        self.Branch4=Branch4
        self.Branch5=Branch5
        self.Branch6=Branch6
        self.Branch7=Branch7
        self.Branch8=Branch8
        self.Branch9=Branch9
        self.Branch10=Branch10
        self.Branch11=Branch11
        self.Branch12=Branch12
        self.Branch13=Branch13
        self.Branch14=Branch14
        self.Branch15=Branch15
        self.Branch16=Branch16
        self.Branch17=Branch17
        self.Branch18=Branch18
    def show_info(self):
        print(self.Branch1)
        print(self.Branch2)
        print(self.Branch3)
        print(self.Branch4)
        print(self.Branch5)
        print(self.Branch6)
        print(self.Branch7)
        print(self.Branch8)
        print(self.Branch9)
        print(self.Branch10)
        print(self.Branch11)
        print(self.Branch12)
        print(self.Branch13)
        print(self.Branch14)
        print(self.Branch15)
        print(self.Branch16)
        print(self.Branch17)
        print(self.Branch18)

tech = School_of_Technology("Computer Science and Engineering (CSE)","CSE (Artificial Intelligence & Machine Learning)","CSE (Cyber Security)","CSE (Data Science)","Artificial Intelligence & Data Science (AI&DS)","Computer Science and Business Systems (in some campuses)","M.Tech CSE","PhD in CSE/AI","Aerospace Engineering","Civil Engineering","Civil Engineering with Computer Applications","Mechanical Engineering","Electrical Engineering","Electronics & Communication Engineering (ECE)","Electronics Engineering (VLSI Design & Technology)","Robotics & AI","Biomedical Engineering","Biotechnology Engineering")
tech.show_info()
class School_of_Science:
    text6 = "->For School of Science:"
    print(text6.upper())
    def __init__(self,Branch1,Branch2,Branch3,Branch4,Branch5,Branch6,Branch7,Branch8,Branch9,Branch10):
        self.Branch1=Branch1
        self.Branch2=Branch2
        self.Branch3=Branch3
        self.Branch4=Branch4
        self.Branch5=Branch5
        self.Branch6=Branch6
        self.Branch7=Branch7
        self.Branch8=Branch8
        self.Branch9=Branch9
        self.Branch10=Branch10
    def show_info(self):
        print(self.Branch1)
        print(self.Branch2)
        print(self.Branch3)
        print(self.Branch4)
        print(self.Branch5)
        print(self.Branch6)
        print(self.Branch7)
        print(self.Branch8)
        print(self.Branch9)
        print(self.Branch10)
sci = School_of_Science("Mathematics","Physics","Chemistry","Statistics","Environmental Science","Food Science & Technology","Biotechnology","Microbiology","Data Science","Computational Sciences")
sci.show_info()
class School_of_Business:
    text7 = "->For School of Business:"
    print(text7.upper())
    def __init__(self,Branch1,Branch2,Branch3,Branch4,Branch5,Branch6,Branch7,Branch8,Branch9,Branch10):
        self.Branch1=Branch1
        self.Branch2=Branch2
        self.Branch3=Branch3
        self.Branch4=Branch4
        self.Branch5=Branch5
        self.Branch6=Branch6
        self.Branch7=Branch7
        self.Branch8=Branch8
        self.Branch9=Branch9
        self.Branch10=Branch10
    def show_info(self):
        print(self.Branch1)
        print(self.Branch2)
        print(self.Branch3)
        print(self.Branch4)
        print(self.Branch5)
        print(self.Branch6)
        print(self.Branch7)
        print(self.Branch8)
        print(self.Branch9)
        print(self.Branch10)
bus = School_of_Business("BBA","B.Com","MBA","Business Analytics","Financial Analysis","Marketing","Human Resource Management","Operations and supply chain","International Business","Hospitality Management")
bus.show_info()
class School_of_Pharmacy:
    text8 = "->For School of Pharmacy:"
    print(text8.upper())
    def __init__(self,Branch1,Branch2,Branch3,Branch4,Branch5,Branch6,Branch7,Branch8):
        self.Branch1=Branch1
        self.Branch2=Branch2
        self.Branch3=Branch3
        self.Branch4=Branch4
        self.Branch5=Branch5
        self.Branch6=Branch6
        self.Branch7=Branch7
        self.Branch8=Branch8
    def show_info(self):
        print(self.Branch1)
        print(self.Branch2)
        print(self.Branch3)
        print(self.Branch4)
        print(self.Branch5)
        print(self.Branch6)
        print(self.Branch7)
        print(self.Branch8)
pharm = School_of_Pharmacy("B.Pharm","Pharm.D","M.Pharm","Pharmaceutical Analysis","Pharmaceutics","Pharmacology","Pharmaceutical Chemistry","Pharmacy Practice")
pharm.show_info()
class School_of_Architecture:
    text9 = "->For School of Architecture:"
    print(text9.upper())
    def __init__(self,Branch1,Branch2,Branch3,Branch4):
        self.Branch1=Branch1
        self.Branch2=Branch2
        self.Branch3=Branch3
        self.Branch4=Branch4
    def show_info(self):
        print(self.Branch1)
        print(self.Branch2)
        print(self.Branch3)
        print(self.Branch4)
arch = School_of_Architecture("Bachelor of Architecture (B.Arch)","Interior Design","Planning","Sustainable Architecture")
arch.show_info()
class School_of_Law:
    text10 = "->For School of Law:"
    print(text10.upper())
    def __init__(self,Branch1,Branch2,Branch3,Branch4,Branch5,Branch6,Branch7):
        self.Branch1=Branch1
        self.Branch2=Branch2
        self.Branch3=Branch3
        self.Branch4=Branch4
        self.Branch5=Branch5
        self.Branch6=Branch6
        self.Branch7=Branch7
    def show_info(self):
        print(self.Branch1)
        print(self.Branch2)
        print(self.Branch3)
        print(self.Branch4)
        print(self.Branch5)
        print(self.Branch6)
        print(self.Branch7)
law = School_of_Law("BA LLB (Hons)","BBA LLB (Hons)","LLB","LLM","Corporate Law","International Law","Intellectual Property Rights")
law.show_info()
class School_of_Humanities_and_Social_Sciences:
    text11 = "->For School of Humanities and Social Sciences:"
    print(text11.upper())
    def __init__(self,Branch1,Branch2,Branch3,Branch4,Branch5,Branch6,Branch7,Branch8,Branch9):
        self.Branch1=Branch1
        self.Branch2=Branch2
        self.Branch3=Branch3
        self.Branch4=Branch4
        self.Branch5=Branch5
        self.Branch6=Branch6
        self.Branch7=Branch7
        self.Branch8=Branch8
        self.Branch9=Branch9
    def show_info(self):
        print(self.Branch1)
        print(self.Branch2)
        print(self.Branch3)
        print(self.Branch4)
        print(self.Branch5)
        print(self.Branch6)
        print(self.Branch7)
        print(self.Branch8)
        print(self.Branch9)
hss = School_of_Humanities_and_Social_Sciences("English","Economics","Psychology","Public Administration","Sociology","Political Science","History","Journalism","Liberal Arts")
hss.show_info()
class School_of_Medicine:
    text12 = "->For School of Medicine:"
    print(text12.upper())
    def __init__(self,Branch1,Branch2,Branch3,Branch4,Branch5,Branch6,Branch7,Branch8,Branch9,Branch10,Branch11,Branch12):
        self.Branch1=Branch1
        self.Branch2=Branch2
        self.Branch3=Branch3
        self.Branch4=Branch4
        self.Branch5=Branch5
        self.Branch6=Branch6
        self.Branch7=Branch7
        self.Branch8=Branch8
        self.Branch9=Branch9
        self.Branch10=Branch10
        self.Branch11=Branch11
        self.Branch12=Branch12  
    def show_info(self):
        print(self.Branch1)
        print(self.Branch2)
        print(self.Branch3)
        print(self.Branch4)
        print(self.Branch5)
        print(self.Branch6)
        print(self.Branch7) 
        print(self.Branch8)
        print(self.Branch9)
        print(self.Branch10)
        print(self.Branch11)
        print(self.Branch12)
med = School_of_Medicine("MBBS","Anatomy","Physiology","Biochemistry","General Medicine","General Surgery","Pediatrics","Orthopedics","ENT","Dermatology","Radiology","Emergency Medicine")
med.show_info()
class School_of_Nursing:
    text13 = "->For School of Nursing:"
    print(text13.upper())
    def __init__(self,Branch1,Branch2,Branch3,Branch4,Branch5,Branch6):
        self.Branch1=Branch1
        self.Branch2=Branch2
        self.Branch3=Branch3
        self.Branch4=Branch4
        self.Branch5=Branch5
        self.Branch6=Branch6
    def show_info(self):
        print(self.Branch1)
        print(self.Branch2)
        print(self.Branch3)
        print(self.Branch4)
        print(self.Branch5)
        print(self.Branch6)
nurs = School_of_Nursing("B.Sc Nursing","M.Sc Nursing","Community Health Nursing","Medical Surgical Nursing","Pediatric Nursing","Psychiatric Nursing")
nurs.show_info()
class School_of_Physiotherapy:
    text14 = "->For School of Physiotherapy:"
    print(text14.upper())
    def __init__(self,Branch1,Branch2,Branch3,Branch4,Branch5):
        self.Branch1=Branch1
        self.Branch2=Branch2
        self.Branch3=Branch3
        self.Branch4=Branch4
        self.Branch5=Branch5
    def show_info(self):
        print(self.Branch1)
        print(self.Branch2)
        print(self.Branch3)
        print(self.Branch4)
        print(self.Branch5)
physio = School_of_Physiotherapy("BPT","MPT","Cardiopulmonary Physiotherapy","Neurological Physiotherapy","Musculoskeletal/Sports Physiotherapy")
physio.show_info()
class School_of_Allied_Health_Sciences:
    text15 = "->For School of Allied Health Sciences:"
    print(text15.upper())
    def __init__(self,Branch1,Branch2,Branch3,Branch4,Branch5,Branch6,Branch7):
        self.Branch1=Branch1
        self.Branch2=Branch2
        self.Branch3=Branch3
        self.Branch4=Branch4
        self.Branch5=Branch5
        self.Branch6=Branch6
        self.Branch7=Branch7
    def show_info(self):
        print(self.Branch1)
        print(self.Branch2)
        print(self.Branch3)
        print(self.Branch4)
        print(self.Branch5)
        print(self.Branch6)
        print(self.Branch7)
allied = School_of_Allied_Health_Sciences("Medical Lab Technology","Radiology & Imaging Technology","Operation Theatre Technology","Emergency & Trauma Care","Dialysis Technology","Physician Assistant","Optometry")
allied.show_info()
class School_of_Public_Policy_and_Education_related_institutes:
    text16 = "->For School of Public Policy and Education-related institutes:"
    print(text16.upper())
    def __init__(self,Branch1,Branch2,Branch3,Branch4):
        self.Branch1=Branch1
        self.Branch2=Branch2
        self.Branch3=Branch3
        self.Branch4=Branch4
       
    def show_info(self):
        print(self.Branch1)
        print(self.Branch2)
        print(self.Branch3)
        print(self.Branch4)
pp = School_of_Public_Policy_and_Education_related_institutes("Public Policy","Education","Leadership Studies","Governance & Administration")
pp.show_info()


    