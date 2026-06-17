import os
from datetime import datetime

def capture_screenshot(driver, test_name):

    time_stamp = datetime.now().strftime("%Y%m%d_%H%M%S")

    filename = f"{test_name}_{time_stamp}.png"

    filepath = os.path.join(
        "screenshots",
        filename
    )

    driver.save_screenshot(filepath)

    return filepath