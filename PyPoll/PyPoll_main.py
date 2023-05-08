# Import Modules
import csv

# Set Path
election_data = r"C:\Users\Owner\Documents\Data Boot Camp\Challenge_3\Python-Challenge\PyPoll\Resources\election_data.csv"

# Read data and set lists/variables
with open(election_data, 'r') as csvfile:
    candidates_list = []
    votes_list = []
    total_votes = 0
    c1_list = []
    c2_list = []
    c3_list = []
    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')
    next(csvreader)

    #set for loop to append list and calulate total votes casted
    for row in csvreader:
        total_votes += 1
        candidates_list.append(str(row[2]))
    candidates_list = sorted(candidates_list)

    # Set for loop  to create lists and then calculate total vote counts per candidate
    for i in range(len(candidates_list)):
         if str(candidates_list[i-1]) == 'Charles Casper Stockham':
              c1_list.append(candidates_list[i])
         elif str(candidates_list[i-1])  == 'Diana DeGette':
              c2_list.append(candidates_list[i])
         elif str(candidates_list[i-1]) == 'Raymon Anthony Doane':
              c3_list.append(candidates_list[i]) 
    candidates = ['Charles Casper Stockham', 'Diana DeGette', 'Raymon Anthony Doane']
    c1_count = len(c1_list)
    c2_count = len(c2_list)
    c3_count = len(c3_list)
    vc_list = [c1_count,c2_count,c3_count]
    max_vote = max(vc_list)
    max_index = vc_list.index(max_vote)
    winner = candidates[max_index]
  
# Print results using for loop to help calculate percent and print each candidate result            
    print(f'Election Results')
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
    print (f'Total Votes: {total_votes}')
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
    for i in range(len(candidates)):
        v_percent = (vc_list[i]/total_votes)*100
        print (f'{candidates[i]}: {round(v_percent,3)}% ({vc_list[i]})')
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
    print(f'Winner: {winner}')
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')