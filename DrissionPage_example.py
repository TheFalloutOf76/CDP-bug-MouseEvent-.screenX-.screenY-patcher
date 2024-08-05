from DrissionPage import ChromiumPage, ChromiumOptions
import time
import os

co = ChromiumOptions()
co.auto_port()

# change this to the path of the folder containing the extension
EXTENSION_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), "turnstilePatch"))
co.add_extension(EXTENSION_PATH) 

# uncomment this if you want to use headless mode
"""
co.headless()

from sys import platform
if platform == "linux" or platform == "linux2":
    platformIdentifier = "X11; Linux x86_64"
elif platform == "darwin":
    platformIdentifier = "Macintosh; Intel Mac OS X 10_15_7"
elif platform == "win32":
    platformIdentifier = "Windows NT 10.0; Win64; x64"

co.set_user_agent(f"Mozilla/5.0 ({platformIdentifier}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36")
"""

page = ChromiumPage(co)
page.get("https://2captcha.com/demo/cloudflare-turnstile")

def getTurnstileToken():
    page.run_js("try { turnstile.reset() } catch(e) { }")

    turnstileResponse = None

    for i in range(0, 15):
        try:
            turnstileResponse = page.run_js("try { return turnstile.getResponse() } catch(e) { return null }")
            if turnstileResponse:
                return turnstileResponse
            
            # pov you tried to hide the turnstile 🍆😫
            challengeSolution = page.ele("@name=cf-turnstile-response", timeout=1)
            challengeWrapper = challengeSolution.parent()
            challengeIframe = challengeWrapper.shadow_root.ele("tag:iframe", timeout=1)
            challengeIframeBody = challengeIframe.ele("tag:body", timeout=1).shadow_root
            challengeButton = challengeIframeBody.ele("tag:input", timeout=1)
            challengeButton.focus()
            challengeButton.click()
        except:
            pass
        time.sleep(1)
    page.refresh()
    raise Exception("failed to solve turnstile")

while True:
    print(getTurnstileToken())