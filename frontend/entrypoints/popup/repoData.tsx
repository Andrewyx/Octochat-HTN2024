import React, { useEffect, useState } from 'react';

// Function to parse repository info from a GitHub URL
const parseRepoInfo = (url: string) => {
  const repoPattern = /github\.com\/([^/]+)\/([^/]+)\/?/;
  const match = url.match(repoPattern);
  if (match) {
    return { owner: match[1], repo: match[2] };
  }
  return null;
};

const RepoData: React.FC = () => {
  const [repoInfo, setRepoInfo] = useState<{ owner: string; repo: string } | null>(null);

  useEffect(() => {
    const url = window.location.href;
    console.log(url);
    const info = parseRepoInfo(url);

    if (info) {
      setRepoInfo(info);
      localStorage.setItem('repoInfo', JSON.stringify(info)); // Store in localStorage
    } else {
      setRepoInfo(null);
    }
  }, []);

  return (
    <div>
      {repoInfo ? (
        <div>
          <h2>Repository Information</h2>
          <p>Owner: {repoInfo.owner}</p>
          <p>Repository: {repoInfo.repo}</p>
        </div>
      ) : (
        <p>No valid GitHub repo detected.</p>
      )}
    </div>
  );
};

export default RepoData;
