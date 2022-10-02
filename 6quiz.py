# a dictonary that stores questions and answers
# have a variable that tracks the score of the player 
# loop through the dictionary using the key-value pairs
# display each question to the user and allow them to answer
# tell them  right or wrong 
# show the final result when quiz is completed

quiz={
    "question1": {
        "question":"what is capital of France" ,
        "answer":"Paris" 
    },
    "question2":{
        "question":"what is capital of Germany",
        "answer":"Berlin"
    },
    "question3":{
        "question":"what is capital of Italy",
        "answer":"Rome"
    },
    "question4":{
        "question":"what is capital of Spain",
        "answer":"Madrid"
    },
    "question5":{
        "question":"what is capital of Portugal",
        "answer":"Lisbon"
    },
    "question6":{
        "question":"what is capital of Switzerland",
        "answer":"Bern"
    },
    "question7":{
        "question":"what is capital of Austria",
        "answer":"Vienna"
    },

}

score=0
for key,value in quiz.items():
    print(value["question"]) #key
    answer=input("Answer?")

    if answer.lower()==value["answer"].lower():
        print("correct")
        score=score+1
        print("Your score is "+str(score))
        print("")
        print("")

    else:
        print("Wrong")
        print("The answer is : " +value["answer"])
        print("Your score is "+str(score))
        print("")
        print("")
print("Your final  score is "+str(score) )
print("Your percentage is "+str(score/7*100) + "%")  # since we designed 7 key-value pair dict