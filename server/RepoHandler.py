from Constants import DATA_FOLDER_PATH 

def get_repo(repo_url) -> None:
    repo = Repo.clone_from(repo_url, DATA_FOLDER_PATH)

def parse_downloaded_repo() -> None:
    pass

def is_valid_code_file(fileHeader: str) -> bool:
    return True

def rename_to_txt() -> None:
    pass
