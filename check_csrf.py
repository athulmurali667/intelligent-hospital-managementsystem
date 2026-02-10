import urllib.request
import http.cookiejar

cookie_jar = http.cookiejar.CookieJar()
opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cookie_jar))

try:
    response = opener.open('http://127.0.0.1:8000/admin/login/')
    print(f"Status Code: {response.getcode()}")
    
    csrf_token = None
    for cookie in cookie_jar:
        if cookie.name == 'csrftoken':
            csrf_token = cookie.value
            break
            
    if csrf_token:
        print("CSRF cookie is present.")
        print(f"Cookie value: {csrf_token}")
    else:
        print("CSRF cookie is MISSING.")
        print("Cookies in jar:", [c.name for c in cookie_jar])
        
except Exception as e:
    print(f"Error: {e}")
