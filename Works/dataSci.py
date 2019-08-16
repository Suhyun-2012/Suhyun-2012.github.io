import school_scores
list_of_record = school_scores.get_all()
import matplotlib.pyplot as bar

#print(list_of_record)

arts_music = []
eng = []
math = []
hist = []
nats = []
lang = []


#for i in list_of_record:
    #am = i["Academic Subjects"]["Arts/Music"]["Average GPA"]
    #arts_music.append(am)
    #e = list_of_record["Academic Sunjects"]["English"][i]
    #print(arts_music)
#sum = sum(arts_music)
#avg = sum/(len(arts_music))
#print(avg)
#3.8227036395147382

for i in list_of_record:
    e = i["Academic Subjects"]["English"]["Average GPA"]
    eng.append(e)
    #e = list_of_record["Academic Sunjects"]["English"][i]
    #print(eng)
sum2 = sum(eng)
avg2 = sum/(len(eng))
print(avg2)
