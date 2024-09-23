To execute all tests in headless mode
pytest

To execute in specific browser in headed mode(default is chromium)
pytest --headed

To execute in firefox browser in headed mode
pytest --browser firefox --headed

To execute in webkit browser in headed mode
pytest --browser firefox --headed

To execute with slow mode flag with specified time interval(in milliseconds)
pytest --headed --slowmo <time_interval>

To execute in verbose and debug mode
pytest -v -s --headed

Generate HTML
pytest -v -s --headed --html=reports/report.html --capture=tee-sys

Execute in multiple browsers
pytest -v -s --browser firefox --browser webkit --headed

Execute in branded browser channels(chrome or edge)
pytest -v -s --browser-channel msedge

Execute in mobile device emulation
pytest -v -s --headed --device="iPhone 15 Pro Max"

Taking screenshots(on, only-on-failure, default is off,--full-page-screenshot)
pytest -v -s --headed --screenshot=only-on-failure

Capturing Videos(on, retain-on-failure, default is off)
pytest -v -s --headed --video=retain-on-failure
