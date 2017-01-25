# Perspective Ansible Inventory File
This repository contains a dynamic inventory file for [Ansible](http://ansible.com/) configuration management system. It allows you to apply your playbooks and commands always to the latest cloud state of all your cloud projects.

## Installation
Just copy ```perspective-inventory``` file from this repository somewhere on your filesystem or install it with ```pip```: 

```$ pip install perspective-ansible```

## Configuration
You only need to specify Perspective API connection settings in ```~/.ansible/perspective.json```:
```
$ cat ~/.ansible/perspective.json
{
    "url": "http://example.com/"
}
```

## Usage
Use Ansible ```-i``` flag to specify custom inventory file:
```
$ ansible ~test-vm.* -i /path/to/perspective-inventory -m ping
```
Alternatively you can specify path to inventory file in Ansible configuration file:
```
$ cat /etc/ansible/ansible.cfg
[defaults]
inventory = /path/to/perspective-inventory
```
