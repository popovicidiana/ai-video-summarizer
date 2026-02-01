import re

def extract_video_id(input_string):
    # Check if input_string is a URL
    if re.match(r'http(s)?:\/\/', input_string):
        #Check if it is a Youtube URL
        if 'youtube.com' in input_string:
            match = re.search(r'v=([^&]*)', input_string)
            if match:
                return match.group(1)
            
        elif 'youtu.be' in input_string:
            match = re.search(r'youtu\.be/([^&]*)', input_string)
            if match:
                return match.group(1)
            
    # If input_string is not a URL, assume it's a video ID
    return input_string
