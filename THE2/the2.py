a = eval(input())
v0 = a[0]
v1 = a[1]
v2 = a[2]
v3 = a[3]

x0 = v0[0]
y0 = abs(v0[1])
x1 = v1[0]
y1 = abs(v1[1])
x2 = v2[0]
y2=  abs(v2[1])
x3=  v3[0]
y3=  abs(v3[1]) 

b=[x0,x1,x2,x3]
c=[y0,y1,y2,y3]
g=[y2,y0]
f=[y1,y3]
n=[y1,y2]
m=[y0,y1]
l=[y0,y3]
k=[y2,y3]
#equality of x's condition-area of trapezoid minus quadrilateral
if (x0==x3 and x1==x2) and (max(c)==y3 or max(c)==y2) and (min(c)==y0 or min(c)==y1):
 print("%.2f" %(((y0+y1)/2)*abs(x1-x0)))
elif (x0==x3 and x1==x2) and (max(c)==y1 or max(c)==y0) and (min(c)==y2 or min(c)==y3):
 print("%.2f" %(((y2+y3)/2)*abs(x1-x0)))
elif (x0==x1 and x3==x2) and (max(c)==y3 or max(c)==y0) and (min(c)==y2 or min(c)==y1):
 print("%.2f" %(((y2+y1)/2)*abs(x2-x0)))
elif (x0==x1 and x3==x2) and (max(c)==y2 or max(c)==y1) and (min(c)==y0 or min(c)==y3):
 print("%.2f" %(((y0+y3)/2)*abs(x2-x0)))





elif x1==x3 and min(b)==x0 and max(b)==x1 and max(c)==y0 and min(c)==y3: 
 print("%.2f" %(((y0+y3)/2)*abs(x1-x0)))
elif x1==x3 and min(b)==x0 and max(b)==x1 and max(c)==y0 and min(c)==y1:
 print("%.2f" %(((y0+y1)/2)*abs(x1-x0)))
elif x1==x3 and min(b)==x0 and max(b)==x1 and max(c)==y1 and min(c)==y0:
 print("%.2f" %(((y0+y3)/2)*abs(x1-x0)))
elif x1==x3 and min(b)==x0 and max(b)==x1 and max(c)==y3 and min(c)==y0:
 print("%.2f" %(((y0+y1)/2)*abs(x1-x0)))
elif x1==x3 and min(b)==x1 and max(b)==x0 and max(c)==y0 and min(c)==y1:
 print("%.2f" %(((y0+y1)/2)*abs(x1-x0))) 
elif x1==x3 and min(b)==x1 and max(b)==x0 and max(c)==y0 and min(c)==y3:
 print("%.2f" %(((y0+y3)/2)*abs(x1-x0)))
elif x1==x3 and min(b)==x1 and max(b)==x0 and max(c)==y1 and min(c)==y0:
 print("%.2f" %(((y0+y3)/2)*abs(x1-x0)))
elif x1==x3 and min(b)==x1 and max(b)==x0 and max(c)==y3 and min(c)==y0:
 print("%.2f" %(((y0+y1)/2)*abs(x1-x0)))

elif x1==x3 and min(b)==x2 and max(b)==x1 and max(c)==y2 and min(c)==y3:
 print("%.2f" %(((y2+y3)/2)*abs(x2-x1))) 
elif x1==x3 and min(b)==x2 and max(b)==x1 and max(c)==y2 and min(c)==y1:
 print("%.2f" %(((y2+y1)/2)*abs(x2-x1)))
elif x1==x3 and min(b)==x2 and max(b)==x1 and max(c)==y3 and min(c)==y2: 
 print("%.2f" %(((y2+y1)/2)*abs(x2-x1)))
elif x1==x3 and min(b)==x2 and max(b)==x1 and max(c)==y1 and min(c)==y2:
 print("%.2f" %(((y2+y3)/2)*abs(x2-x1)))
elif x1==x3 and min(b)==x1 and max(b)==x2 and max(c)==y2 and min(c)==y3:
 print("%.2f" %(((y2+y3)/2)*abs(x2-x1)))
