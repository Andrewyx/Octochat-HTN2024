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

      chrome.storage.sync.set({ VOICEFLOW_API_KEY: "VF.DM.66e5c1c0380effe3d506deb7.zq9kiS8nAEfLUcYR" }, function () {
        console.log('API key is set.');
      });
    },
  );
});