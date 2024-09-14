export default defineBackground(() => {
  console.log('Hello background!', { id: browser.runtime.id });
});


// Import the necessary data or functions (though you may not directly import TSX components here)
import { RepoInfo } from './popup/repoData.tsx';

// Function to process and validate GitHub URLs
function handleUrl(url: string): void {
  if (isGitHubRepoUrl(url)) {
    const repoInfo = parseGitHubRepoUrl(url);
    console.log('GitHub Repo Info:', repoInfo);
    // Save repoInfo in storage or handle it as needed
    chrome.storage.local.set({ repoInfo });
  }
}

function isGitHubRepoUrl(url: string): boolean {
  const githubUrlPattern = /^(https:\/\/)?(www\.)?github\.com\/([a-zA-Z0-9_-]+)\/([a-zA-Z0-9_-]+)(\/)?$/;
  return githubUrlPattern.test(url);
}

function parseGitHubRepoUrl(url: string): RepoInfo | null {
  const match = url.match(/github\.com\/([a-zA-Z0-9_-]+)\/([a-zA-Z0-9_-]+)/);
  if (match) {
    return {
      owner: match[1],
      repo: match[2]
    };
  }
  return null;
}

// Event listeners for tab updates or URL changes
chrome.tabs.onActivated.addListener(async (activeInfo) => {
  const tab = await chrome.tabs.get(activeInfo.tabId);
  if (tab.url) {
    handleUrl(tab.url);
  }
});

chrome.tabs.onUpdated.addListener(async (tabId, changeInfo) => {
  if (changeInfo.status === 'complete') {
    const tab = await chrome.tabs.get(tabId);
    if (tab.url) {
      handleUrl(tab.url);
    }
  }
});
