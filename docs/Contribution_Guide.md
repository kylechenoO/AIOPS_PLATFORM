# AIOPS PLATFORM Contribution Guide

**Preparing**
1. fork the project
2. clone your own project repo(which 1st step fork into your github account) into your file system.
3. run `git branch dev` to create a new branch.
4. run `git checkout dev` to your new branch.
5. run `git remote add upstream https://github.com/aiops-project/AIOPS_PLATFORM.git`, to setup your upstream.

**Pull from upstream**
1. run `git pull --rebase upstream master`. ATTENTION: you must run this command everday and before you commit code into your own repo.

**Commit code**
1. run `git add *`
2. run `git commit -am 'YOUR_COMMENT_HERE'`
3. run `git push -u origin dev`
4. open your project repo, and submit `Pull Request` to upstream repo.

**How to Contribute**
claim some issue -> develop -> submit `Pull Request` -> wait for merge or comment
