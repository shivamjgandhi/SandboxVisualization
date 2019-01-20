from bs4 import BeautifulSoup
import nltk
import operator
import matplotlib.pyplot as plt
import numpy as np

text = open("database.txt", "r")
lines = text.read().splitlines()

helpful_skills = []
for line in lines:
	if line[0:14] == 'Can help with:':
		skills_list = line[14:]
		individual_skills = [x.strip() for x in skills_list.split(',')]
		helpful_skills += individual_skills

skill_count = {}
for i in range(len(helpful_skills)):
	helpful_skills[i] = helpful_skills[i].lower()
	if (helpful_skills[i] in skill_count):
		skill_count[helpful_skills[i]] += 1
	else:
		skill_count[helpful_skills[i]] = 1

if '' in skill_count:
	skill_count.pop('', None)

sorted_skills = sorted(skill_count.items(), key=operator.itemgetter(1))
# top_skills = {}
# sorted_skills_list = list(sorted_skills)
# print(sorted_skills)
# for i in range(20):
# 	top_skills[sorted_skills_list[i][0]] = sorted_skills_list[i][1]

# print(top_skills)
skills = list(zip(*sorted_skills))[0]
occurence = list(zip(*sorted_skills))[1]
skill_pos = np.arange(len(skills))

plt.bar(skill_pos, occurence, align='center')
plt.xticks(skill_pos, skills)
plt.ylabel('frequency')
plt.show()
