from selenium import webdriver

browser = webdriver.PhantomJS('/usr/local/bin/phantomjs')
browser.set_window_size(1120, 550)

# go to home page
browser.get('http://localhost:8000/backend/')
assert '' in  browser.title

# should see sign in link
link = browser.find_element_by_link_text('Sign In').text
assert 'Sign In' == link

# sign in with sign in link


# once signed in should see sign out link

browser.quit()
print('completed tests.')