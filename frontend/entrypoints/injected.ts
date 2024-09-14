export default defineUnlistedScript(() => {

    console.log('hello from injected.ts')

    const script = document.createElement('script');
    script.src = 'https://cdn.voiceflow.com/widget/bundle.mjs';
    script.type = 'text/javascript';

    script.onload = function () {
      console.log('Voiceflow chat available, loading the chat widget...');

      (window as any).voiceflow?.chat?.load({
        verify: { projectID: '66e57d0592f43d1a82365bbe' },
        url: 'https://general-runtime.voiceflow.com',
        versionID: 'production',
      });
    };

    script.onerror = function () {
      console.error('failed to load Voiceflow script');
    };

    document.head.appendChild(script);
  });