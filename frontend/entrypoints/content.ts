export default defineContentScript({
  matches: ['*://*.github.com/*/*'],
  main() {
    console.log('Hello content.');
    (browser.action ?? browser.browserAction).onClicked.addListener(
      async (tab) => {
        try {
          const dataUrl = await browser.tabs.captureTab();
          console.log(dataUrl);
        } catch (err) {
          console.error("Cannot get URL current tab", tab, err);
        }
      },
    );
  },
});
