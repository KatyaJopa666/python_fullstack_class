def choose_ad_platform(budget: int) -> str:
    if budget > 5000:
        print('Instagram')
    elif budget >= 1000:
        print('Facebook')
    else:
        print('Google')

choose_ad_platform(500)
choose_ad_platform(3000)
choose_ad_platform(6000)