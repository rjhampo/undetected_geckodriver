# Undetected GeckoDriver v1.0.0

[![PyPI version](https://badge.fury.io/py/undetected_geckodriver.svg)](https://badge.fury.io/py/undetected_geckodriver)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## Overview

Undetected GeckoDriver is a wrapper around Selenium's `webdriver.Firefox` that patches the driver to bypass detection mechanisms used by various web services. This package is designed to be a drop-in replacement for Selenium's `webdriver.Firefox` and can be used in the same way.

## Installation

You can install the package via pip:

```bash
pip install undetected-geckodriver
```

## Usage

Here's a basic example of how to use Undetected GeckoDriver:

```python
from undetected_geckodriver import Firefox

driver = Firefox()
driver.get("https://www.google.com")

# Use it like a normal Selenium driver ...
```

## Requirements

- Python 3.6+
- Selenium 4.10.0+

## Contributing

Contributions are welcome! Please feel free to open an issue or submit a pull request if you encounter any problems or have any suggestions.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Author

- **ByteXenon** - [GitHub](https://github.com/ByteXenon)

## Acknowledgments

- Special thanks to the contributors of the Selenium project.
- Inspiration from the [undetected-chromedriver project](https://github.com/ultrafunkamsterdam/undetected-chromedriver).