# CDP bug MouseEvent .screenX .screenY patcher
another site to test the bug on: https://drissionpage.pages.dev/

## bug that this fixes: https://issues.chromium.org/issues/40280325
When the CDP command `Input.dispatchMouseEvent` is ran, the MouseEvent/PointerEvent created will have a "fake" property for .screenX and .screenY (they will be same as the .x and .y properties respectively). Cloudflare Turnstile is able to detect this and will mark you as a bot, and you won't be able to get past (Interstitial) Turnstile.

This extension fixes this by providing fake values for .screenX and .screenY. One downside of this is that now even real clicks will use fake values. However manually clicking in an automated browser is mostly non-existant so its fine, and .screenX and .screenY are rarely used anyways, so it should be fine. Let me know if it breaks something and I'll see if I can fix it.

TL;DR: Chrome has a bug allowing fake clicks to be detected. This extension fixes those detections so you can continue scraping.

## how to use
Load the extension in [./turnstilePatch/](/turnstilePatch/)

tested libraries:
* [DrissionPage](https://github.com/g1879/DrissionPage) ([example](/DrissionPage_example.py))
* [puppeteer-real-browser](https://github.com/zfcsoftware/puppeteer-real-browser) ([example](/puppeteer-real-browser_example.js))

## status
Gets past Cloudflare Turnstile

![turnstile success](https://files.catbox.moe/hx2i15.gif)