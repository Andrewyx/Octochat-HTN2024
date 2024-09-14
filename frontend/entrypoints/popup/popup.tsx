import React, { useEffect, useState } from 'react';

// Fetch repository info from localStorage (could also come from an API)
const fetchRepoInfo = () => {
  const storedRepoInfo = localStorage.getItem('repoInfo');
  return storedRepoInfo ? JSON.parse(storedRepoInfo) : null;
};

const Popup: React.FC = () => {
  const [repoInfo, setRepoInfo] = useState<{ owner: string; repo: string } | null>(null);

  useEffect(() => {
    const storedInfo = fetchRepoInfo();
    if (storedInfo) {
      setRepoInfo(storedInfo);
    }
  }, []);

  return (
    <div className="popup-container">
      {repoInfo ? (
        <div>
          <h3>Repository Info</h3>
          <p>Owner: {repoInfo.owner}</p>
          <p>Repo: {repoInfo.repo}</p>
        </div>
      ) : (
        <p>No repo data available.</p>
      )}
    </div>
  );
};

export default Popup;
