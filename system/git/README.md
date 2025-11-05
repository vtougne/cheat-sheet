# GIT


#### list tag with time and ordered by time

```bash
git for-each-ref --sort=creatordate --format '%(refname) %(creatordate)' refs/tags
```
#### delete remote tag / branch

```bash
git push --delete origin tagname / branch
```

### undo last commit
```bash
git reset HEAD~
git restore super_file.txt
```



#### pushing existing repo to new git bare repo

1. Create new empty project on remote git

2. duplicate local repo
```bash
   copy -rp <local_repo> <new_repo>
   cd <new_repo>
```

3. change git origine
```bash
   git remote set-url origin git@local-gitlab.me:root/new_repo.git
```

4. push all tags
```bash
   git push
   git push --tags
```

#### add new remote repository to existing repo

```bash
git remote add my-gitlab git@my-gitlab.home:root/jtable.git

```




### Remove file from repo history and tags
- install git-filter-repo 
```bash
sudo apt install git-filter-repo
```

- remove file from hostory
```bash
git filter-repo --path <chemin-du-fichier> --invert-paths
```

- force push remote repo
```bash
git push origin --force --all

```

- force push tag remote repo
```bash
git push origin --force --tags
```



```
Voici les commandes pour effectuer ces opérations :

  # 1. Récupérer les dernières modifications des deux remotes
  git fetch local-gitlab
  git fetch my-gitlab

  # 2. Configurer la branche main pour tracker local-gitlab
  git config branch.main.remote local-gitlab

  # 3. Réinitialiser la branche main sur local-gitlab/main (la version en retard)
  git reset --hard local-gitlab/main

  # 4. Créer une branche develop à partir de main (local-gitlab/main)
  git checkout -b develop

  # 5. Merger le contenu de my-gitlab/main dans develop
  git merge my-gitlab/main

  # 6. Pousser develop vers local-gitlab
  git push local-gitlab develop

  Voulez-vous que j'exécute ces commandes pour vous ?
```