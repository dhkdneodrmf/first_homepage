import torch  #torch를 알고 싶으면 따로 학습

x_train = torch.FloatTensor([[30],[60],[90]]) #tensor 1차원은 벡터, 2차원은 행렬 3차원 이상 텐서. gpu가 텐서 연산에 특화
y_train = torch.FloatTensor([[700],[750],[800]]) #행렬곱셈 연산
W = torch.zeros(1)  #차원에 따른 변수정의 차원을 다르게 정의하면 바꿔야함
b = torch.zeros(1) #bias는 무조건 1차원

lr = 0.0002 #learning rate 학습률

epochs = 100000 #반복횟수

len_x = len(x_train) #x학습데이터 행의 수

for epoch in range(epochs): #for문반복
  hypothesis = x_train * W + b  #h(x) 행렬계산
  cost = torch.mean((hypothesis -y_train)**2) #c(w) 행렬계산으로 비용함수 계산 

  gradient_w = torch.sum((W*x_train - y_train +b)*x_train)/ len_x #cost함수를 w에 대해 편미분진행 2나오는건 필요없음. 미분값이 정확한게 아니라 w값 찾는게 중요. 편의상 2를 지움.
  gradient_b = torch.sum((W*x_train - y_train +b))/len_x #cost함수를 b에 대해 편미분진행한값 sum이유는 나온값 배열들의 평균하려고

  W -= lr * gradient_w #봤던 수식대로 대입계산
  b -= lr * gradient_b #봤던 수식대로 대입계산
  
  if epoch % 10000 == 0: #10000번마다 for문 트래킹 하겠다는 의미
    print('Epoch {:4d}/{} W:{:.6f} b:{:.6f} Cost: {:.6f}'.format(epoch,epochs,W.item() ,b.item() , cost.item()))