class Node:
    def __init__(self):
        self.children = [None] * 26     # 子节点列表
        self.isEnd = False              # 标记是否尾节点
class Trie:
    def __init__(self):
        self.root = Node()
    def insert(self, word: str) -> None:
        node = self.root      # 从根节点开始构造这个word对应的路径节点
        for char in word:
            id_ = ord(char) - ord('a') 
            if not node.children[id_]:
                node.children[id_] = Node()
            node = node.children[id_]
        node.isEnd = True # 最后一个节点的isEnd置为true，表示一个完整的字符串
    def search(self, word: str) -> bool:
        node = self.__search_prefix(word)
        return node != None and node.isEnd  # 返回不为空且节点标记为尾节点，则包含word这个完整的字符串

    def startsWith(self, prefix: str) -> bool:
        return self.__search_prefix(prefix) != None # 返回不为空，则包含了prefix前缀
    def __search_prefix(self, word: str) -> Node:
        node = self.root  # 从根节点依次开始匹配每个字符
        for char in word:
            node = node.children[ord(char) - ord('a')]  # 根节点开始构造这个word对应的路径节点
            if not node:
                return     # 只要当前节点为空，则不包含这个字符串，直接返回空指针
        return node    # 否则匹配成功返回node