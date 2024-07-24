## json_query


### Ansible playbook sample

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