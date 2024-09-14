export default defineContentScript({
<<<<<<< HEAD
  matches: ['*://*.github.com/*/*'],
  main() {
    console.log('Hello content.');
    console.log(window.location.href);
=======
  matches: ["*://*/*"],
  async main() {
    console.log("Injecting script...");
    await injectScript('/injected.js', {
      keepInDom: true,
    });
    console.log("Done!");
>>>>>>> f36fe19 (loading in chat)
  },
});