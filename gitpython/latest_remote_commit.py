from pathlib import Path

repo_url = 'https://github.com/armenforget/stackoverflow_samples.git'
local_repo_dir = Path('../dummy_repo')


def get_sha_with_gitpython():
    import git

    local_repo_dir.unlink(missing_ok=True)
    repo = git.Repo.clone_from(repo_url, local_repo_dir, depth=1)
    sha = repo.rev_parse('origin/master')
    # sha = repo.git.execute('git rev-parse origin/master')
    print(sha)
    local_repo_dir.unlink(missing_ok=True)


def get_sha_with_subprocess():
    import subprocess
    import re

    process = subprocess.Popen(["git", "ls-remote", repo_url], stdout=subprocess.PIPE)
    stdout, stderr = process.communicate()
    sha = re.split(r'\t+', stdout.decode('ascii'))[0]
    print(sha)


if __name__ == '__main__':
    get_sha_with_subprocess()
    get_sha_with_gitpython()
