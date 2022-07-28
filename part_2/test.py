import torch

before = torch.tensor([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(id(before))  # 2175310194816
x = torch.ones_like(before)
before = before + x  # 会重新指向新的地址，增加内存消耗
print(id(before))  # 2175309926976

# 改进方法，使用切⽚表⽰法将操作的结果分配给先前分配的数组
before[:] = before + x
print(id(before))  # 2175310194816

# 对象间的相互转化
# Tensor --> ndarray
A = before.numpy()

# ndarray --> Tensor
B = torch.tensor(A)

# 单个元素的Tensor --> 标量
C = torch.tensor([33.01])
C.item()  # 33.01
