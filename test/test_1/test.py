import os
import sys
#sys.path.append(os.path.abspath(__file__))

def test(File):
    if File.name !='primes.txt':
        return 'File Error !'
    destination = open(
        File.name,
        'wb+')  # 打开特定的文件进行二进制的写操作
    for chunk in File.chunks():  # 分块写入文件
        destination.write(chunk)
    destination.close()

    F = open(File.name,'r')

    lines = F.readlines()
    l = len(lines)
    if l==100 :
        if lines[-1][-3::]=='547':
            res = 1.0
        else:
            res = 'Wrong Answer !'
    else:
        res = 'Presentation Error ! lines:' + str(l)

    F.close()
    os.remove(File.name)
    return res