import pandas


data = pandas.read_csv("hw1.part1.1.txt", delim_whitespace=True, header=None)

#convert data into a dict with item as a key and list of tuples as anotator&label pairs

basic_dict = {} 
by_annotator_dict = {'annotator:0':{'label:0':0, 'label:1':0, 'label:2':0}, 
                     'annotator:1':{'label:0':0, 'label:1':0, 'label:2':0}} #creating nested dictionaries for labels of two annotators
for index, row in data.iterrows():
	item = row[0]
	annotator = row[1]
	label = row[2]
	val = basic_dict.get(item, [])
	# if val == None:
	# 	val = []
	val.append((annotator,label))
	basic_dict[item] = val
	by_annotator_dict[annotator][label] += 1

#calculate Cohen's k

nb_items = len(basic_dict)
agreements = 0 #agreements bw 1 and 2 annotaters of each item
for key, val in basic_dict.items():
	if val[0][1] == val[1][1]: #if labels inside one items are the same
		agreements +=1

p_o = agreements/nb_items #observed agreement rate

p_e = 0 #expected agreement
anns = list(by_annotator_dict.keys())
for label, label_cnt in by_annotator_dict[anns[0]].items():
	p_e += label_cnt/nb_items * by_annotator_dict[anns[1]][label]/nb_items

cohens_k = (p_o - p_e)/(1 - p_e) #Cohen's k
print("Cohen's k = " + str(cohens_k))





		


