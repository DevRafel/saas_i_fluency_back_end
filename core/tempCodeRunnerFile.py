import instaloader


profile_name = 'stherzada'

dp = instaloader.Instaloader()

dp.download_profile(profile_name, profile_pic_only=True)