elif x1==x3 and min(b)==x1 and max(b)==x2 and max(c)==y2 and min(c)==y1:
 print("%.2f" %(((y2+y1)/2)*abs(x2-x1)))
elif x1==x3 and min(b)==x1 and max(b)==x2 and max(c)==y1 and min(c)==y2:
 print("%.2f" %(((y2+y3)/2)*abs(x2-x1)))
elif x1==x3 and min(b)==x1 and max(b)==x2 and max(c)==y3 and min(c)==y2:
 print("%.2f" %(((y2+y1)/2)*abs(x2-x1)))

elif x2==x0 and min(b)==x0 and max(b)==x1 and max(c)==y1 and min(c)==y0:
 print("%.2f" %(((y0+y1)/2)*abs(x2-x0)))
elif x2==x0 and min(b)==x0 and max(b)==x1 and max(c)==y1 and min(c)==y2:
 print("%.2f" %(((y2+y0)/2)*abs(x2-x0)))
elif x2==x0 and min(b)==x0 and max(b)==x1 and max(c)==y2 and min(c)==y1: 
 print("%.2f" %(((y2+y1)/2)*abs(x2-x0)))
elif x2==x0 and min(b)==x0 and max(b)==x1 and max(c)==y0 and min(c)==y1:
 print("%.2f" %(((y2+y1)/2)*abs(x2-x0)))

elif x2==x0 and min(b)==x1 and max(b)==x0 and max(c)==y1 and min(c)==y2: 
 print("%.2f" %(((y2+y1)/2)*abs(x2-x0)))

elif x2==x0 and min(b)==x1 and max(b)==x0 and max(c)==y1 and min(c)==y0:
 print("%.2f" %(((y0+y1)/2)*abs(x2-x0)))

elif x2==x0 and min(b)==x1 and max(b)==x0 and max(c)==y2 and min(c)==y1:
 print("%.2f" %(((y0+y1)/2)*abs(x2-x0)))

elif x2==x0 and min(b)==x1 and max(b)==x0 and max(c)==y0 and min(c)==y1:
 print("%.2f" %(((y2+y1)/2)*abs(x2-x0)))


elif x2==x0 and min(b)==x3 and max(b)==x2 and max(c)==y3 and min(c)==y0: 
 print("%.2f" %(((y0+y3)/2)*abs(x3-x2)))

elif x2==x0 and min(b)==x3 and max(b)==x2 and max(c)==y3 and min(c)==y2:
 print("%.2f" %(((y2+y3)/2)*abs(x2-x3)))

elif x2==x0 and min(b)==x3 and max(b)==x2 and max(c)==y0 and min(c)==y3: 
 print("%.2f" %(((y2+y3)/2)*abs(x2-x3)))

elif x2==x0 and min(b)==x3 and max(b)==x2 and max(c)==y2 and min(c)==y3:
 print("%.2f" %(((y0+y3)/2)*abs(x2-x3)))

elif x2==x0 and min(b)==x2 and max(b)==x3 and max(c)==y3 and min(c)==y0: 
 print("%.2f" %(((y0+y3)/2)*abs(x2-x3)))

elif x2==x0 and min(b)==x2 and max(b)==x3 and max(c)==y3 and min(c)==y2:
 print("%.2f" %(((y2+y3)/2)*abs(x2-x3)))

elif x2==x0 and min(b)==x2 and max(b)==x3 and max(c)==y2 and min(c)==y3:
 print("%.2f" %(((y0+y3)/2)*abs(x2-x3)))

elif x2==x0 and min(b)==x2 and max(b)==x3 and max(c)==y0 and min(c)==y3:
 print("%.2f" %(((y2+y3)/2)*abs(x2-x3)))

  


#quadrilateral condition when x's are different 
elif (max(b)==x0 and min(b)==x1) and (max(c)==y3 or max(c)==y2) and (min(c)==y0 or min(c)==y1):
 print("%.2f" %((x0-x1)*((y0+y1)/2)))
elif (max(b)==x1 and min(b)==x0) and (max(c)==y3 or max(c)==y2) and (min(c)==y0 or min(c)==y1):
 print("%.2f" %((x1-x0)*((y0+y1)/2)))
