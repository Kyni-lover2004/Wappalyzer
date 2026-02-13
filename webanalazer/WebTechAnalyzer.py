import sys
import requests
from Wappalyzer import Wappalyzer, WebPage
from colorama import Fore, Style, init
import builtwith


init(autoreset=True)


class WebTechAnalyzer:
    def __init__(self, url):
        self.url = url if url.startswith('http') else f'https://{url}'
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }

    def analyze_wappalyzer(self):
        print(f"\n{Fore.CYAN}[*] Running Wappalyzer Analysis...{Style.RESET_ALL}")
        try:
            wappalyzer = Wappalyzer.latest()
            webpage = WebPage.new_from_url(self.url, headers=self.headers)
            techs = wappalyzer.analyze_with_versions_and_categories(webpage)

            if not techs:
                print(f"{Fore.YELLOW}[!] No specific technologies identified via Wappalyzer.")
                return

            for tech, info in techs.items():
                categories = ", ".join(info['categories'])
                version = info['versions'][0] if info['versions'] else "Unknown"
                print(
                    f"{Fore.GREEN}[+] {tech}{Style.RESET_ALL} (Version: {Fore.YELLOW}{version}{Style.RESET_ALL}) - {categories}")
        except Exception as e:
            print(f"{Fore.RED}[-][Wappalyzer Error]: {e}")

    def analyze_builtwith(self):
        print(f"\n{Fore.CYAN}[*] Running BuiltWith Analysis...{Style.RESET_ALL}")
        try:
            results = builtwith.parse(self.url)
            for category, apps in results.items():
                apps_str = ", ".join(apps)
                print(f"{Fore.GREEN}[+] {category.capitalize()}:{Style.RESET_ALL} {apps_str}")
        except Exception as e:
            print(f"{Fore.RED}[-][BuiltWith Error]: {e}")

    def check_headers(self):
        print(f"\n{Fore.CYAN}[*] Checking HTTP Headers...{Style.RESET_ALL}")
        try:
            response = requests.get(self.url, headers=self.headers, timeout=10)
            target_headers = ['Server', 'X-Powered-By', 'X-AspNet-Version', 'Via']
            found = False
            for header in target_headers:
                if header in response.headers:
                    print(f"{Fore.GREEN}[+] {header}:{Style.RESET_ALL} {response.headers[header]}")
                    found = True
            if not found:
                print(f"{Fore.YELLOW}[!] No sensitive headers found.")
        except Exception as e:
            print(f"{Fore.RED}[-][Header Error]: {e}")


def main():
    if len(sys.argv) < 2:
        print(f"Usage: python {sys.argv[0]} <domain.com>")
        sys.exit(1)

    target = sys.argv[1]
    analyzer = WebTechAnalyzer(target)

    print(f"{Fore.BLUE}{'=' * 50}")
    print(f"{Fore.WHITE} Analyzing Technology Stack for: {Fore.YELLOW}{target}")
    print(f"{Fore.BLUE}{'=' * 50}")

    analyzer.check_headers()
    analyzer.analyze_wappalyzer()
    analyzer.analyze_builtwith()


if __name__ == "__main__":
    main()