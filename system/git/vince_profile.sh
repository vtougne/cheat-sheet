

# line to add in ~/.bash_aliases
# . /home/vince/dev/home/vince_profile.sh

set -o vi
alias ll='ls -lrta'
export pp=~/dev/project
alias cdp="cd $pp"
me=~/dev/home/vince_profile.sh
export ANSIBLE_STDOUT_CALLBACK=yaml
export ANSIBLE_INVENTORY=/home/vince/dev/home/ansible_inventory
export PYTHONDONTWRITEBYTECODE=1
# export PATH=$PATH:/home/vince/dev/project/jtable/jtable
alias dps='docker ps --format "table {{.Names}}\t{{.State}}\t{{.Status}}"'

# cdp

tee <<'EOF'

 ___      ___  __    _____  ___    ______    _______                  
|"  \    /"  ||" \  (\"   \|"  \  /" _  "\  /"     "|                 
 \   \  //  / ||  | |.\\   \    |(: ( \___)(: ______)                 
  \\  \/. ./  |:  | |: \.   \\  | \/ \      \/    |                   
   \.    //   |.  | |.  \    \. | //  \ _   // ___)_                  
    \\   /    /\  |\|    \    \ |(:   _) \ (:      "|                 
     \__/    (__\_|_)\___|\____\) \_______) \_______)                 
                                                                      
   _______    _______     ______    _______  __    ___       _______  
  |   __ "\  /"      \   /    " \  /"     "||" \  |"  |     /"     "| 
  (. |__) :)|:        | // ____  \(: ______)||  | ||  |    (: ______) 
  |:  ____/ |_____/   )/  /    ) :)\/    |  |:  | |:  |     \/    |   
  (|  /      //      /(: (____/ // // ___)  |.  |  \  |___  // ___)_  
 /|__/ \    |:  __   \ \        / (:  (     /\  |\( \_|:  \(:      "| 
(_______)   |__|  \___) \"_____/   \__/    (__\_|_)\_______)\_______) 
                                                                                                                                                     
                                                                                                                                                                                                                      
EOF


echo Functions:
echo '- reload                  reload profile'
echo '- lpush                   add, commit, push'
echo '- pull_all                pull all repo in ${repo_path}'
echo '- gitlab_start            gitlab_start'
echo '- gitlab_stop             gitlab_stop'
echo
echo Aliases:
echo '- cdp                        cd ~/dev/project'
echo
echo "Source script: $me"
echo "project path: \$pp"
echo



#############
# Functions #
#############

function reload() {
# . /home/vince/dev/home/vince_profile.sh
. $me
}

function glsremote() {  
  git for-each-ref --sort=creatordate --format '%(refname) %(creatordate)' refs/tags
}
function f_exec() {
  echo "exec: $@"
  eval "$@"
  return $?
}

function git_delete_all_branch() {
  prompt="Are you sure you want to delete all branches except main? (y/n) "
  read -p "$prompt" -n 1 -r
  echo    # (optional) move to a new line
  if [[ $REPLY =~ ^[Yy]$ ]]; then
    echo "Deleting all branches except main..."
  else
    echo "Aborting deletion."
    return 1
  fi
  git switch main && git branch | grep -v main | xargs git branch -D
}


function pull_all() {
  old_pwd=$PWD
  cd ${$epo_path}
  for repo in * ; do
    if [ -d $repo ] ; then
      cd $repo
      echo "info: pulling repo $repo"
      git pull
      cd ..
    fi
  done
  cd $old_pwd
}

function lpush() {
  target_repo_path=/repos/local-gitlab
  target_repo_url=git@local-gitlab.me
  target_repo_username=root
  ___git_push $target_repo_path $target_repo_url $target_repo_username "$@"
}

function gpush() {
  target_repo_path=/repos/github/
  target_repo_url=git@github.com
  target_repo_username=vtougne
  ___git_push $target_repo_path $target_repo_url $target_repo_username "$@"
}



function ___git_push() {
    [ ! $1 ] && { echo "ERROR: $FUNCNAME required target_repo_path and remote srv" ; return 1; }
    target_repo_path=$1
    shift
    target_repo_url=$1
    shift
    target_repo_username=$1

    branch=${2:-develop}
    commit_message="${3:-$branch}"

    export OLD_IFS=$IFS
    export IFS="
"
    source_path=$PWD
    project_name=${PWD##*/}
    echo info: project_name: $project_name
    echo info: target_repo_path: $target_repo_path
    parent_project_path=$(echo ${PWD%/*} | sed "s/.*\///g")
    echo info: parent_project_path: $parent_project_path
    echo info: commit_message: $commit_message

    if [ $parent_project_path != "project" ] ; then
      echo ERROR parent path must be project
      return 1
    fi

    if [ ! -d "${target_repo_path}/${project_name}" ] ; then
      echo "ERROR ${target_repo_path}/${project_name} doesn't exist or is not a directory"
      return 1
    fi

    cd ${target_repo_path}/${project_name}
    f_exec "git remote set-url origin ${target_repo_url}:${target_repo_username}/${project_name}.git"
    gitlab_repo_url=$(git config remote.origin.url | cut -d"@" -f2 | cut -d":" -f1)

    echo info: gitlab_repo_url: $gitlab_repo_url
    # return 0
    f_exec "git switch main" || return $?
    f_exec "git pull" || return $?

    # Check remote branch exists
    git ls-remote --exit-code --heads origin $branch
    if [  $? -eq 0 ] ; then
      f_exec "git switch $branch" || return $?
      f_exec "git pull" || return $?
    else
      git show-ref --verify --quiet refs/heads/$branch
      if [  $? -ne 0 ] ; then
        f_exec "git checkout -b $branch" || return $?
      fi
    fi


    if [ -f ${source_path}/_gitignore ] ; then
      f_exec "cp -p ${source_path}/_gitignore ${source_path}/.gitignore" || return $?
      target_gitignore="${target_repo_path}/${project_name}/.gitignore"
      echo info: comparing _gitignore with $target_gitignore
      push_git_ignore=false
      if [ -f "$target_gitignore" ] ; then
        diff $target_gitignore ${source_path}/_gitignore >/dev/null && push_git_ignore=true
      else
        push_git_ignore=true
      fi
      echo info: push_git_ignore: $push_git_ignore
      if [ $push_git_ignore = true ] ; then
        f_exec "cp -p ${source_path}/_gitignore $target_gitignore" || return $?
        f_exec "git add .gitignore" || return $?
        f_exec "git commit -m \"Push git ignore\""
        f_exec "git push --set-upstream origin $branch"
      fi
    fi

    cd - >/dev/null 2>&1
    # return 0

    for item in $(ls -laf1 ${target_repo_path}/${project_name} | egrep -v "^\.$|^\.\.$|^\.git$") ; do
      f_exec "rm -rf \"${target_repo_path}/${project_name}/${item}\"" || return $?
    done

    f_exec "tar cvf - . | (cd ${target_repo_path}/${project_name} && tar xvf - )"
    # f_exec "cp -rp ${source_path}/* ${target_repo_path}/${project_name}" || return $?
    f_exec "cd ${target_repo_path}/${project_name}" || return $?
    f_exec git add . || return $?
    f_exec "git commit -m \"${commit_message}\""
    f_exec git push --set-upstream origin ${branch} || return $?
    cd - >/dev/null 2>&1
    echo ""
    echo "consult http://${gitlab_repo_url}/root/${project_name}/-/tree/${branch}"
    echo "consult pipelines http://${gitlab_repo_url}/root/${project_name}/-/pipelines"
    export IFS=$OLD_IFS
}

function jtable() {
  python3 /mnt/c/data/repos/my-gitlab/jtable/jtable/jtable.py "$@"
}

function gitlab_start() {
  docker compose -f /srv/local-gitlab/docker-compose.yml up -d
}
function gitlab_stop() {
  docker compose -f /srv/local-gitlab/docker-compose.yml down -t 3
}

f_tree() {
  find . -type d -print | sed -e 's;[^/]*/;|____;g;s;____|; |;g'
}

f_network_scan() {
  nmap -sn 192.168.1.0/24 | grep "^Nmap scan" | sed "s/Nmap scan report for//g"
}

secret_file=~/.${LOGNAME}_secrets.txt

if [ -f $secret_file ] ; then
  . $secret_file
fi