import torch
import torch.nn as nn
import torch.nn.functional as F

my_network = nn.Sequential(
    nn.Conv2d(1,  32, kernel_size=3, padding=2, stride=2)
    # nn.Conv2d(32, 32, kernel_size=3, padding=2, stride=1)
)

x = torch.Tensor([[ [[1,2,3,4,5,6,7,8,9,10],
                     [1,2,3,4,5,6,7,8,9,10],
                     [1,2,3,4,5,6,7,8,11,15],
                     [1,2,3,4,5,6,7,8,9,10],
                     [1,2,3,4,5,6,7,8,9,10],
                     [1,2,3,4,5,6,7,8,9,10],
                     [1,2,3,4,5,6,7,8,9,10],
                     [1,2,3,4,5,6,7,8,9,10],
                     [1,2,3,4,5,6,7,8,9,10],
                     [1,2,3,4,5,6,7,8,9,10]] ]])

w = torch.Tensor( [[[[-1,0,1],
                     [-1,0,1],
                     [-1,0,1]]]] )


result = F.conv2d(x,w,stride=2,padding=0)
print(result)
print(result.shape)

# y_pred = my_network(x)
# print(y_pred)