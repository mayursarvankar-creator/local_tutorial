from pages.login_page import LoginPage


def test_login_page_loads(page, app_url):
    login_page = LoginPage(page)
    login_page.open(app_url)

    assert page.url.startswith(app_url)
