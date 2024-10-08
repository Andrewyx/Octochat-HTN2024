import { defineConfig } from 'wxt';

// See https://wxt.dev/api/config.html
export default defineConfig({
  modules: ['@wxt-dev/module-react'],
  manifest: {
    permissions: ["activeTab", "downloads", "storage"],
    action: {},
    background: {
      service_worker: "background.js"
    }
  },
});
