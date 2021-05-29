topic = ["Name", "Roll", "Email", "Phone"]
for i in range(len(topic)):
    data = list(input(f"Enter your {topic[i]} :"))

    print(f"Your {topic[i]} is {str(data)}")

#append list
topic.append("Blood")
print(topic[:6])

#extend list
new_topic = ["Name", "Roll", "Email", "Phone", "Address"]
topic.extend(topic.extend(new_topic))
print(new_topic)

#short list
print(topic.sort())

#copy list
cpList = topic.copy()
print(cpList)

#join list
join_list = topic+new_topic
print(join_list)

