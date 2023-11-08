# HAR File Session Cookie Remover

This Python script removes specified session cookies from a HAR (HTTP Archive) file.

## Requirements

- Python 3.6 or later

## Usage

Run the script with the path to the .har file and either a list of session cookie names or a file with session cookie names:

```bash
python zHARFileSanitiser.py /path/to/your_file.har -c SESSIONID,OTHERCOOKIE
```
or
```
python zHARFileSanitiser.py /path/to/your_file.har -f cookies.txt
```

The script will:

- Remove the specified session cookies from the 'request' and 'response' objects in the .har file.
- Print the removed cookies to the console.
- Save the .har file without the session cookies under a new name with the suffix '_no_session_cookies'.

##  Command-Line Arguments
- `har_file_path`: The path to the .har file. This argument is mandatory.
- `-c, --cookies`: A list of names of the session cookies to remove, separated by commas.
- `-f, --file`: A file with a list of names of the session cookies to remove, one per line.
You must provide either `-c` or `-f`.

## Example
To remove the session cookies 'SESSIONID' and 'OTHERCOOKIE' from the file 'your_file.har', you can use:
```
python remove_session_cookies.py your_file.har -c SESSIONID,OTHERCOOKIE
```
This will create a new file 'your_file_no_session_cookies.har' without the specified session cookies.
