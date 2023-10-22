from bs4 import BeautifulSoup as soup
from urllib.request import Request, urlopen

# define the matrix which stores episode and category information
category_matrix = np.asarray([["Category", "Episode"]])


# define function which stores each episode and category information into the matrix


def save_matrix(category):
    url_category = 'https://jrelibrary.com/guests/' + category
    req_category = Request(url_category, headers={'User-Agent': 'Mozilla/5.0'})
    page_html_category = urlopen(req_category).read()
    page_soup_category = soup(page_html_category, 'html.parser')
    global category_matrix
    for person_name_link in page_soup_category.find_all('div', {'class': 'entry'}):
        for person_name in person_name_link.find_all('p'):
            i = np.asarray([[category, person_name.string]])
            category_matrix = np.append(category_matrix, i, axis=0)


# Webscrapping all category information and their respective link in JRE page
# and call out function to save these information in the matrix
my_url = 'https://jrelibrary.com/guests/'
req = Request(my_url, headers={'User-Agent': 'Mozilla/5.0'})
page_html = urlopen(req).read()
page_soup = soup(page_html, 'html.parser')
for ultag in page_soup.find_all('ul', {'class': 'table-of-contents'}):
    for litag in ultag.find_all('li'):
        for link in litag.find_all('a'):
            category = link.get('href')[8:]
            print(category)
            save_matrix(category)

# Save the matrix into a csv file
np.savetxt("JRE_Category.csv", category_matrix, delimiter=",", fmt='%s')
