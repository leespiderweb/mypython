#test.py
import time

scale = 50

print("打印开始".center(scale//2,'-'))
t =  time.clock()

for i  in  range(scale+1):
    a,b = "*" * i, "." * (scale -i)
    c = i/(scale+1)*100
    #c = (c+(1-c)**0.03)**2
    t-= time.clock()

    print("\r{:^3.0f}%, [{} ->{}]  {:.2f}s ".format(c,a,b,-t) ,end="")
    time.sleep(0.05)


print("\n"+"打印结束".center(scale//2,"-"))
print("test of  test.py in  branch test")
