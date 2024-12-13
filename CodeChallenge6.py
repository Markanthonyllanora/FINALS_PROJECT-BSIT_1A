def cc6():

    prelim = eval(input("Grade in prelim: "))
    midterm = eval(input("Grade in midterm: "))
    semifinals = eval(input("Grade in semi final: "))
    finals = eval(input("Grade in finals: "))
    quizzes = eval(input("Grade in quuzzes: "))
    project = eval(input("Grade in project: "))

    if (prelim >= 65 and prelim <= 100) and (midterm >= 65 and midterm <= 100) and (semifinals >= 65 and semifinals <= 100) and (finals >= 65 and finals <= 100) and (quizzes >= 65 and quizzes <= 100) and (project >= 65 and project <= 100):
        grades = (prelim * .15) + (midterm * .15) + (semifinals * .15) + (finals * .15) + (quizzes * .25) + (project * .15)
        
        if grades >= 75:
            print(f"Congratulations,You have passed the subject, Your  grade is {grades}")
        else:
            print(f"Sorry,you failed. Your grade is {grades}")                
    else: 
        print("Invalid Grade")


cc6()
  