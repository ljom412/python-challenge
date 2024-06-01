import os
import csv

election_data = os.path.join("PyPoll/Resources/election_data.csv")

# open the csv file
with open(election_data) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    csv_header = next(csv_file)
    print(f"Header: {csv_header}")

    # get total vote count
    data = list(csv_reader) 
    row_count = len(data)
    print(row_count)    

    # get a complete list of candidates who received votes
    tally = []
    candidates = []

    for x in range (0, row_count):
        candidate = data[x][2]
        tally.append(candidate)
        if candidate not in candidates:
            candidates.append(candidate)
        candidate_count = len(candidates)
    
    # get total number of votes and the percentage for each candidate
    votes = []
    percentage = []
    for i in range(0, candidate_count):
        name = candidates[i]
        votes.append(tally.count(name))
        vote_pct = votes[i]/row_count
        percentage.append(vote_pct)
    print(percentage)
    print(votes)

    # get winner based on votes
    winner = votes.index(max(votes))

    # print analysis to the terminal
    print('Election Results')
    print('.............................................')
    print(f'Total Votes: {row_count}')
    print('.............................................')
    for j in range(0, candidate_count):
        print(f'{candidates[j]}: {percentage[j]: .3%} ({votes[j]:,})')
    print('.............................................')
    print(f'Winner: {candidates[winner]}')
    print('.............................................')
    
    #print analysis to a text file
    print('Election Results', file=open('PyPoll/Analysis/PyPoll.txt', 'a'))
    print('.............................................', file=open('PyPoll/Analysis/PyPoll.txt', 'a'))
    print(f'Total Votes: {row_count}', file=open('PyPoll/Analysis/PyPoll.txt', 'a'))
    print('.............................................', file=open('PyPoll/Analysis/PyPoll.txt', 'a'))
    for j in range(0, candidate_count):
        print(f'{candidates[j]}: {percentage[j]: .3%} ({votes[j]:,})', file=open('PyPoll/Analysis/PyPoll.txt', 'a'))
    print('.............................................', file=open('PyPoll/Analysis/PyPoll.txt', 'a'))
    print(f'Winner: {candidates[winner]}', file=open('PyPoll/Analysis/PyPoll.txt', 'a'))
    print('.............................................', file=open('PyPoll/Analysis/PyPoll.txt', 'a'))
