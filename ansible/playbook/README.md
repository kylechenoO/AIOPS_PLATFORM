# Ansible playbook directory

## Usage

- need to add hosts to /etc/ansible/hosts
- run `ssh-keygen` to generate a public key, and run `ssh-copy-id -i ~/.ssh/id_rsa.pub root@HOST` to deploy public to HOST
- now, you can try `ssh root@HOST`, will login to the HOST directly, without password
- run `ansible-playbook cmdb.yml` in current directory, and check the directory `/AIOPS` on HOST
