import urllib.request
import urllib.parse
import http.cookiejar
import re

# Setup cookie jar
cookie_jar = http.cookiejar.CookieJar()
opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cookie_jar))

login_url = 'http://127.0.0.1:8000/login_post'
admin_page_url = 'http://127.0.0.1:8000/admin/login/'

try:
    # 1. Get the login page to get the CSRF token
    response = opener.open(admin_page_url)
    content = response.read().decode('utf-8')
    
    csrf_token = None
    # Extract token from HTML
    match = re.search(r'name="csrfmiddlewaretoken" value="(.*?)"', content)
    if match:
        csrf_token = match.group(1)
        print(f"CSRF Token found: {csrf_token}")
    else:
        print("CSRF Token NOT found in HTML")
        exit(1)

    # 2. Prepare POST data
    data = urllib.parse.urlencode({
        'username': 'admin',
        'password': 'admin',
        'csrfmiddlewaretoken': csrf_token,
        'Submit': 'Login'
    }).encode('utf-8')

    # 3. Perform Login
    request = urllib.request.Request(login_url, data=data)
    # Add Referer header as Django CSRF middleware might check it
    request.add_header('Referer', admin_page_url)
    
    response = opener.open(request)
    response_content = response.read().decode('utf-8')
    
    print(f"Login Response Code: {response.getcode()}")
    print("Login Response Content:")
    print(response_content)
    
    if 'window.location="/adminhome"' in response_content:
        print("LOGIN SUCCESSFUL!")
    else:
        print("LOGIN FAILED or Unexpected Response.")

except Exception as e:
    print(f"Error: {e}")
