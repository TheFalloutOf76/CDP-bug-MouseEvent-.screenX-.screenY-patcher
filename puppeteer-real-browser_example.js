async function main() {
    const { connect } = await import('puppeteer-real-browser');

    // change this to the path of the folder containing the extension
    const EXTENSION_PATH = `${__dirname}/turnstilePatch/`;

    const { page, browser } = await connect({
        args: [
            `--disable-extensions-except=${EXTENSION_PATH}`,
            `--load-extension=${EXTENSION_PATH}`
        ],
        turnstile: true,
    });
    page.goto('https://nopecha.com/demo/cloudflare');
}

main()