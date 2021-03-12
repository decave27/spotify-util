import asyncio, json, requests


with requests.Session() as (c):
    url = 'https://accounts.spotify.com/en/login?continue=https:%2F%2Fwww.spotify.com%2Fint%2Faccount%2Foverview%2F'
    headers = {'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',  'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'}
    page = c.get(url, headers=headers)
    CSRF = page.cookies['csrf_token']
    headers = {'Accept':'*/*',  'User-Agent':'Mozilla/5.0 (iPhone; CPU iPhone OS 10_0_1 like Mac OS X) AppleWebKit/602.1.50 (KHTML, like Gecko) Version/10.0 Mobile/14A403 Safari/602.1',  'Referer':'https://accounts.spotify.com/en/login/?continue=https:%2F%2Fwww.spotify.com%2Fus%2Fgooglehome%2Fregister%2F&_locale=en-US'}
    url = 'https://accounts.spotify.com/api/login'
    login_data = {'remember':'true',  'username': 'masteruser',  'password':'masterpwd',  'csrf_token':CSRF}
    cookies = dict(__bon='MHwwfC0xNDAxNTMwNDkzfC01ODg2NDI4MDcwNnwxfDF8MXwx')
    login = c.post(url, headers=headers, data=login_data, cookies=cookies)
    if '{"displayName":"' in login.text:
        url = 'https://www.spotify.com/us/account/overview/'
        capture = c.get(url, headers=headers)
        csr = capture.headers['X-Csrf-Token']
        url = 'https://www.spotify.com/us/family/api/master-invite-by-email/'
        headers = {'Accept':'*/*',  'User-Agent':'Mozilla/5.0 (iPhone; CPU iPhone OS 10_0_1 like Mac OS X) AppleWebKit/602.1.50 (KHTML, like Gecko) Version/10.0 Mobile/14A403 Safari/602.1',  'x-csrf-token':csr}
        login_data = {'firstName':'name1',  'lastName':'name2',  'email': 'email'}
        invite = c.post(url, headers=headers, json=login_data)
        print(invite.text)
