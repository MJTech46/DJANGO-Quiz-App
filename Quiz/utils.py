import requests
from Quiz.models import Quiz, Option
from django.db.utils import IntegrityError
from time import sleep

def add_data(amount: int, difficulty: str, category: int, category_text: str) -> None:
    """
    amount = 1 to 50
    difficulty = [
        "easy", "medium", "hard"
    ]
    category = check the api site (https://opentdb.com/api_config.php)
    """
    counter=0
    print("\n****Task started****")
    # The API endpoint
    url = f"https://opentdb.com/api.php?amount={amount}&category={category}&difficulty={difficulty}&type=multiple"
    # A GET request to the API
    response = requests.get(url)
    #converting to json format
    response_json = response.json()
    #some times the api will return no data
    try:
        results_list = response_json["results"]
    except KeyError:
        print("Please Retry")
        #for a deliberate delay
        sleep(5.00) 
        return None
    #if the get() was success
    for result in results_list:
        #gethering the data
        difficulty=result["difficulty"]
        question=result["question"]
        options= [result["correct_answer"]]+result["incorrect_answers"]
        #there is a high possibility to send existing datas by the api
        try:
            #creating quiz
            quiz=Quiz(
                question_text=question,
                difficulty=difficulty,
            )
            quiz.save()
            counter+=1
        #if existing data
        except IntegrityError as e:
            if "UNIQUE constraint failed".lower() in str(e).lower():
                print("Skiped...")
                continue
            else:
                raise e
        #creating options
        for i,option_txt in enumerate(options):
            is_correct=False
            if i == 0:
                is_correct=True
            option=Option(
                quiz=quiz,
                option_text=option_txt,
                is_correct=is_correct
            )
            option.save()
    print(f"****{counter} datas added to the db****")
    #for a deliberate delay
    sleep(5.00)