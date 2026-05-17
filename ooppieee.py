import sys

file = open("gitam_info.txt", "w", encoding="utf-8")
sys.stdout = file

import  oopsGitaminfo
class Clubs:
    Club_info = "\n Gitam has a lot of clubs that are very active and have a lot of members with events that gathered thousands of people across the campuses"
    Club_info2 = "These Clubs are very suppportive and tot those being part of the clubs enccourage them on scoial behaviour,able to handle and learn tasks that are not taught in any respective class,Gitam's clubs are blend of arts,creative events,fests that gather and bring together all kinds of people,tech based clubs that teach technological values,social clubs that teach a lot of social values and many more"
    print(Club_info.upper())
    print(Club_info2.upper())
    def __init__(self,ClubName,ClubDescription):
        self.ClubName=ClubName
        self.ClubDescription=ClubDescription
    def show_info(self):
       print(self.ClubName)
       for number, i in enumerate(self.ClubDescription, start=1):
           print(f"{number}. {i}")
           
club_info = Clubs(" \nCOMMON GITAM CLUBS",
                  ["Anime Manga Club — Community for anime, manga, cosplay, and Japanese pop-culture fans.",
"Google Developer Student Club — Tech club focused on coding, app development, workshops, and Google technologies.",
"GitHub Community Club — Helps students learn open-source collaboration, Git, and GitHub projects.",
"Cybersecurity Club / CYSEC — Focuses on ethical hacking, cyber awareness, and security-related events.",
"Kalakrithi Cultural Club — Organizes dance, music, fashion, and cultural performances during festivals.",
"G-Studio — Media and photography club covering events, editing, videography, and creative content.",
"Entrepreneurship Club (E-Club) — Encourages startups, business ideas, innovation, and networking.",
"GITAM Quiz Club (GQC) — Conducts quizzes and intellectual competitions across various topics.",
"Korean Culture Club — Celebrates Korean language, K-dramas, K-pop, food, and traditions.",
"NSS (National Service Scheme) — Social-service club involved in volunteering, awareness drives, and community work.",
"NCC (National Cadet Corps) — Discipline and leadership-focused cadet organization with training activities.",
"Debate Society — Club for debating, public speaking, discussions, and argument-building skills.",
"Literary Club — Focuses on writing, poetry, storytelling, reading, and language activities.",
"Cooking Club — Community for students interested in cooking, recipes, and food events.",
"Rotaract Club — Student-led social service and leadership organization connected to Rotary initiatives.",
"GMUN / Model United Nations — Simulates UN-style debates where students represent countries and discuss global issues.",
"Innovation Center — Supports student innovation, research ideas, projects, and startup development.",
"Women Leaders Forum — Promotes women empowerment, leadership, networking, and career development.",
"Toastmasters Club — Helps students improve communication, confidence, and public-speaking skills."])
club_info.show_info()
class fests:
    def __init__(self,fest,fest_info):
      self.fest = fest
      self.fest_info = fest_info
    def show_info(self):
        print(self.fest) 
        for number, i in enumerate(self.fest_info, start = 1):
            print(f"{number}.{i}")
fest_info = fests("\nHERE ARE POPULAR GITAM FESTS WITH 1000+ STUDENTS:",
                  ["Shore Fest-A large beach-side cultural celebration mainly associated with the Visakhapatnam campus featuring music, performances, fun activities, and student entertainment.",

"GMUN Fest / GITAM Model United Nations-A diplomatic simulation event where students represent countries, debate global issues, improve public speaking, negotiation, and leadership skills.",

"Homecoming-An alumni-centered celebration where former students reconnect with campus life, juniors, faculty, and major university events.",

"Kalakrithi Fest- A Cultural arts festival focused on dance, music, fashion, drama, and creative performances by students across different schools and campuses.",

"Freshers Party-A welcoming event organized for first-year students to help them socialize, interact with seniors, and experience campus culture."])
fest_info.show_info()
class library:
    def __init__(self,Library):
        print("GITAM's LIBRARY STRUCTURE:")
        self.Library = Library
    def show_info(self):
         for number, i in enumerate(self.Library, start = 1):
          print(f"{number}.{i}")
