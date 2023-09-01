#Find Highest to lowest Grade Level and Store in Data:

if __name_ == '__main__':
    n=input("Etner Name: ")
    student_scores=[]

    for _ in range(n):
        name=input("Enter a Name: ")
        score=float(input("Enter a Score: "))
        student_scores.append([name,score])

    #Sort the Nested list based on the scores

    student_scores.sort(key=lambda x:x[1])