import git
from git.refs.remote import RemoteReference
from git.cmd import Git
import subprocess

import git

repo_url = 'https://github.com/armenforget/stackoverflow_samples.git'
local_repo_dir = "../dummy_repo"

repo = git.Repo.clone_from(repo_url, local_repo_dir, depth=1)
result = repo.git.execute('git rev-parse origin/master')
print(result)

#import subprocess
#process = subprocess.Popen(["git", "ls-remote", repo_url], stdout=subprocess.PIPE)
#output = process.communicate()[0]