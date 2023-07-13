import csv

file_path = "election_data.csv"

total_number_vote = 0
list_candidates = []
number_vote = {}
percentage_vote = {}

with open(file_path, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    next(csvreader)

    for row in csvreader:
        total_number_vote += 1
        current_candidate = row[2]

        if current_candidate not in list_candidates:
            list_candidates.append(current_candidate)
            number_vote[current_candidate] = 1
        else:
            number_vote[current_candidate] += 1

    for candidate in list_candidates:
        vote = number_vote[candidate]
        percentage = (vote / total_number_vote) * 100
        percentage_vote[candidate] = percentage

print("Election Results")
print("-------------------------")
print(f"Total Votes: {total_number_vote}")
print("-------------------------")

for candidate in list_candidates:
    votes = number_vote[candidate]
    percentage = percentage_vote[candidate]
    print(f"{candidate}: {percentage:.3f}% ({votes})")

print("-------------------------")

winner = max(number_vote, key=number_vote.get)
print(f"Winner: {winner}")

print("-------------------------")
