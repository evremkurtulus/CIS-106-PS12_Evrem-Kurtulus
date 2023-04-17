last_names = ['Kurtulus', 'Tytyla', 'Jackson', 'Moore', 'Stevens', 'Tierney', 'Jones', 'Musk', 'Jordan', 'Sal']
exam_scores = [85, 70, 92, 78, 81, 65, 90, 98, 87, 79]

def display_names_and_scores(names, scores):
    for i in range(len(names)):
        print(f"{names[i]} - {scores[i]}")

def display_names_and_scores_reverse(names, scores):
    for i in range(len(names)-1, -1, -1):
        print(f"{names[i]} - {scores[i]}")

display_names_and_scores(last_names, exam_scores)
print("---------------")
display_names_and_scores_reverse(last_names, exam_scores)

