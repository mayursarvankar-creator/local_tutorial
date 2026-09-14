from asyncio import wait

from pages.login_page import LoginPage
from playwright.sync_api import expect
from dotenv import load_dotenv
import os
load_dotenv()


def test_login_page_loads(page, app_url):
    login_page = LoginPage(page)
    login_page.open(app_url)
    login_page.login(os.getenv("TEST_EMAIL"), os.getenv("TEST_PASSWORD"))

    page.wait_for_load_state("networkidle")

    expect(page).to_have_title("My Account")