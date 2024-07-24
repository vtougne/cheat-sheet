# GIT

## pushing existing repo to new git bare repo

1. Create new empty project on remote git
2. duplicate local repo
   ```
   copy -rp <local_repo> <new_repo>
   cd <new_repo>
   ```
3. change git origine
   ```
   git remote set-url origin git@local-gitlab.me:root/new_repo.git
   ```
4. push all tags
   ```
   git push --tags
   ```