from playwright.sync_api import Page, expect

def test_wiki2(page:Page):
    page.goto('https://www.wikipedia.org/')
    page.get_by_role('link', name='English').click()
    expect(page.get_by_text('From today\'s featured article')).to_be_visible()
    page.get_by_role('link', name='Talk').click()
    expect(page.locator('#talkheader')).to_contain_text('Welcome! This page is for discussing the contents of the English Wikipedia\'s Main Page.')
