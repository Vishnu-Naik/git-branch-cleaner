from cleaner import git_repo_cleaner
import argparse

parser = argparse.ArgumentParser(
    description='Connect to git repository and delete branches which are not in remote repository')
parser.add_argument('-r', '--repo_path', required=False, help='Path to local git repository')

def main():
    repo_path = parser.parse_args().repo_path
    git_repo_cleaner.main(repo_path)

if __name__ == '__main__':
    main()
