# init password
```
read password
read gitlab_instance

docker exec -ti ${gitlab_instance} bash -c "gitlab-rake 'gitlab:password:reset[root]'<<EOF
${password}
${password}
EOF"
```



# API

## list projects

```bash
curl http://my-gitlab/api/v4/projects/
```

## list pipelines

Pour lister les pipelines d'un projet spécifique :

```bash
curl -H "PRIVATE-TOKEN: ${GITLAB_TOKEN}" "http://my-gitlab/api/v4/projects/${project_id}/pipelines"
```

## Get job traces

```bash
/api/v4/projects/{project_id}/jobs/{job_id}/trace
```


