#!/usr/bin/env python
from pyVim.connect import SmartConnect, Disconnect
from pyVmomi import vim, vmodl
import ssl
import atexit

host = '名前解決ができるvCenterのホスト名またはIPアドレスに変更'
username = 'vCenterのアカウントに変更'
password = '上記パスワードに変更'
vm_name = 'instanceUuidを取得したいVM名'
mob = vim.VirtualMachine

if __name__ == "__main__":
    context = None
    if hasattr(ssl, '_create_unverified_context'):
        context = ssl._create_unverified_context()

    si = SmartConnect(host=host,
                      user=username,
                      pwd=password,
                      sslContext=context)

    atexit.register(Disconnect, si)

    content = si.content

    mob_list = content.viewManager.CreateContainerView(content.rootFolder,
                                                       [mob],
                                                       True)

    for mob in mob_list.view:
        if mob.name == vm_name:
            print(mob.config.instanceUuid)
