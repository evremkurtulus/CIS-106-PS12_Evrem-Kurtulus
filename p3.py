def display_highest_lowest(names, scores):
    high_var = 0
    high_index = 0
    low_var = 999
    low_index = 0
    for i in range(len(scores)):
        if scores[i] > high_var:
            high_var = scores[i]
            high_index = i
        if scores[i] < low_var:
            low_var = scores[i]
            low_index = i
    print(f"Highest score: {names[high_index]} - {scores[high_index]}")
    print(f"Lowest score: {names[low_index]} - {scores[low_index]}")

with open('data.txt', 'r') as f:
    last_names = []
    exam_scores = []
    for line in f:
        data = line.strip().split()
        last_names.append(data[0])
        exam_scores.append(int(data[1]) + int(data[2]))

display_highest_lowest(last_names, exam_scores)