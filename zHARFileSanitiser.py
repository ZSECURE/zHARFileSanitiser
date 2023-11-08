#!/usr/bin/python3

import json
import os
import argparse

def load_cookie_names(file_path):
    with open(file_path, 'r') as f:
        return [line.strip() for line in f]

def remove_session_cookies(har_file_path, session_cookie_names):
    # Load the .har file
    with open(har_file_path, 'r') as f:
        data = json.load(f)

    # Iterate over the entries
    for entry in data['log']['entries']:
        # Remove the session cookies from the request
        new_cookies = []
        for cookie in entry['request']['cookies']:
            if cookie['name'] not in session_cookie_names:
                new_cookies.append(cookie)
            else:
                print(f"Removed cookie: {cookie['name']} = {cookie['value']}")
        entry['request']['cookies'] = new_cookies

        # Remove the session cookies from the headers
        new_headers = []
        for header in entry['request']['headers']:
            if header['name'].lower() != 'cookie' or not any(name in header['value'] for name in session_cookie_names):
                new_headers.append(header)
            else:
                print(f"Removed cookie from headers: {header['name']} = {header['value']}")
        entry['request']['headers'] = new_headers

        # Remove the session cookies from the response
        new_cookies = []
        for cookie in entry['response']['cookies']:
            if cookie['name'] not in session_cookie_names:
                new_cookies.append(cookie)
            else:
                print(f"Removed cookie from response: {cookie['name']} = {cookie['value']}")
        entry['response']['cookies'] = new_cookies

        # Remove the session cookies from the response headers
        new_headers = []
        for header in entry['response']['headers']:
            if header['name'].lower() != 'set-cookie' or not any(name in header['value'].split('=')[0] for name in session_cookie_names):
                new_headers.append(header)
            else:
                print(f"Removed cookie from response headers: {header['name']} = {header['value']}")
        entry['response']['headers'] = new_headers

    # Save the .har file without the session cookies
    new_file_path = os.path.splitext(har_file_path)[0] + '_no_session_cookies.har'
    with open(new_file_path, 'w') as f:
        json.dump(data, f)

    print(f'File saved as {new_file_path}')

# Parse command-line arguments
parser = argparse.ArgumentParser(description='Remove session cookies from a .har file.')
parser.add_argument('har_file_path', help='The path to the .har file.')
parser.add_argument('-c', '--cookies', help='A list of names of the session cookies to remove, separated by commas.')
parser.add_argument('-f', '--file', help='A file with a list of names of the session cookies to remove, one per line.')
args = parser.parse_args()

# Load the session cookie names
if args.cookies:
    session_cookie_names = args.cookies.split(',')
elif args.file:
    session_cookie_names = load_cookie_names(args.file)
else:
    raise ValueError('You must provide either a list of cookie names or a file with cookie names.')

# Use the function with the command-line arguments
remove_session_cookies(args.har_file_path, session_cookie_names)
