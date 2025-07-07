## json_query


```yaml
- hosts: localhost
  gather_facts: no
  vars:
    the_title: bob
    dataset:
      cluster_1:
      - { hostname: joe, os: linux, cost: 5000, state: alive }
      - { hostname: john, os: linux, cost: 200, state: alive }
      - { hostname: roger, os: windows, cost: 200, state: alive }
      - { hostname: elton, os: windows, cost: 5000, state: decom }
      cluster_2:
      - { hostname: pomme, os: linux, cost: 5000, state: alive }
      - { hostname: orange, os: linux, cost: 200, state: alive }
      - { hostname: figue, os: windows, cost: 200, state: alive }
      - { hostname: fraise, os: windows, cost: 5000, state: decom }
  tasks:

  - debug:
      msg: "{{ dataset | json_query('*[?cost > `200`] | [].hostname') }}"

  - debug:
      msg:  "{{ dataset | json_query('*[?cost > `200`].{hostname: hostname, os: os} | []' ) }}"



```


## ad-hoc command with var

```bash
ansible -c local -m debug -e name=vince -a 'msg={{ "Hello " +  name }}' localhost
```

## ad-hoc template command with var

```bash
ansible -c local -m template -e jtable_version=0.9.12 -a 'src=./conf.template.j2 dest=conf_testing.yml' localhost
```