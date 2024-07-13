from DrissionPage import ChromiumPage, ChromiumOptions
import time

co = ChromiumOptions()
co.auto_port()

# load in the chrome extension
co.add_extension("./turnstilePatch/")


page = ChromiumPage(co)
page.get("https://peet.ws/turnstile-test/managed.html")

def getTurnstileToken():
    page.run_js("try { turnstile.reset() } catch(e) { }")

    turnstileResponse = None

    for i in range(0, 15):
        try:
            turnstileResponse = page.run_js("try { return turnstile.getResponse() } catch(e) { return null }")
            if turnstileResponse:
                return turnstileResponse
            challengeWrapper = page.ele("@class=cf-turnstile-wrapper", timeout=1)
            challengeIframe = challengeWrapper.sr.ele("tag:iframe", timeout=1)
            challengeIframeBody = challengeIframe.ele("tag:body", timeout=1).sr
            challengeButton = challengeIframeBody.ele("tag:input", timeout=1)
            challengeButton.click()
        except:
            pass
        time.sleep(1)
    page.refresh()
    raise Exception("failed to solve turnstile")

while True:
    print(getTurnstileToken())