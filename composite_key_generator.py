import random 
import csv

num_history = 3000
history = set()

while len(history) < num_history:
    show_id = random.randint(5181, 7180)
    user_id = random.randint(1, 1000)
    composite_key = (show_id, user_id)
    if composite_key not in history: 
        history.add(composite_key)

formatted_history = [{"show_id": show_id, "user_id": user_id} for show_id, user_id in history]

with open(f"ID.csv", mode="w") as file:
    writer = csv.DictWriter(file, fieldnames=['show_id', 'user_id'])
    writer.writeheader()
    writer.writerows(formatted_history)
