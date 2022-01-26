#! python3
# Email.py  Finds email addresses on the clipboard
import pyperclip, re
# Create email regex.
emailRegex = re.compile(r'''(
        [a-zA-Z0-9._%+-]+   #   username
        @                   #   @ symbol
        [a-zA-Z0-9.-]+      #   domain name
        (\.[a-zA-Z]{2,4})   #   dot-somethine
        )''', re.VERBOSE)
# Find matches in clipboard text.
text = str(pyperclip.paste())
matches = []
for groups in emailRegex.findall(text):
    matches.append(groups[0])   # 将每次匹配的分组0添加到matches列表中。
# Copy results to the clipboard.
if len(matches) > 0:
    pyperclip.copy('\n'.join(matches))
    print('Copied to clipboard:')
    print('\n'.join(matches))
else:
    print('No email addresses found.')

