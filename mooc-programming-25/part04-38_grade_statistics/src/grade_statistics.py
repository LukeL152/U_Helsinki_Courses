# Write your solution here:
exam_scores = []
pass_fail = []
final_scores = []


def mean(integers):
    average = sum(integers) / len(integers)
    return average


while True:
    raw_scores = input("Exam points and exercises completed: ")
    if raw_scores == "":
        break
    space = raw_scores.index(" ")
    exam = int(raw_scores[:space])
    excercise = int(raw_scores[space + 1 :])
    excercise_final = int((excercise / 100) * 10)
    final_score = exam + excercise_final
    exam_scores.append(exam)
    final_scores.append(final_score)

i = 0
while i < len(exam_scores):
    if exam_scores[i] < 10:
        pass_fail.append("Fail")
    elif final_scores[i] < 15:
        pass_fail.append("Fail")
    else:
        pass_fail.append("Pass")
    i += 1

final_converted = []
for i in final_scores:
    if i < 15:
        final_converted.append(0)
    elif i >= 15 and i < 18:
        final_converted.append(1)
    elif i >= 18 and i < 21:
        final_converted.append(2)
    elif i >= 21 and i < 24:
        final_converted.append(3)
    elif i >= 24 and i < 28:
        final_converted.append(4)
    elif i >= 28 and i <= 30:
        final_converted.append(5)

i = 0
while i < len(final_converted):
    if pass_fail[i] == "Fail":
        final_converted[i] = 0
    i += 1


points_avg = mean(final_scores)
pass_percent = (pass_fail.count("Pass") / len(pass_fail)) * 100

print("Statistics:")
print(f"Points average: {points_avg:.1f}")
print(f"Pass percentage: {pass_percent:.1f}")
print("Grade distribution:")

grades = [5, 4, 3, 2, 1, 0]
for i in grades:
    print(f"  {i}: {'*' * final_converted.count(i)}")
