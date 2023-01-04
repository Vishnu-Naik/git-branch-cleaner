from git import Repo, InvalidGitRepositoryError
from pathlib import Path


class GitRepoCleaner:
    """
    This class is used to connect to git repository and delete branches which are not in remote repository.
    This class has two methods:
    1. get_local_and_remote_branches(repo_path: str) -> tuple[list[str], list[str]]
    2. delete_branches(local_branches: list[str], remote_branches: list[str]) -> None

    """

    @staticmethod
    def get_repo(repo_path: str) -> Repo:
        """Get git repository object

        Args:
            repo_path (str): Path to local git repository

        Returns:
            Repo: Git repository object

        Raises:
            AssertionError: If repository is bare
            InvalidGitRepositoryError: If repository is not a valid git repository
        """
        repo_path = Path(repo_path) if repo_path else Path.cwd()
        try:
            repo = Repo(repo_path)
        except InvalidGitRepositoryError:
            print('=' * 100)
            print(
                f'Invalid git repository or no git repository found at given path {repo_path} \nPlease check the path.')
            print('=' * 100)
            raise InvalidGitRepositoryError

        assert not repo.bare

        return repo

    @staticmethod
    def get_local_and_remote_branches(repo_path: str = None) -> tuple[list[str], list[str]]:
        """Get branches from local and remote repository

        Args:
            repo_path (str): Path to local git repository

        Returns:
            tuple: Tuple of lists of local and remote branches
        """
        repo = GitRepoCleaner.get_repo(repo_path)

        remote_refs = repo.remote().refs
        remote_branches = []
        local_branches = []

        for refs in remote_refs:
            remote_branches.append(refs.name.replace('origin/', ''))

        for refs in repo.branches:
            local_branches.append(refs.name)

        return local_branches, remote_branches

    @staticmethod
    def delete_branches(repo_path: str) -> None:
        """Delete branches which are not in remote repository

        Args:
            repo_path(str): Path to local git repository

        Returns:
            None
        """
        repo = GitRepoCleaner.get_repo(repo_path)
        local_branches, remote_branches = GitRepoCleaner.get_local_and_remote_branches(repo_path)
        local_branches_not_on_remote = list(set(local_branches).symmetric_difference(set(remote_branches)))
        is_check = input(f"There {'is' if len(local_branches_not_on_remote) == 1 else 'are'} "
                         f"{len(local_branches_not_on_remote)} branch[s] which are not in remote repository. "
                         f"They are listed as below:\n" + '\n #'.join(local_branches_not_on_remote) +
                         "\nWant to delete them? (y/n): ")
        if is_check.upper() == "Y":
            for branch in local_branches:
                print(f"Fetching branch...\n")
                if branch not in remote_branches:
                    permission_given = input(f"Attempting to DELETE branch: {branch}\n Are you sure? (y/n): ")

                    if permission_given.upper() == "Y":
                        print(f"Deleting branch: {branch} ...")
                        repo.delete_head(branch, force=True)
                        print(f"{branch} is deleted from local repository")
                    else:
                        print(f"Branch {branch} is not deleted")
                else:
                    print(f"Branch {branch} is OK")
        else:
            print('[INFO] You can delete them manually by running: git branch -d <branch_name> (for local) '
                  'or git push origin --delete <branch_name> (for remote)')



def main(repo_path: str = '') -> None:
    """This is the main function which is used to run the program

    Args:
        repo_path (str): Path to local git repository

    Returns:
        None
    """
    local_branches, remote_branches = GitRepoCleaner.get_local_and_remote_branches(repo_path)
    print('=' * 100)
    print('List of remote branches: \n' + '\n'.join(remote_branches))
    print('-' * 100)
    print('List of local branches: \n' + '\n'.join(local_branches))
    print('=' * 100)
    if len(remote_branches) == len(local_branches):
        print("ALL OK!!! \nYour local repository and remote are in sync\n")
    elif len(remote_branches) < len(local_branches):
        GitRepoCleaner.delete_branches(repo_path)
    else:
        print("Looks like you have some branches in remote repository which are not in local repository. "
              "Try to fetch them first by running: git fetch")