elif (max(b)==x1 and min(b)==x2) and (max(c)==y3 or max(c)==y0)  and (min(c)==y1 or min(c)==y2):
 print("%.2f" %((x1-x2)*((y1+y2)/2)))
elif (max(b)==x2 and min(b)==x1) and (max(c)==y3 or max(c)==y0)  and (min(c)==y1 or min(c)==y2):
 print("%.2f" %((x2-x1)*((y1+y2)/2)))
#quadrilateral which extends inward(trapezoid+triangle)
elif (max(b)==x0 and min(b)==x2) and (max(c)==y3)  and (min(c)!=y1) and (min(c)==y0 or min(c)==y2):
 print("%.2f" %(((x0-x2)*((y2+y0)/2))+(abs((x0*y1)+(x1*y2)+(x2*y0)-(x1*y0)-(x2*y1)-(x0*y2))/2)))
elif (max(b)==x0 and min(b)==x2) and (max(c)==y1)  and (min(c)!=y3) and (min(c)==y0 or min(c)==y2):
 print("%.2f" %(((x0-x2)*((y2+y0)/2))+(abs((x0*y2)+(x2*y3)+(x3*y0)-(x2*y0)-(x3*y2)-(x0*y3))/2)))
elif (max(b)==x2 and min(b)==x0) and (max(c)==y3)  and (min(c)!=y1) and (min(c)==y0 or min(c)==y2):
 print("%.2f" %(((x2-x0)*((y0+y2)/2))+(abs((x0*y1)+(x1*y2)+(x2*y0)-(x1*y0)-(x2*y1)-(x0*y2))/2)))
elif (max(b)==x2 and min(b)==x0) and (max(c)==y1) and (min(c)!=y3)  and (min(c)==y0 or min(c)==y2):
 print("%.2f" %(((x2-x0)*((y0+y2)/2))+(abs((x0*y2)+(x2*y3)+(x3*y0)-(x2*y0)-(x3*y2)-(x0*y3))/2)))
#quadrilateral condition(rest of it)
elif (max(b)==x0 and min(b)==x3) and (max(c)==y2 or max(c)==y1)  and (min(c)==y0 or min(c)==y3):
 print("%.2f" %((x0-x3)*((y0+y3)/2)))
elif (max(b)==x3 and min(b)==x0) and (max(c)==y2 or max(c)==y1)  and (min(c)==y0 or min(c)==y3):
 print("%.2f" %((x3-x0)*((y0+y3)/2)))
elif (max(b)==x3 and min(b)==x2) and (max(c)==y0 or max(c)==y1)  and (min(c)==y3 or min(c)==y2):
 print("%.2f" %((x3-x2)*((y3+y2)/2)))
elif (max(b)==x2 and min(b)==x3) and (max(c)==y0 or max(c)==y1)  and (min(c)==y3 or min(c)==y2):
 print("%.2f" %((x2-x3)*((y2+y3)/2)))
#quadrilateral which extends inward(trapezoid+triangle)(rest of it)
elif (max(b)==x1 and min(b)==x3) and (max(c)==y0) and (min(c)!=y2) and (min(c)==y1 or min(c)==y3):
 print("%.2f" %(((x1-x3)*((y1+y3)/2))+(abs((x1*y2)+(x2*y3)+(x3*y1)-(x2*y1)-(x3*y2)-(x1*y3))/2)))
elif (max(b)==x1 and min(b)==x3) and (max(c)==y2) and (min(c)!=y0) and (min(c)==y1 or min(c)==y3):
 print("%.2f" %(((x1-x3)*((y1+y3)/2))+(abs((x0*y1)+(x1*y3)+(x3*y0)-(x1*y0)-(x3*y1)-(x0*y3))/2)))
elif (max(b)==x3 and min(b)==x1) and (max(c)==y0) and (min(c)!=y2) and (min(c)==y1 or min(c)==y3):
 print("%.2f" %(((x3-x1)*((y3+y1)/2))+(abs((x1*y2)+(x2*y3)+(x3*y1)-(x2*y1)-(x3*y2)-(x1*y3))/2)))
