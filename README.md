# GitBranchCleaner

GitRepoCleaner is a tool to clean up git repositories. 
This tool allows users to delete branches from a local git repository that are not present in the remote repository.
This tool is useful when you have a lot of branches in your local repository, and you want to clean up your local repository.
This tool is not intended to delete remote branches as it is not safe to do so and one might need to do a lot of manual work to recover from such a mistake.

# Installation
To use the tool first install using pip or git clone the repository and run the setup.py file:
```commandline
pip install git-branch-cleaner
```
or
```commandline
git clone https://github.com/Vishnu-Naik/git-branch-cleaner
cd git-branch-cleaner
python setup.py install
```

# Usage
This tool can be used as a command line tool or as a library. Let's see those two options in detail.

## Command Line Tool

The command line tool can be used to delete branches from a local repository that are not present in the remote repository.
The command line tool can be used as follows:

```bash
repo_cleaner --repo <path to git repository>
```


--repo is the optional flag to the command. If this flag is not provided, the current working directory is assumed to be the git repository. 
The tool will show the branches that are on local and remote. As shown below:
```
=================================================
List of remote branches:
main
develop
feature/branch1
=================================================
List of local branches:
main
develop
feature/branch1
feature/branch2
=================================================
```
 

The tool will ask the user if they want to delete the branches that are not present in the remote repository. 
If the user enters anything else other than Y or y, the tool will end its execution. Else it will display the branches that are not present in the remote repository one after the other which are
going to be deleted and ask for confirmation before deleting each of the branches.

## Library

To use this tool as a library, you can import the GitRepoCleaner class from the git_repo_cleaner module and use it as follows:

from cleaner import git_repo_cleaner

```python
from cleaner import git_repo_cleaner

git_repo_cleaner.main('D:\STUDY MATERIAL\Masters Study Material\WS2022\Thesis\CodeBase\AccessPointSearch')
 ```
For finer functionality, you can use the GitRepoCleaner class directly as follows:
```python
from cleaner.git_repo_cleaner import *

local_branches, remote_branches = GitRepoCleaner.get_local_and_remote_branches()
print(local_branches)
```
