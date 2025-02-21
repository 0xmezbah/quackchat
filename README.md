# 🦆 QuackChat: Unofficial DuckDuckGo Chat API Wrapper <img src="https://raw.githubusercontent.com/twitter/twemoji/master/assets/72x72/1f986.png" width="30" height="30">

[![GitHub issues](https://img.shields.io/github/issues/0xmezbah/quackchat.svg)](https://github.com/yourusername/quackchat/issues)  
[![GitHub stars](https://img.shields.io/github/stars/0xmezbah/quackchat.svg)](https://github.com/yourusername/quackchat/stargazers) 
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

*A simple, **unofficial Python library** to access **DuckDuckGo's Chat** functionality. Interact with **DuckDuckGo's AI chat** directly from your Python code. **No API key needed!***

## ✨ Overview

QuackChat is a lightweight, easy-to-use **Python wrapper** for the **DuckDuckGo Chat API**. It allows you to seamlessly integrate **DuckDuckGo's conversational AI** capabilities into your **Python projects**, scripts, and applications.  Leverage the power of **DuckDuckGo Chat** without complex setup or official API keys. Perfect for quick prototyping, experimentation, and building **chatbots** or other **AI-powered tools**. 🚀

## 🌟 Features

*   **Easy DuckDuckGo Chat Integration:**  Access **DuckDuckGo Chat** with minimal Python code.
*   **Streaming Responses:** Receive **chat responses** as they are generated, providing a dynamic and responsive user experience.
*   **Chat History Management:** Built-in support for maintaining **conversation context** through chat history.
*   **Customizable Settings:**  Adjust the **chat model**, **proxy**, **user agent**, and other parameters for fine-grained control.
*   **No API Key Required:** Directly interacts with DuckDuckGo's publicly available endpoint.
*   **Lightweight and Efficient:**  Uses only the `requests` and `user_agent` libraries, minimizing dependencies.
*   **Open Source (MIT License):**  Freely use, modify, and distribute the code.

## 🚀 Getting Started

1.  **Clone the Repository:**

    ```bash
    git clone https://github.com/0xmezbah/quackchat.git
    cd quackchat
    ```

2.  **Install Dependencies:**

    ```bash
    pip install requests user_agent
    ```
    (You may need to use `pip3` depending on your system.)

3.  **Run the Example:**

    ```python
    python quackchat.py
    ```

Here's the code you'll find in `quackchat.py` (or your main file):

```python
from quackchat import DC  # Assuming you've organized your code into a module

# Initialize the DuckDuckGo Chat client
d = DC()

# Get a response to a prompt
response = d.genchat("Explain the theory of relativity in simple terms.")
print(response)


# Example with a custom proxy and model
d_custom = DC(proxy={"http": "http://yourproxy:8080", "https": "http://yourproxy:8080"}, model="o3-mini")
response_custom = d_custom.genchat("Tell me a joke.")
print(response_custom)

## ⚙️ Configuration Options

The `DC` class constructor accepts the following optional parameters:

| Parameter      | Type     | Default             | Description                                                                    |
| -------------- | -------- | ------------------- | ------------------------------------------------------------------------------ |
| `model`        | `str`    | `"o3-mini"`        | The **DuckDuckGo Chat model** to use. Check DuckDuckGo for available options. |
| `proxy`        | `dict`   | `None`              | Proxy settings for the `requests` library (if needed).                       |
| `user_agent`   | `str`    | (Generated)         | The User-Agent string for HTTP requests.                                     |
| `verify`       | `bool`   | `False`            | Whether to verify SSL certificates (set to `True` for increased security).    |
| `timeout`      | `int`    | `30`                | The request timeout in seconds.                                               |

## 📚 API Reference

### `DC(model="o3-mini", proxy=None, user_agent=None, verify=False, timeout=30)`

Creates a new **DuckDuckGo Chat client** instance.

*   **Parameters:** See the table above.
*   **Returns:** A `DC` object.

### `genchat(prompt, payload=None)`

Gets a **chat response** for a single prompt from **DuckDuckGo Chat**.

*   **Parameters:**
    *   `prompt` (`str`): The user's input text (**prompt**).
    *   `payload` (`dict`, optional): A custom JSON payload. Use only if you understand the DuckDuckGo Chat API.
*   **Returns:** The complete generated text as a string.

### `chat(prompt)`

Maintains **chat history** and retrieves a response, preserving the **conversation context**.

*   **Parameters:**
    *   `prompt` (`str`):  The user's input text.
*   **Returns:** The complete generated text response as a string.

### `_save_history(history_type, content)`

*(Internal method)* Saves the request or response to the internal chat history.

### `_get_xvqd_4()`

*(Internal method)* Retrieves the `X-Vqd-4` header from DuckDuckGo.

## 🤝 Contributing

Contributions are highly encouraged! To contribute:

1.  **Fork** the repository on GitHub.
2.  Create a new branch: `git checkout -b feat/your-amazing-feature`
3.  Implement your changes and commit them: `git commit -m 'Add: Awesome new feature'`
4.  Push to the branch: `git push origin feat/your-amazing-feature`
5.  Open a **Pull Request** on GitHub.

Please follow these guidelines:

*   Use the [Black code style](https://github.com/psf/black) for consistent formatting.
*   Write clear and descriptive commit messages.
*   Include tests if you add new features.

## 📝 License

This project is licensed under the MIT License – see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgements

*   **DuckDuckGo** for their chat service.

## ❓ FAQ

*   **Q: Is this an official DuckDuckGo library?**
    *   A: No, it's an **unofficial wrapper**. Use it responsibly and be aware of potential changes.
*   **Q: Do I need an API key?**
    *   A: No **API key** is required.  It interacts directly with DuckDuckGo's publicly available endpoint.
*    **Q: Why are some methods marked with an underscore (e.g., `_get_xvqd_4`)?**
     *   A: These are *internal* methods.  They are not part of the public API and might change without notice.

## ⚠️ Disclaimer

This project is not affiliated with or endorsed by DuckDuckGo. The underlying chat service is subject to change, which may affect this library's functionality. Use this tool responsibly and in accordance with DuckDuckGo's terms of service.

