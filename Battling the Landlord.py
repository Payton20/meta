import random
daletou_qian = [i for i in range (1,36)]
daletou_hou = [i for i in range(1,13)]
daletou_qian_random = random.sample(daletou_qian, k = 5)
daletou_hou_random = random.sample(daletou_hou,  k = 2)
print(daletou_qian_random, daletou_hou_random)


# Poker resuffling 
poker_num = [str(i) for i in range(2,11)]
poker_str = ["A","J","Q","K"]
poker_king = ["Harlequin", "Bandit"]
print(poker_num)
poker_color = ["Club ","Diamond ","Heart ","Spade "]

# List of Cards / Total Numbers
pokers = ["%s%s" %(i,j) for i in poker_color for j in poker_num + poker_str] + poker_king
print(len(pokers))
print(pokers)

# shuffling
random.shuffle(pokers)
print(pokers)

# battling the landlord 
# (http://www.chinadaily.com.cn/english/doc/2004-04/10/content_322207.htm)
person_a = pokers[0:51:3]
person_b = pokers[1:51:3]
person_c = pokers[2:51:3]
last_3 = pokers[-3:]
print("person_a:", person_a)
print("persom_b:", person_b)
print("person_c:", person_c)
