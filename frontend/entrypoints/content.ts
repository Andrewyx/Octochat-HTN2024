import { URL } from "./popup/Button";

export default defineContentScript({
  matches: ['*://*.github.com/*/*'],
  main() {
    sendURL(window.location.href);
  },
});

async function sendURL(url: string) {
  try {
    console.log('sending url: ', url);
    const response = await fetch('http://localhost:5525/parseurl', {
      method: 'POST',
      body: JSON.stringify({
        url: url
      }),
      headers: {
        'Content-Type':'application/json',
        'Access-Control-Allow-Origin':'*',
        'Access-Control-Allow-Methods':'POST,PATCH,OPTIONS'
      },
    });

    if (!response.ok) {
      throw new Error(`Error! status: ${response.status}`);
    }

    const result = (await response.json());

    console.log('result is: ', JSON.stringify(result, null, 4));

    return result;
  } catch (error) {
    if (error instanceof Error) {
      console.log('error message: ', error.message);
      return error.message;
    } else {
      console.log('unexpected error: ', error);
      return 'An unexpected error occurred';
    }
  }

}