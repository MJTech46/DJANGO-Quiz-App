from .models import Reward, Quiz, Option

def create_default_rewards_once():
    """ This function adding demo rewards for once """
    Reward.objects.get_or_create(
        reward_name = "Roblox card",
        reward_value = 500,
        reward_points_required = 5000,
        reward_image = "/static/Quiz/img/redeem/000400000343_v3_262x164.png"
    )
    Reward.objects.get_or_create(
        reward_name = "Amazon Gift card",
        reward_value = 500,
        reward_points_required = 5000,
        reward_image = "/static/Quiz/img/redeem/AmazonPayIN_262x164.png"
    )
    Reward.objects.get_or_create(
        reward_name = "Bookmyshow",
        reward_value = 500,
        reward_points_required = 5000,
        reward_image = "/static/Quiz/img/redeem/BookMyShow_262x164.png"
    )
    Reward.objects.get_or_create(
        reward_name = "Flipkart Gift card",
        reward_value = 500,
        reward_points_required = 5000,
        reward_image = "/static/Quiz/img/redeem/Flipkart_262x164.png"
    )
    Reward.objects.get_or_create(
        reward_name = "Spotify Premium",
        reward_value = 60,
        reward_points_required = 5000,
        reward_image = "/static/Quiz/img/redeem/Spotify_3M_rerun_262x164.png"
    )

def create_default_quizzes_once():
    """ This function adding demo quizzes for once """

    # quiz1 #
    q, _ =  Quiz.objects.get_or_create(
                question_text = "In Python, which method is used to write text to a file?"
            )
    Option.objects.get_or_create(
        quiz = q,
        option_text = "write()",
        is_correct = True
    )
    Option.objects.get_or_create(
        quiz = q,
        option_text = "writing()",
        is_correct = False
    )
    Option.objects.get_or_create(
        quiz = q,
        option_text = "print()",
        is_correct = False
    )
    Option.objects.get_or_create(
        quiz = q,
        option_text = "read()",
        is_correct = False
    )

    # quiz2 #
    q, _ =  Quiz.objects.get_or_create(
                question_text = "In Python, what operator is used to check if two values are equal?"
            )
    Option.objects.get_or_create(
        quiz = q,
        option_text = "==",
        is_correct = True
    )
    Option.objects.get_or_create(
        quiz = q,
        option_text = "===",
        is_correct = False
    )
    Option.objects.get_or_create(
        quiz = q,
        option_text = "!=",
        is_correct = False
    )
    Option.objects.get_or_create(
        quiz = q,
        option_text = "=",
        is_correct = False
    )
