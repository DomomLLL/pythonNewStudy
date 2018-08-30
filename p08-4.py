class my_open():
    def __init__(self, path, mod):
        self.path = path
        self.mod = mod
    def __enter__(self):
        try:
            self.file_now = open(self.path,self.mod)
            print('ads')
        except FileNotFoundError:
            print('文件不存在')
        return self.file_now
    def __exit__(self, e, m, d):
            print('over')
with my_open('/mnt/share/p.py', 'r') as f1:
    print('777')
    print(f1.read())
