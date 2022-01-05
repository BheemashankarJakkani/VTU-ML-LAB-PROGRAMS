import numpy as np

X=np.array(([2,9],[1,5],[3,6]),dtype=float)
y=np.array(([92],[86],[89]),dtype=float)

X=X/np.amax(X,axis=0)
y=y/100


epoch=7000
lr=0.1
input_layer_neuron=2
hidden_neuron=3
op_neuron=1



wh=np.random.uniform(size=(input_layer_neuron,hidden_neuron))
bh=np.random.uniform(size=(1,hidden_neuron))
wout=np.random.uniform(size=(hidden_neuron,op_neuron))
bout=bh=np.random.uniform(size=(1,op_neuron))

def sigmoid(x):
    return x/(1+np.exp(-x))

def derivative_sigmoid(x):
    return x*(1-x)


for i in range(epoch):
    hinp1=np.dot(X,wh)
    hinp=hinp1+bh
    hlayer_act=sigmoid(hinp)
    outinp1=np.dot(hlayer_act,wout)
    outinp=outinp1+bout
    output=sigmoid(outinp)
    #Backpropogation
    EO=y-output
    d_grad=derivative_sigmoid(output)
    d_output=EO*d_grad
    EH=d_output.dot(wout.T)
    h_grad=derivative_sigmoid(hlayer_act)
    h_output=EH*h_grad
    wout+=hlayer_act.T.dot(d_output)*lr
    #bout+=np.sum(d_output,axis=0,keepdims=True)*lr
    wh+=X.T.dot(h_output)*lr    
    

print("Input: \n"+str(X))
print("Actual output :\n"+str(y))
print("Predicted output: \n",output)