elif (max(b)==x3 and min(b)==x1) and (max(c)==y2) and (min(c)!=y0) and (min(c)==y1 or min(c)==y3):
 print("%.2f" %(((x3-x1)*((y3+y1)/2))+(abs((x0*y1)+(x1*y3)+(x3*y0)-(x1*y0)-(x3*y1)-(x0*y3))/2)))
#quadrilateral which extend outward(trapezoid-triangle which is downward)
elif (max(b)==x0 and min(b)==x2) and (max(c)==y3 and min(c)==y1):
 print("%.2f" %(((x0-x2)*((y0+y2)/2))-(abs((x0*y1)+(x1*y2)+(x2*y0)-(x1*y0)-(x2*y1)-(x0*y2))/2)))
elif (max(b)==x0 and min(b)==x2) and (max(c)==y1 and min(c)==y3):
 print("%.2f" %(((x0-x2)*((y0+y2)/2))-(abs((x0*y2)+(x2*y3)+(x3*y0)-(x2*y0)-(x3*y2)-(x0*y3))/2)))
elif (max(b)==x2 and min(b)==x0) and (max(c)==y3 and min(c)==y1):
 print("%.2f" %(((x2-x0)*((y0+y2)/2))-(abs((x0*y1)+(x1*y2)+(x2*y0)-(x1*y0)-(x2*y1)-(x0*y2))/2)))
elif (max(b)==x2 and min(b)==x0) and (max(c)==y1 and min(c)==y3):
 print("%.2f" %(((x2-x0)*((y0+y2)/2))-(abs((x0*y2)+(x2*y3)+(x3*y0)-(x2*y0)-(x3*y2)-(x0*y3))/2)))
elif (max(b)==x1 and min(b)==x3) and (max(c)==y2 and min(c)==y0):
 print("%.2f" %(((x1-x3)*((y1+y3)/2))-(abs((x0*y1)+(x1*y3)+(x3*y0)-(x1*y0)-(x3*y1)-(x0*y3))/2)))
elif (max(b)==x1 and min(b)==x3) and (max(c)==y0 and min(c)==y2):
 print("%.2f" %(((x1-x3)*((y1+y3)/2))-(abs((x1*y2)+(x2*y3)+(x3*y1)-(x2*y1)-(x3*y2)-(x1*y3))/2)))
elif (max(b)==x3 and min(b)==x1) and (max(c)==y2 and min(c)==y0):
 print("%.2f" %(((x3-x1)*((y1+y3)/2))-(abs((x0*y1)+(x1*y3)+(x3*y0)-(x1*y0)-(x3*y1)-(x0*y3))/2)))
elif (max(b)==x3 and min(b)==x1) and (max(c)==y0 and min(c)==y2):
 print("%.2f" %(((x1-x3)*((y1+y3)/2))-(abs((x1*y2)+(x2*y3)+(x3*y1)-(x2*y1)-(x3*y2)-(x1*y3))/2)))
 #trapezoid-quadrilateral 
elif (max(b)==x0 and min(b)==x1) and (max(c)==y0 or max(c)==y1):
 print("%.2f" %(((x0-x1)*((y0+y1)/2))-(abs((x0*y1-y0*x1)+(x1*y2-y1*x2)+(x2*y3-y2*x3)+(x3*y0-y3*x0))/2)))
elif max(b)==x1 and min(b)==x0 and (max(c)==y1 or max(c)==y0):
 print("%.2f" %(((x1-x0)*((y0+y1)/2))-(abs((x0*y1-y0*x1)+(x1*y2-y1*x2)+(x2*y3-y2*x3)+(x3*y0-y3*x0))/2)))
elif (max(b)==x1 and min(b)==x2) and (max(c)==y1 or max(c)==y2):
 print("%.2f" %(((x1-x2)*((y1+y2)/2))-(abs((x0*y1-y0*x1)+(x1*y2-y1*x2)+(x2*y3-y2*x3)+(x3*y0-y3*x0))/2)))
elif (max(b)==x2 and min(b)==x1) and (max(c)==y1 or max(c)==y2):
 print("%.2f" %(((x2-x1)*((y1+y2)/2))-(abs((x0*y1-y0*x1)+(x1*y2-y1*x2)+(x2*y3-y2*x3)+(x3*y0-y3*x0))/2)))
