from selenium import webdriver

browser = webdriver.PhantomJS('/usr/local/bin/phantomjs')
browser.set_window_size(1120, 550)

# go to home page
browser.get('http://localhost:8000')
assert 'Home Page' in  browser.title

# see category link Amsterdam In The 1950s

link = browser.find_element_by_link_text('Amsterdam In The 1950s').text
assert 'Amsterdam In The 1950s' == link

# click category and go to the category list page
browser.get('http://localhost:8000/category/amsterdam-in-the-50s/')
assert 'http://localhost:8000/category/amsterdam-in-the-50s/' == browser.current_url

header = browser.find_element_by_tag_name('h1').text
assert 'Amsterdam In The 1950s' == header

# click on a image
image = browser.find_element_by_tag_name('img')
assert 'http://localhost:8000/images/upload/4904712826.jpg' == image.get_attribute("src")

# image link goes to the detail image page

browser.quit()
print('completed tests.')









