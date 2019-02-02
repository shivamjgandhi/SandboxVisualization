
"""
All of the necessary imports and setup
"""
from bs4 import BeautifulSoup
# from mpl_toolkits.basemap import Basemap
import nltk
import operator
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

"""
This part returns the data from the Sandbox main website
"""
text = open("database.txt", "r")
lines = text.read().splitlines()

"""
This part creates the visualization for people's occupations
"""
# stop_words = stopwords.words('english')

"""
This part creates the visualizations for people's skillsets
"""
def skillset_vis(lines):
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
	top_skills = []
	sorted_skills_list = list(sorted_skills)

	for i in range(20):
		newArr = [sorted_skills_list[-i-1][0], sorted_skills_list[-i-1][1]]
		top_skills.append(newArr)

	barWidth = 0.9
	X = [x + 1 for x in list(range(20))]
	Y = [elem[1] for elem in top_skills]
	x_labels = [elem[0] for elem in top_skills]

	plt.bar(X, Y, width=barWidth, color=(0.3, 0.1, 0.4, 0.6))
	plt.xticks([r + barWidth for r in range(20)], x_labels, rotation=90)
	labels = [ 'n = ' + str(y) for y in Y]
	for i in range(20):
		plt.text(x = X[i]-0.5, y = Y[i]+0.1, s=labels[i])
	plt.subplots_adjust(bottom=0.2, top=0.98)
	plt.show()

"""
This part creates the visualization for what people do as a profession
"""
def profession_visualization(lines):
	professions = []
	for line in lines:
		line = line.split()
		if line[-1][-1] == ')' or line[0] == 'Linkedin' or line[0] == 'Slack'or line[0] == 'Can':
			

"""
This part creates the visualization for where people are from
"""
def places_visualization(lines):
	lines = lines[:-2]
	places_list = []
	for line in lines:
		line = line.split()
		if line[-1][0] == "(":
			unprocessed_location = line[-1]
			processed_location = ""
			for letter in unprocessed_location:
				if letter.isalpha():
					processed_location = processed_location + letter
			places_list.append(processed_location)

	city_count = {}
	for i in range(len(places_list)):
		if (places_list[i] in city_count):
			city_count[places_list[i]] += 1
		else:
			city_count[places_list[i]] = 1

	sorted_locations = sorted(city_count.items(), key=operator.itemgetter(1))
	top_locations = []
	sorted_locations_list = list(sorted_locations)

	for i in range(10):
		newArr = [sorted_locations_list[-i-1][0], sorted_locations_list[-i-1][1]]
		top_locations.append(newArr)

	barWidth = 0.9
	X = [x + 1 for x in list(range(10))]
	Y = [elem[1] for elem in top_locations]
	x_labels = [elem[0] for elem in top_locations]

	plt.bar(X, Y, width=barWidth, color=(0.3, 0.1, 0.4, 0.6))
	plt.xticks([r + barWidth for r in range(10)], x_labels, rotation=90)
	labels = [ 'n = ' + str(y) for y in Y]
	for i in range(10):
		plt.text(x = X[i]-0.5, y = Y[i]+0.1, s=labels[i])
	plt.subplots_adjust(bottom=0.2, top=0.98)
	plt.show()

# Create the map with all of the sandbox hubs
# data = pd.DataFrame

places_visualization(lines)