#trapezoid-bigger triangle
elif (max(b)==x0 and min(b)==x2) and (max(c)==y0 or max(c)==y2) and min(f)==y1:
 print("%.2f" %(((x0-x2)*((y2+y0)/2))-(abs((x0*y1)+(x1*y2)+(x2*y0)-(x1*y0)-(x2*y1)-(x0*y2))/2)))
elif (max(b)==x0 and min(b)==x2) and (max(c)==y0 or max(c)==y2) and min(f)==y3:
 print("%.2f" %(((x0-x2)*((y2+y0)/2))-(abs((x0*y2)+(x2*y3)+(x3*y0)-(x2*y0)-(x3*y2)-(x0*y3))/2)))
elif (max(b)==x2 and min(b)==x0) and (max(c)==y0 or max(c)==y2) and min(f)==y3:
 print("%.2f" %(((x2-x0)*((y0+y2)/2))-(abs((x0*y2)+(x2*y3)+(x3*y0)-(x2*y0)-(x3*y2)-(x0*y3))/2)))
elif (max(b)==x2 and min(b)==x0) and (max(c)==y0 or max(c)==y2) and min(f)==y1:
 print("%.2f" %(((x2-x0)*((y2+y0)/2))-(abs((x0*y1)+(x1*y2)+(x2*y0)-(x1*y0)-(x2*y1)-(x0*y2))/2)))
 #trapezoid-quadrilateral
elif (max(b)==x0 and min(b)==x3) and  (max(c)==y0 or max(c)==y3):
 print("%.2f" %(((x0-x3)*((y0+y3)/2))-(abs((x0*y1-y0*x1)+(x1*y2-y1*x2)+(x2*y3-y2*x3)+(x3*y0-y3*x0))/2)))
elif (max(b)==x3 and min(b)==x0) and  (max(c)==y0 or max(c)==y3):
 print("%.2f" %(((x3-x0)*((y0+y3)/2))-(abs((x0*y1-y0*x1)+(x1*y2-y1*x2)+(x2*y3-y2*x3)+(x3*y0-y3*x0))/2)))
elif (max(b)==x3 and min(b)==x2) and  (max(c)==y3 or max(c)==y2):
 print("%.2f" %(((x3-x2)*((y3+y2)/2))-(abs((x0*y1-y0*x1)+(x1*y2-y1*x2)+(x2*y3-y2*x3)+(x3*y0-y3*x0))/2)))
elif (max(b)==x2 and min(b)==x3) and  (max(c)==y3 or max(c)==y2):
 print("%.2f" %(((x2-x3)*((y2+y3)/2))-(abs((x0*y1-y0*x1)+(x1*y2-y1*x2)+(x2*y3-y2*x3)+(x3*y0-y3*x0))/2)))
#trapezoid-bigger triangle
elif (max(b)==x1 and min(b)==x3) and  (max(c)==y1 or max(c)==y3) and min(g)==y2:
 print("%.2f" %(((x1-x3)*((y1+y3)/2))-(abs((x1*y2)+(x2*y3)+(x3*y1)-(x2*y1)-(x3*y2)-(x1*y3))/2)))
elif (max(b)==x1 and min(b)==x3) and  (max(c)==y1 or max(c)==y3) and min(g)==y0:
 print("%.2f" %(((x1-x3)*((y1+y3)/2))-(abs((x0*y1)+(x1*y3)+(x3*y0)-(x1*y0)-(x3*y1)-(x0*y3))/2)))
elif (max(b)==x3 and min(b)==x1) and  (max(c)==y1 or max(c)==y3) and min(g)==y2:
 print("%.2f" %(((x3-x1)*((y3+y1)/2))-(abs((x1*y2)+(x2*y3)+(x3*y1)-(x2*y1)-(x3*y2)-(x1*y3))/2)))
elif (max(b)==x3 and min(b)==x1) and  (max(c)==y1 or max(c)==y3) and min(g)==y0:
 print("%.2f" %(((x3-x1)*((y3+y1)/2))-(abs((x0*y1)+(x1*y3)+(x3*y0)-(x1*y0)-(x3*y1)-(x0*y3))/2)))
 
else:
 print("this is not a quadrilateral")



    
