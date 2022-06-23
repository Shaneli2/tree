# 这是一个示例 Python 脚本。

# 按 Shift+F10 执行或将其替换为您的代码。
# 按 双击 Shift 在所有地方搜索类、文件、工具窗口、操作和设置。

# 先定义一个类表示节点
class Node(object):
    def __init__(self, data, left=None, right=None):
        self.data, self.left, self.right = data, left, right


# root 节点是入口，定义一个 二叉树, 这就构造了一棵二叉树对象
class Tree(object):
    def __init__(self, root=None):
        self.root = root

    def install_data(self, node_list): # basing on node_list to build the tree
        node_dict = {}
        for n in node_list:
            node = Node(n['data'], n['left'], n['right'])
            node_dict[n['data']] = node

        for n in node_list:
            node = node_dict[n['data']]
            if node.left:
                node.left = node_dict[node.left]
            if node.right:
                node.right = node_dict[node.right]
            if n['is_root']:
                self.root = node

    # 二叉树递归遍历，用递归的方式来遍历
    def iter_node1(self, node):
        if node is not None:
            print(node.data)
            self.iter_node1(node.left)
            self.iter_node1(node.right)

    #二叉树层序遍历，层序遍历就是从根节点开始按照一层一层的方式遍历节点
    def iter_node2(self, node):
        node_list = [node]

        for node in node_list:
            print(node.data)
            if node.left:
                node_list.append(node.left)
            if node.right:
                node_list.append(node.right)

    #反转二叉树，就是将根节点下的子节点左右互换即可
    def reverse(self, subtree):
        if subtree is not None:
            subtree.left, subtree.right = subtree.right, subtree.left
            self.reverse(subtree.left)
            self.reverse(subtree.right)


def print_hi(name):
    # 在下面的代码行中使用断点来调试脚本。
    print(f'Hi, {name}')  # 按 Ctrl+F8 切换断点。

# 定义node_list，只有一个根节点
node_list = [
    {'data': 'A', 'left': 'B', 'right': 'C', 'is_root': True},
    {'data': 'B', 'left': 'D', 'right': 'E', 'is_root': False},
    {'data': 'D', 'left': None, 'right': None, 'is_root': False},
    {'data': 'E', 'left': 'H', 'right': None, 'is_root': False},
    {'data': 'H', 'left': None, 'right': None, 'is_root': False},
    {'data': 'C', 'left': 'F', 'right': 'G', 'is_root': False},
    {'data': 'F', 'left': None, 'right': None, 'is_root': False},
    {'data': 'G', 'left': 'I', 'right': 'J', 'is_root': False},
    {'data': 'I', 'left': None, 'right': None, 'is_root': False},
    {'data': 'J', 'left': None, 'right': None, 'is_root': False},
]

# 按间距中的绿色按钮以运行脚本。
if __name__ == '__main__':
    # print_hi('PyCharm')
    node = Node(None)
    mytree = Tree(node)
    mytree.install_data(node_list)
    print("xxxx1")
    mytree.iter_node1(mytree.root)
    print("xxxx2")
    mytree.iter_node2(mytree.root)

# 访问 https://www.jetbrains.com/help/pycharm/ 获取 PyCharm 帮助