library_info = library(["Central Library-GITAM libraries provide large collections of books, research journals, digital resources, and quiet reading spaces.",

"Digital Library-Students can access e-books, online journals, IEEE papers, and research databases for academic learning.",

"Reading Halls-Dedicated study areas designed for focused learning and group discussions."])
library_info.show_info()
class Hostel:
     
 
    def __init__(self,hostel,hostel_info):
        self.hostel = hostel
        self.hostel_info = hostel_info
        
       

    def show_info(self):

        print(self.hostel)
        for number, i in enumerate(self.hostel_info, start=1):
            print(f"{number}. {i}")
        print()

hostel = Hostel("\n GITAM HAS MANY HOSTEL FACILITIES", [
    "HOSTELS: Boys Hostel, Girls Hostel, Mess & Food Courts, Gym & Recreation",
    "SPORTS: Cricket, Basketball, Badminton, Fitness Centers",
    "PLACEMENTS: Placement Cell, Top Recruiters, Internships, Skill Development",
    "FACILITIES: Smart Classrooms, Laboratories, Auditorsiums, Transportation, Medical Facilities",
    "STUDENT ACHIEVEMENTS: Hackathons, Research Projects, Cultural Achievements, Sports Achievements",
    "CAMPUS LIFE: Cultural Diversity, Student Communities, Events & Celebrations, Learning Beyond Classroom"
])

hostel.show_info()
class Sports:
    def __init__(self):
        self.title = "SPORTS"
        self.data = [
            "Cricket",
            "One of the most popular sports activities with tournaments and practice grounds across campuses.",
            "Basketball",
            "Well-maintained courts and inter-college competitions encourage student participation.",
            "Badminton",
            "Indoor badminton facilities are available for practice and tournaments.",
            "Fitness Centers",
            "Campus gyms and fitness centers support student health and physical development."
        ]

    def show(self):
        print("\n" + self.title)
        for i, item in enumerate(self.data, start=1):
            print(f"{i}. {item}")
        print()


class Placements:
    def __init__(self):
        self.title = "PLACEMENTS"
        self.data = [
            "Placement Cell",
            "GITAM’s placement department helps students prepare for jobs through training and recruitment drives.",
            "Top Recruiters",
            "Companies from software, consulting, banking, healthcare, and core engineering sectors visit campuses.",
            "Internship Programs",
            "Students get real-world industry experience through internships.",
            "Skill Development",
            "Training programs focus on aptitude, coding, communication, and interview preparation."
        ]

    def show(self):
        print("\n" + self.title)
        for i, item in enumerate(self.data, start=1):
            print(f"{i}. {item}")
        print()


class Facilities:
    def __init__(self):
        self.title = "FACILITIES"
        self.data = [
            "Smart Classrooms",
            "Modern classrooms with projectors, digital boards, and advanced teaching tools.",
            "Laboratories",
            "Engineering, pharmacy, science, and research labs.",
            "Auditoriums",
            "Used for seminars, cultural events, workshops, and guest lectures.",
            "Transportation",
            "Bus services across multiple routes for students and staff.",
            "Medical Facilities",
            "On-campus healthcare and medical support services."
        ]

    def show(self):
        print("\n" + self.title)
        for i, item in enumerate(self.data, start=1):
            print(f"{i}. {item}")
        print()


class StudentAchievements:
    def __init__(self):
        self.title = "STUDENT ACHIEVEMENTS"
        self.data = [
            "Hackathons",
            "Students participate in coding competitions and innovation challenges.",
            "Research Projects",
            "Students develop research papers and prototypes.",
            "Cultural Achievements",
            "Wins in dance, music, theatre, and arts competitions.",
            "Sports Achievements",
            "Participation in university and national-level sports events."
        ]

    def show(self):
        print("\n" + self.title)
        for i, item in enumerate(self.data, start=1):
            print(f"{i}. {item}")
        print()


class CampusLife:
    def __init__(self):
        self.title = "CAMPUS LIFE"
        self.data = [
            "Cultural Diversity",
            "Students from different states and backgrounds live together.",
            "Student Communities",
            "Clubs help build teamwork, leadership, and friendships.",
            "Events & Celebrations",
            "Festivals, concerts, and cultural nights throughout the year.",
            "Learning Beyond Classroom",
            "Students gain skills, experience, and networking outside academics."
        ]

    def show(self):
        print("\n" + self.title)
        for i, item in enumerate(self.data, start=1):
            print(f"{i}. {item}")
        print()
sports = Sports()
placements = Placements()
facilities = Facilities()
achievements = StudentAchievements()
campus = CampusLife()

sports.show()
placements.show()
facilities.show()
achievements.show()
campus.show()

file.close()
                  
                  
                  
                  
                  
                  
                  