import requests

# r = requests.get('https://xkcd.com/')
r = requests.get('https://imgs.xkcd.com/comics/iso_paper_size_golden_spiral.png')


# print(dir(r))
# print(r.text)

# with open('image.png', 'wb') as f:
#     f.write(r.content)

print(r.status_code)
