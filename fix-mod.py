#!/usr/bin/env python3

import os

# 从一个文件中，每次读取一行。如果这一行以diff --git 开头，
# 那么从这个格式中："diff --git a/filename b/filename",把filename提取出来。
diff_file = open('diff.txt', 'r')
# diff_file = os.popen('git diff --diff-filter=d').readlines()

for line in diff_file:
    line = line.strip()

    if line.startswith('diff --git'):

        filename = line.split(' ')[2]

        # 现在的文件名是 a/arch/arm64/kvm/hyp/proxy.c 这样的形式，把前面的 'a/' 去掉
        filename = filename[2:]

        print("\n\nfilename=", filename)

        # 然后在下面继续读取，如果找到 old mode 100644 这种格式，就把 100644 提取出来， mod=100644
        # 然后执行 chmod mod filename
        line = diff_file.readline().strip()
        if line.startswith('old mode'):
            print("old mode= ", line)
            mod = line.split(' ')[2]
            mod = mod[3:]
            cmd = 'chmod ' + mod + ' ' + filename

            print("cmd=", cmd)
            os.system(cmd)
