import csv

file_path = "budget_data.csv"

total_months = 0
net_total = 0
previous_profit_loss = 0
total_changes = 0
greatest_increase = 0
greatest_decrease = 0
greatest_increase_date = ""
greatest_decrease_date = ""

with open(file_path, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    next(csvreader)  

 
    for row in csvreader:
        total_months += 1
        current_profit_loss = int(row[1])
        net_total += current_profit_loss

        if total_months > 1:
            change = current_profit_loss - previous_profit_loss
            total_changes += change

            if change > greatest_increase:
                greatest_increase = change
                greatest_increase_date = row[0]

            if change < greatest_decrease:
                greatest_decrease = change
                greatest_decrease_date = row[0]

        previous_profit_loss = current_profit_loss


average_change = total_changes / (total_months - 1)


print("Financial Analysis")
print("-----------------------------")
print(f"Total Months: {total_months}")
print(f"Net Total: ${net_total}")
print(f"Average Change: ${average_change:.2f}")
print(f"Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase})")
print(f"Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease})")
