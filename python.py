x=eval(input("请输入需要检查的数量:"))
if x==1:
	x1=eval(input("请输入该科室到该地点的路程："))
	print("需要走的最短路径为"+str(2*x1))
elif x==2:
	x1,x2,x3=eval(input("请输入该科室到该地点的路程：(用逗号分隔)"))
	print("需要走的最短路径为"+str(x1+x2+x3))
elif x==3:
	x1,x2,x3,x4,x5,x6=eval(input("请依次输入该科室到检查1,2,3的路程以及检查1到2,3的路程和检查2和3的路程（用逗号分隔）"))
	
	print("需要走的最短路径为"+str(x1+x2+x3+x4+x5+x6))
	