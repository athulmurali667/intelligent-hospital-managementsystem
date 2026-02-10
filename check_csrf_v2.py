import urllib.request
import http.cookiejar
import re

cookie_jar = http.cookiejar.CookieJar()
opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cookie_jar))

try:
    response = opener.open('http://127.0.0.1:8000/admin/login/')
    content = response.read().decode('utf-8')
    
    print(f"Status Code: {response.getcode()}")
    print("--- Headers ---")
    for header, value in response.headers.items():
        print(f"{header}: {value}")
    print("----------------")
    
    if 'csrfmiddlewaretoken' in content:
        print("CSRF Token found in HTML form (hidden input).")
        match = re.search(r'name="csrfmiddlewaretoken" value="(.*?)"', content)
        if match:
            print(f"Token value in HTML: {match.group(1)}")
    else:
        print("CSRF Token NOT found in HTML.")

    print("--- Cookies ---")
    found_cookie = False
    for cookie in cookie_jar:
        print(f"{cookie.name}: {cookie.value}")
        if cookie.name == 'csrftoken':
            found_cookie = True
            
    if not found_cookie:
        print("CSRF cookie MISSING from jar.")
        
except Exception as e:
    print(f"Error: {e}")
