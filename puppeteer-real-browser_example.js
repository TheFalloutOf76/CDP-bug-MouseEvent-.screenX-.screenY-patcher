async function main() {
    const { connect } = await import('puppeteer-real-browser');

    // not needed anymore cuz library already does it automatically 😉👌
    //const EXTENSION_PATH = `${__dirname}/turnstilePatch/`;

    const { page, browser } = await connect({
        /*
        args: [
            `--disable-extensions-except=${EXTENSION_PATH}`,
            `--load-extension=${EXTENSION_PATH}`
        ],
        */
        turnstile: true,
    });
    page.goto('https://nopecha.com/demo/cloudflare');
}

main()