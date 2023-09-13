import browser
import tiktok


tt_url = 'https://www.tiktok.com/'

user_browser = input('Digite o nome do navegador: ')
user_name = input('Digite o usuário do TikTok para login: ')
user_password = input('Digite a senha do TikTok para login: ')
tt_creator = input('Digite o criador TikTok que deseja curtir: (com @) ')
likes = input('Digite a quantidade de vídeos para curtir: ')

browser.open_browser(user_browser)

browser.open_tiktok(tt_url)

tiktok.login_tiktok(user_name, user_password)

# tiktok.search_creator(tt_url, tt_creator)

# tiktok.search_first_video()

# tiktok.like_videos(likes)
