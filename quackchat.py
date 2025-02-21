import requests
import json
from user_agent import generate_user_agent

requests.urllib3.disable_warnings()

class DC:
    def __init__(self, model="o3-mini", proxy=None, user_agent=None, verify=False, timeout=30):
        self.model = model
        self.proxy = proxy
        self.user_agent = user_agent if user_agent else generate_user_agent()
        self.verify = verify
        self.timeout = timeout

        history = []
        self.history = history

    def genchat(self, prompt, payload=None):
        xvqd_4 = self._get_xvqd_4()
        if payload is None:
            payload = {
                "model": self.model,
                "messages": [{"role": "user", "content": prompt}]
            }
        head = {
            "User-Agent": self.user_agent,
            "X-Vqd-4": xvqd_4,
        }
        
        payload = payload

        r = requests.post(
            "https://duckduckgo.com/duckchat/v1/chat",
            json=payload,
            headers=head,
            proxies=self.proxy,
            verify=self.verify,
            timeout=self.timeout,
        )
        
        full_message = ""

        for line in r.iter_lines(decode_unicode=True):
            if not line:
                continue
            if line.startswith("data:"):
                data_line = line[len("data:"):].strip()
                if data_line == "[DONE]":
                    break
                try:
                    data_json = json.loads(data_line)
                except json.JSONDecodeError as e:
                    print("JSON decode error:", e)
                    continue

                if "message" in data_json:
                    full_message += data_json["message"]
        
        return full_message

    def chat(self, prompt):
        self._save_history("request", prompt)
        payload = {
            "model": self.model,
            "messages": self.history
        }

        response = self.genchat(prompt, payload)
        self._save_history("response", response)
        return response

    def _save_history(self, history_type, content):
        if history_type == "request":
            self.history.append({"role": "user", "content": content})
        elif history_type == "response":
            self.history.append({"role": "assistant", "content": content})

    def _get_xvqd_4(self):
        head = {
            "User-Agent": self.user_agent,
            "X-Vqd-Accept": "1"
        }
        r = requests.get(
            "https://duckduckgo.com/duckchat/v1/status",
            headers=head,
            proxies=self.proxy,
            verify=self.verify,
            timeout=self.timeout
        )
        return r.headers.get("X-Vqd-4", "")

if __name__ == "__main__":
    RESET = "\033[0m"
    BOLD = "\033[1m"
    UNDERLINE = "\033[4m"
    REVERSED = "\033[7m"
    
    # Foreground colors
    FG_BLACK = "\033[30m"
    FG_RED = "\033[31m"
    FG_GREEN = "\033[32m"
    FG_YELLOW = "\033[33m"
    FG_BLUE = "\033[34m"
    FG_MAGENTA = "\033[35m"
    FG_CYAN = "\033[36m"
    FG_WHITE = "\033[37m"
    
    # Background colors
    BG_BLACK = "\033[40m"
    BG_RED = "\033[41m"
    BG_GREEN = "\033[42m"
    BG_YELLOW = "\033[43m"
    BG_BLUE = "\033[44m"
    BG_MAGENTA = "\033[45m"
    BG_CYAN = "\033[46m"
    BG_WHITE = "\033[47m"

    # Bright foreground colors
    FG_BRIGHT_BLACK = "\033[90m"
    FG_BRIGHT_RED = "\033[91m"
    FG_BRIGHT_GREEN = "\033[92m"
    FG_BRIGHT_YELLOW = "\033[93m"
    FG_BRIGHT_BLUE = "\033[94m"
    FG_BRIGHT_MAGENTA = "\033[95m"
    FG_BRIGHT_CYAN = "\033[96m"
    FG_BRIGHT_WHITE = "\033[97m"

    # Bright background colors
    BG_BRIGHT_BLACK = "\033[100m"
    BG_BRIGHT_RED = "\033[101m"
    BG_BRIGHT_GREEN = "\033[102m"
    BG_BRIGHT_YELLOW = "\033[103m"
    BG_BRIGHT_BLUE = "\033[104m"
    BG_BRIGHT_MAGENTA = "\033[105m"
    BG_BRIGHT_CYAN = "\033[106m"
    BG_BRIGHT_WHITE = "\033[107m"
    
    
    
    print(BOLD + "Welcome to DuckDuckGo Chat!" + RESET)
    print("Type 'exit' to quit.")
    d = DC()
    while True:
        user_input = input(FG_GREEN + "Prompt: " + RESET)
        if user_input.lower() == 'exit':
            break
        response = d.genchat(user_input)
        print(FG_CYAN + response + RESET)
