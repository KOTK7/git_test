from survey import AnonymousSurvey

#* Define a question , and make a survey *# 
question = "what language did you learn first to speak"
language_survey = AnonymousSurvey(question)
#* Show the question, and store responses to the question*#
language_survey.show_question()
print("Enter 'q' to quit anytime\n")
while True:
    response = input("Language: ")
    if response == "q":
        break
    language_survey.store_response(response)
#* show the survey results *#
print("Thank you to everyone who participated in the survey")
language_survey.show_result()