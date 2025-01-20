# 1. Une première VM

🌞 Générer un Vagrantfile
```powershell
PS C:\Users\Quentin Chaillou\work\vagrant\test> ls


    Répertoire : C:\Users\Quentin Chaillou\work\vagrant\test


Mode                 LastWriteTime         Length Name
----                 -------------         ------ ----
-a----        17/01/2025     16:40           3461 Vagrantfile
```

🌞 Modifier le Vagrantfile
```
PS C:\Users\Quentin Chaillou\work\vagrant\test> cat .\Vagrantfile
# -*- mode: ruby -*-
# vi: set ft=ruby :

# All Vagrant configuration is done below. The "2" in Vagrant.configure
# configures the configuration version (we support older styles for
# backwards compatibility). Please don't change it unless you know what
# you're doing.

Vagrant.configure("2") do |config|
  config.vm.box = "generic/ubuntu2204"
  config.vm.box_version = "4.3.12"
 🌞 config.vm.box_check_update = false🌞
 🌞config.vm.synced_folder ".", "/vagrant", disabled: true🌞

  config.vm.provider 'virtualbox' do |v|
    v.gui = true
    end
end
```
🌞 Faire joujou avec une VM
```
PS C:\Users\Quentin Chaillou\work\vagrant\test> 🌞vagrant up🌞
Bringing machine 'default' up with 'virtualbox' provider...
==> default: Clearing any previously set forwarded ports...
==> default: Clearing any previously set network interfaces...
==> default: Preparing network interfaces based on configuration...
    default: Adapter 1: nat
==> default: Forwarding ports...
    default: 22 (guest) => 2222 (host) (adapter 1)
==> default: Running 'pre-boot' VM customizations...
==> default: Booting VM...
==> default: Waiting for machine to boot. This may take a few minutes...
    default: SSH address: 127.0.0.1:2222
    default: SSH username: vagrant
    default: SSH auth method: private key
==> default: Machine booted and ready!
==> default: Checking for guest additions in VM...
    default: The guest additions on this VM do not match the installed version of
    default: VirtualBox! In most cases this is fine, but in rare cases it can
    default: prevent things such as shared folders from working properly. If you see
    default: shared folder errors, please make sure the guest additions within the
    default: virtual machine match the version of VirtualBox you have installed on
    default: your host and reload your VM.
    default:
    default: Guest Additions Version: 6.1.38
    default: VirtualBox Version: 7.0
==> default: Machine already provisioned. Run `vagrant provision` or use the `--provision`
==> default: flag to force provisioning. Provisioners marked to run always will still run.



PS C:\Users\Quentin Chaillou\work\vagrant\test> 🌞vagrant status🌞
Current machine states:

default                   running (virtualbox)

The VM is running. To stop this VM, you can run `vagrant halt` to
shut it down forcefully, or you can run `vagrant suspend` to simply
suspend the virtual machine. In either case, to restart it again,
simply run `vagrant up`.
```
# 2. Repackaging
