
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
##--> làm ra một cái node để chứa 1 danh sách liên kết

## --> làm danh sách liên kết
class linked_list:
    def __init__(self):
        self.head=None


### --> thêm vào đầu tàu

    def them_vao_dau(self,data):
        new_Node = Node(data)
        new_Node.next = self.head
        self.head = new_Node
    

if __name__ == '__main__':
    a =linked_list()
    a.them_vao_dau(20)
    a.them_vao_dau(10)
    a.them_vao_dau(6)
    cur = a.head
    while cur is not None:
        print(f"[{cur.data}]", end=" ---> ")
        cur = cur.next
    print(None)
