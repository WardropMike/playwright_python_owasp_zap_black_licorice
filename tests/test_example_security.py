def test_example(browser):
    page = browser.new_page()
    page.goto("http://example.com")  # Test site
    assert "Example" in page.title()
