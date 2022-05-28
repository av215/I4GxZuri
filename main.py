class Student:
    name = ""
    age = ""
    track = ["full", "part", "contract"]
    score = ""

    # [assignment] Skeleton class. Add your code here
    def __init__():
       # self.name = name
        #self.age = age
       # self.track = track
       # self.score = score
        #pass

    def change_name(name):
        name = name
        return name

    def change_age(age):
        age = age
        return age

    def add_track(track):
        track = track.append(track)

    def get_score(score):
        return score

Bob = Student("Bob", 26, "part", 20.90)

# Expected methods
Bob.change_name("Peter")
Bob.change_age(34)
Bob.add_track("UI/UX")
Bob.get_score()
