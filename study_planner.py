import json

topics = []

n = int(input("Enter number of topics: "))

for i in range(n):
    name = input("Enter topic name: ")
    importance = input("Importance (high/medium/low): ").lower()

    topics.append({"name": name, "importance": importance})

# Sort by importance
priority = {"high": 3, "medium": 2, "low": 1}
topics.sort(key=lambda x: priority[x["importance"]], reverse=True)

print("\n📅 Study Plan:\n")

day = 1
for topic in topics:
    if topic["importance"] == "high":
        hours = 2
    elif topic["importance"] == "medium":
        hours = 1
    else:
        hours = 0.5

    print(f"Day {day}: {topic['name']} - {hours} hrs")
    day += 1

    print("\n✅ Mark Progress:\n")

for topic in topics:
    status = input(f"Did you complete '{topic['name']}'? (yes/no): ")
    topic["status"] = status

print("\n📊 Progress Report:\n")

for topic in topics:
    print(f"{topic['name']} - {topic['status']}")

with open("study_data.json", "w") as f:
    json.dump(topics, f)

print("\nData saved!")