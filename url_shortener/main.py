import random
import string
import time
import bleach
import validators

url_mapping = {}


def generate_alias(length=6):
    while True:
        # define characters for alias
        characters = string.ascii_letters + string.digits
        # generate a random string of characters with a generator expression
        alias = ''.join(random.choice(characters) for _ in range(length))

        if alias not in url_mapping:
            return alias
        
def shorten_url(url):
    try:
        alias = generate_alias()
        url_mapping[alias] = users_url
        return alias
    except Exception as e:
        print(f'Error occurred while generating shortened URL: {e}')

# (rate limiting, restricting number of requests a user can make 
# within a specified time frame)
# dictionary to store request counts for each user/IP
request_counts = {}
def check_rate_limit(used_id):
    # check if user_id is preset in request_counts dictionary
    if user_id in request_counts:
        # get the timestamp of the last request
        last_request_time = request_counts[user_id]
        # calculate the time difference since the last request
        time_difference = time.time() - last_request_time
        # if the time difference is less than the allowed time frame
        # deny the request
        if time_difference < 60:
            return False
    # update the request timestamp for the user
    request_counts[user_id] = time.time()
    return True

# example usage of rate limit
user_id = 'example_user'
if(check_rate_limit(user_id)):
    print("Request allowed.")
    # ...
else:
     print("Rate limit exceeded. Please try again later.")


# Sanitization of the user's input
def sanitize_input(input_text):
    # define allowed HTML tags and attributes
    allowed_tags = ['a', 'abbr', 'acronym', 'b', 
                    'blockquote', 'code', 'em', 'li', 'ol', 'strong', 'ul']
    allowed_attributes = {'a': ['href', 'title'], 'abbr': ['title']}
    # sanitize the input text
    sanitized_text = bleach.clean(input_text, tags=allowed_tags, 
                                  attributes=allowed_attributes)
    
# example usage of sanitized user's input
user_input = '<script>alert("XSS attack");</script>'
sanitized_input = sanitize_input(user_input)
print("Sanitized input:", sanitized_input) # will return "None"

users_url = input("Paste a link URL you want to shorten: ")
if not validators.url(users_url):
    print("Please paste a valid link.")
else:
    alias = shorten_url(users_url)
    print(f'Your shortened URL is: https://{alias}.com')
    print('----------------------')
    print(f'Your long URL is: {url_mapping.get(alias)}')