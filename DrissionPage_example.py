from DrissionPage import Chromium, ChromiumOptions
import time
import os

co = ChromiumOptions()
co.auto_port()

co.set_timeouts(base=1)

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

co.set_user_agent(f"Mozilla/5.0 ({platformIdentifier}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36")
"""

browser = Chromium(co)
page = browser.get_tabs()[-1]
page.get("https://turnstile.zeroclover.io/")

def getTurnstileToken():
    page.run_js("try { turnstile.reset() } catch(e) { }")

    turnstileResponse = None

    for i in range(0, 15):
        try:
            turnstileResponse = page.run_js("try { return turnstile.getResponse() } catch(e) { return null }")
            if turnstileResponse:
                return turnstileResponse
            
            challengeSolution = page.ele("@name=cf-turnstile-response")
            challengeWrapper = challengeSolution.parent()
            challengeIframe = challengeWrapper.shadow_root.ele("tag:iframe")
            
            challengeIframe.run_js("""
window.dtp = 1
function getRandomInt(min, max) {
    return Math.floor(Math.random() * (max - min + 1)) + min;
}

// old method wouldn't work on 4k screens

let screenX = getRandomInt(800, 1200);
let screenY = getRandomInt(400, 600);

Object.defineProperty(MouseEvent.prototype, 'screenX', { value: screenX });

Object.defineProperty(MouseEvent.prototype, 'screenY', { value: screenY });
                        """)
            
            challengeIframeBody = challengeIframe.ele("tag:body").shadow_root
            challengeButton = challengeIframeBody.ele("tag:input")
            challengeButton.click()
        except:
            pass
        time.sleep(1)
    page.refresh()
    raise Exception("failed to solve turnstile")

while True:
    print(getTurnstileToken())
