print("Beautiful Soup")

from bs4 import BeautifulSoup

# #basic scraping
# with open('home.html', 'r') as fail_html:
#     kandungan = fail_html.read()
#     # print(kandungan)

#     sup = BeautifulSoup(kandungan, 'lxml')
#     # print(sup.prettify)
#     tags_courses = sup.find_all('h5')
#     # print(tags_courses)
#     for course in tags_courses:
#         print(course.text)

#scrap price from website
with open("home.html", 'r') as fail_html:
    kandungan = fail_html.read()

    sup = BeautifulSoup(kandungan, 'lxml')
    course_cards = sup.find_all('div', class_='card')
    for course in course_cards:
        course_name = course.h5.text
        course_price = course.a.text.split()[-1]

        # print(course_name)
        # print(course_price)
        print(f'{course_name} costs {course_price}')
