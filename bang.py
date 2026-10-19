# import matplotlib.pyplot as plt

# thang = [
#     'T1', 'T2', 'T3', 'T4', 'T5', 
#     'T6', 'T7', 'T8', 'T9', 'T10*'
# ]
# doanh_thu = [
#     226271690, 198918000, 226679627, 208229080, 217662330,
#     248592000, 226040560, 250954600, 246842140, 125010200
# ]

# colors = [
#     '#4E79A7', '#F28E2B', '#E15759', '#76B7B2', '#59A14F',
#     '#EDC948', '#B07AA1', '#FF9DA7', '#9C755F', '#BAB0AC'
# ]

# plt.figure(figsize=(9, 9))
# plt.pie(
#     doanh_thu, 
#     labels=thang, 
#     autopct='%1.1f%%', 
#     startangle=90, 
#     counterclock=False, 
#     colors=colors,
#     wedgeprops={'edgecolor': 'white', 'linewidth': 1.5}
# )

# plt.title('Tỷ trọng Doanh thu theo Tháng (Năm 2026)', fontsize=14, fontweight='bold', pad=20)
# plt.tight_layout()
# plt.show()
n =int(input("Nhập: "))
tong,dem=0,0
while n !=0 :
    s = n%10
    dem+=1
    tong=tong + s
    n//=10
print("Tổng là : ",tong)
print("Đếm là : ",dem)

trai_cay = ['táo', 'chuối', 'cam']
for i in range(len(trai_cay)):
    print(i, trai_cay[i])
trai_cay = ['táo', 'chuối', 'cam']
for i, ten in enumerate(trai_cay):
    print(i, ten) 
## enumerate vừa lấy dữ liệu vừa đnahs số


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










### oop
class preser:
    nasion ='Viet Nam'
    def __init__(self,name,job):
        self.name=name #pulic
        self.__job =job # priver
    def get_job(self):
        return self.__job
    def set_job(self,job):
        self.__job=job
    def set_name(self,name):
        self.name=name
    def __str__(self):
        return f'{self.name}/{self.__job}'
if __name__ == '__main__':
    a=preser('dung','studen')
    # print(a.get_job())
    a.set_job('dev')
    print(a.get_job())
