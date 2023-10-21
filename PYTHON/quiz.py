import random
Questions_list=['What is the capital of the United States of America? ',
'Who is the current president of the United States of America? ',
'What is the capital of Nigeria? ',
'Muhammadu Buhari is the president of which country? ',
'Uhuru Kenyatta is the president of which country? ',
'What is the capital of France? ',
'Which state has only one neighbor? ',
'Where is Amsterdam located? ',
'Emmanuel Macron is the president of which country? ',
'Sir Alex Ferguson until his retirement coached which team?']
Answers=[ 'Washington DC','President Donald Trump','Abuja','Nigeri','Kenya','Paris','Maine','Netherland','France','Manchester United']
dic={'What is the capital of the United States of America? ':'Washington DC','Who is the current president of the United States of America? ':'President Donald Trump','What is the capital of Nigeria? ':'Abuja','Muhammadu Buhari is the president of which country? ':'Nigeri','Uhuru Kenyatta is the president of which country? ':'Kenya',
'What is the capital of France? ':'Paris',
'Which state has only one neighbor? ':'Maine',
'Where is Amsterdam located? ':'Netherland',
'Emmanuel Macron is the president of which country? ':'France',
'Sir Alex Ferguson until his retirement coached which team?':'Manchester United'}

num_right= 0
s = random.sample(Questions_list, 4)

for i in range(4):
    answer= input(s[i])

    correct_Answer=str(dic[s[i]])
    
    if answer.lower()==correct_Answer.lower():
        print('Correct!!!')
        num_right+=1
    else:
        print('Not correct') 
print(f"Your score is {num_right}")
      
   

