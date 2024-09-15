export interface URL {
    url: string
  }

export default function Button({url}:URL) {

    return(
      <>
      <button className="download-button" onClick={() => alert('Repo uploaded!')}>
              Validate
            </button>
            </>
    )
  }