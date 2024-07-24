# init password
```
read password
read gitlab_instance

docker exec -ti ${gitlab_instance} bash -c "gitlab-rake 'gitlab:password:reset[root]'<<EOF
${password}
${password}
EOF"
```