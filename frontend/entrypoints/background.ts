export default defineBackground(() => {
  // See https://developer.chrome.com/docs/extensions/develop/concepts/activeTab#invoking-activeTab
  (browser.action ?? browser.browserAction).onClicked.addListener(
    async (tab) => {
      try {
        const dataUrl = await browser.tabs.captureTab();
        console.log(dataUrl);
        console.log('something')
      } catch (err) {
        console.error("Cannot get URL current tab", tab, err);
      }
    },
  );
});