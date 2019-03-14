import shutil
from collections import namedtuple
from ansible.parsing.dataloader import DataLoader
from ansible.vars.manager import VariableManager
from ansible.inventory.manager import InventoryManager
from ansible.playbook.play import Play
from ansible.executor.task_queue_manager import TaskQueueManager
import ansible.constants as C


# 设置ansbile选项 ansible --help
# connetion -> local 表示本地执行 ssh smart
# moudle_path 指定模块路径
# forks值嗯的是一次花簇昂件多少个子进程
# check 尝运行
# diff用于显示改变了什么
Options = namedtuple('Options', ['connection', 'module_path', 'forks',
                                 'become', 'become_method', 'become_user', 'check', 'diff'])
options = Options(connection='smart', module_path=['/to/mymodules'], forks=10,
                  become=None, become_method=None, become_user=None, check=False, diff=False)

# loader用于查找和分析yaml， json, 和 ini 文件
loader = DataLoader()
# passwords用于设置各种各样的密码
passwords = dict(vault_pass='secret')

# 指定主机清单，有两种方式，一种是用逗号分隔开各台主机，另一种是文件列表
# inventory = InventoryManager(loader=loader, sources='localhost,')
inventory = InventoryManager(loader=loader, sources='/etc/ansible/hosts')

# VariableManager用于管理变量
variable_manager = VariableManager(loader=loader, inventory=inventory)

# 定义一个playbook
play_source = dict(
        name="Ansible Play",
        hosts='db',
        gather_facts='no',
        tasks=[
            dict(action=dict(module='yum', args='name=vsftpd state=latest'))
            # dict(action=dict(module='shell', args='ls'), register='shell_out'),
            # dict(action=dict(module='debug', args=dict(msg='{{shell_out.stdout}}')))
         ]
    )

# 创建play对象,将前面的对象组合到play中
play = Play().load(play_source, variable_manager=variable_manager, loader=loader)

# 运行，创建任务对类管理器，用与管理将要执行任务
tqm = None
try:
    tqm = TaskQueueManager(
              inventory=inventory,
              variable_manager=variable_manager,
              loader=loader,
              options=options,
              passwords=passwords,
          )
    result = tqm.run(play)
finally:
    if tqm is not None:
        tqm.cleanup()  # 清理任务

    # Remove ansible tmpdir
    # 删除临时目录
    shutil.rmtree(C.DEFAULT_LOCAL_TMP, True)