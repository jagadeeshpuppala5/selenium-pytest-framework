def test_launch(driver):
    driver.get("https://www.saucedemo.com/")
    assert "Swag Labs" in driver.title
