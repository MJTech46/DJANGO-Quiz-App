from .models import Reward

def create_default_rewards_onces():
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
