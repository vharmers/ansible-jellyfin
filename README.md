Jellyfin
=========

[Jellyfin](https://jellyfin.org) is a free media solution. This Ansible role will allow you to install it on your Debian based systems.

Requirements
------------

This role has no additional requirements.

Role Variables
--------------

| Variable | Default | Description |
| -------- | ------- | ----------- |
| jellyfin_enabled | yes | Controls whenever the Jellyfin service should be running and started at boot |
| jellyfin_service | `"jellyfin"` | The name of the service |
| jellyfin_package | `"jellyfin"` | The name of the package to install |
| jellyfin_repo | `"repo.jellyfin.org"` | The domain of the repository to use |

Role Tags
---------

| Tag | Description |
| --- | ----------- |
| jellyfin-install | Runs installation tasks such as installing packages, creating users and groups and installing service files |
| jellyfin-configure | Runs configuration tasks such as creating configuration directories and files |
| jellyfin-validate | Runs tasks that validate the variables and system configuration and ensures that the role can be properly deployed |
| install | Global install tag. Allows you to easily run the installation tasks on a multitude of compatible roles |
| configure | Global configure tag. Allows you to easily run the configuration tasks on a multitude of compatible roles |
| validate | Global validate tag. Allows you to easily run the validation tasks on a multitude of compatible roles |

Dependencies
------------

This role has no dependencies.

Example Playbook
----------------

```yaml
- hosts: all
  roles:
    - vharmers.jellyfin
  vars:
    jellyfin_enabled: no  # Install and configure but don't start the service yet
```

Testing
-------

Testing is done with [Molecule](https://molecule.readthedocs.io/en/latest/) and [Vagrant](https://www.vagrantup.com).

**Step 1:** Install a hypervisor such as [VirtualBox](https://www.virtualbox.org).

**Step 2:** Install Vagrant. Follow the installation instructions for your OS on the [downloads](https://www.vagrantup.com/downloads) page.

**Step 3:** Install the necessary Python packages:

```bash
pip install ansible ansible-lint molecule molecule_vagrant pytest-testinfra
```

**Step 4:** Descent into the role directory and run the `molecule test` command.

License
-------

[MIT](LICENSE)

Author Information
------------------

*Valentijn Harmers* ([website](https://www.vharmers.com))
