
from re import U
from turtle import end_fill
import streamlit as st 
import numpy as np 
import matplotlib.pyplot as plt 
st.title("hola")

st.sidebar.checkbox("Convolucion")
st.sidebar.number_input("DEsplazamiento")
#a=st.number_input('escalamiento')
listado=["-","seno","coseno","tramos1","tramos2","tramos3","senoidal","Prueba"]
w=st.sidebar.selectbox("Metodo",listado)
#st.radio('hola',['y','r'])
m=2
#b=st.text_input('Digite su nomre')
#st.write(b)
#st.write(a)
A= st.sidebar.number_input("Digite la amplitud")  
F= st.sidebar.number_input("Digite la frecuencia")

if w=="-":
  st.write("Escoja una gráfica")
    
elif w=="seno":
    #if st.sidebar.button("OK"):
    #st.write("Es la seno")
    delta=0.1
    t=np.arange(0,10+delta,delta)
    t1=np.arange(0,20+delta,delta)
    y=np.cos(t)
    #z=A*np.sin(2*np.pi*F*t)
    S=np.convolve(y,y)
    s1=S*delta
    fig,(ax2, p, ax3)= plt.subplots(3, 1)
    ax2.plot(t1,s1)
    p.plot(t,y)
    ax3.plot(t,y)

    st.pyplot(fig)
    

elif w=="coseno":
    st.write("Es la coseno")
    

    fig1,(p, ax2)= plt.subplots(2, 1,)
    t=np.arange(0,10,0.001)
    y=np.cos(t)
    z=A*np.sin(2*np.pi*F*t)
    p.plot(t,y)
    p.set_title('coseno')
    p.set_xlabel('n')
    ax2.plot(t,z)
    st.pyplot(fig1)

    fig2, (h)= plt.subplots(1, 1)
    h.plot(t,y)
    st.pyplot(fig2)

elif w=="tramos1":
  u=st.number_input("Digite el intervalo de tiempo")
  if st.sidebar.button("OK"):
    st.write("Es a tramos1")
    d=u
    a=0
    b=(d/3)*1
    c=(d/3)*2

    def tramo1 (x):
      return 0

    def tramo2 (x):
      return x-b

    def tramo3 (x):
      return b

    x=np.arange(a,d,0.01) 
    y=np.piecewise(x,[(a<=x) & (x<b), (b<=x) & (x<=c), (c<x) & (x<=d)],[lambda x:tramo1(x), lambda x:tramo2(x), lambda x:tramo3(x)])
    tramo1=np.vectorize(tramo1)
    #tramo2=np.vectorize(tramo2)
    tramo3=np.vectorize(tramo3)
    fig3,(ax1)= plt.subplots(1, 1)
    ax1.plot(x[x<b], tramo1(x[x<b]))
    ax1.plot(x[(b<=x) & (x<c)], tramo2(x[(b<=x) & (x<c)]))
    ax1.plot(x[(c<=x) & (x<=d)], tramo3(x[(c<=x) & (x<=d)]))
    st.pyplot(fig3)
elif w=="tramos2":
  u=st.number_input("Digite el intervalo de tiempo")
  if st.sidebar.button("OK"):
    st.write("Es a tramos2")
    d=u
    a=0
    b=(d/3)*1
    c=(d/3)*2

    def tramo1 (x):
      return b

    def tramo2 (x):
      return -x+b*2

    def tramo3 (x):
      return 0

    x=np.arange(a,d,0.01) 
    y=np.piecewise(x,[(a<=x) & (x<b), (b<=x) & (x<=c), (c<x) & (x<=d)],[lambda x:tramo1(x), lambda x:tramo2(x), lambda x:tramo3(x)])
    tramo1=np.vectorize(tramo1)
    #tramo2=np.vectorize(tramo2)
    tramo3=np.vectorize(tramo3)
    fig3,(ax1)= plt.subplots(1, 1)
    ax1.plot(x[x<b], tramo1(x[x<b]))
    ax1.plot(x[(b<=x) & (x<c)], tramo2(x[(b<=x) & (x<c)]))
    ax1.plot(x[(c<=x) & (x<=d)], tramo3(x[(c<=x) & (x<=d)]))
    st.pyplot(fig3)

elif w=="tramos3":
  u=st.number_input("Digite el intervalo de tiempo")
  if st.sidebar.button("OK"):
    st.write("Es a tramos3")
    d=u
    a=0
    b=(d/3)*1
    c=(d/3)*2

    def tramo1 (x):
      return x

    def tramo2 (x):
      return b

    def tramo3 (x):
      return -x+b*3

    # x=np.arange(a,d,0.01) 
    # y=np.piecewise(x,[(a<=x) & (x<b), (b<=x) & (x<=c), (c<x) & (x<=d)],[lambda x:tramo1(x), lambda x:tramo2(x), lambda x:tramo3(x)])
    # tramo1=np.vectorize(tramo1)
    # tramo2=np.vectorize(tramo2)
    # tramo3=np.vectorize(tramo3)
    # fig3,(ax1,ax2)= plt.subplots(2, 1)
    # ax1.plot(x[x<b], tramo1(x[x<b]))
    # ax1.plot(x[(b<=x) & (x<c)], tramo2(x[(b<=x) & (x<c)]))
    # ax1.plot(x[(c<=x) & (x<=d)], tramo3(x[(c<=x) & (x<=d)]))
    #ax2.stem(x[x<b], tramo1(x[x<b]))-
    # ax1.stem(x[(b<=x) & (x<c)], tramo2(x[(b<=x) & (x<c)]))-
    # ax1.stem(x[(c<=x) & (x<=d)], tramo3(x[(c<=x) & (x<=d)]))-

    x=np.arange(a,d,0.01) 
    x1=np.arange(a,d+1,1) 
    y1= lambda n: np.piecewise(x1,[(a<=x1) & (x1<b), (b<=x1) & (x1<=c), (c<x1) & (x1<=d)],[lambda x1:tramo1(x1), lambda x1:tramo2(x1), lambda x1:tramo3(x1)])
    y= lambda n: np.piecewise(x,[(a<=x) & (x<b), (b<=x) & (x<=c), (c<x) & (x<=d)],[lambda x:tramo1(x), lambda x:tramo2(x), lambda x:tramo3(x)])
    signal=y(x)
    tramo1=np.vectorize(tramo1)
    tramo2=np.vectorize(tramo2)
    tramo3=np.vectorize(tramo3)
    fig3,(ax1,ax2)= plt.subplots(2, 1)
    ax1.plot(x[x<b], tramo1(x[x<b]))
    ax1.plot(x[(b<=x) & (x<c)], tramo2(x[(b<=x) & (x<c)]))
    ax1.plot(x[(c<=x) & (x<=d)], tramo3(x[(c<=x) & (x<=d)]))
    ax2.stem(x1[x1<b], tramo1(x1[x1<b]))
    ax2.stem(x1[(b<=x1) & (x1<c)], tramo2(x1[(b<=x1) & (x1<c)]))
    ax2.stem(x1[(c<=x1) & (x1<=d)], tramo3(x1[(c<=x1) & (x1<=d)]))

    st.pyplot(fig3)
#invertir y dezplazar Discretas 
elif w=="senoidal":
  A1=st.number_input("Amplitud")
  W1=st.number_input("Frecuencia")
  puntoinicio1=int(st.number_input("Ingrese el valor del punto de inicio (numero entero) 1 sin"))
  puntofinal1=st.number_input("Ingrese el valor del punto final (numero entero) 1 sin")
  vx1=np.arange((puntofinal1-puntoinicio1)/0.999999)
  vx2=np.arange((puntofinal1-puntoinicio1)/0.999999)
  #vx3=np.arange((puntofinal1-puntoinicio1)/0.999999)
  # vx1=np.arange((puntofinal1-puntoinicio1)/0.999999,puntofinal1,1)
  # vx2=np.arange((puntofinal1-puntoinicio1)/0.999999,puntofinal1,1)
  # vx3=np.arange((puntofinal1-puntoinicio1)/0.999999,puntofinal1,1)
  n1=np.arange(puntoinicio1,puntofinal1,0.999999)
  n2=np.arange(puntoinicio1,puntofinal1,0.999999)
  n3=n2-(puntofinal1+1)
  c1=int(puntofinal1-puntoinicio1+1)
  i1=puntoinicio1
  i2=puntofinal1
  #i3=-1
  for i in range(puntoinicio1,c1,1):
    vx1[i1]= A1*np.sin(W1*i1)
    vx2[i1]= A1*np.sin(W1*i2)
    #vx3[i3]= A1*np.sin(W1*i1)
    i1=i1+1
    i2=i2-1
    #i3=i3+1

  if st.sidebar.button("OK"):
    fig, (grafica1,p)=plt.subplots(2,1)
    grafica1.stem(n1,vx1)
    grafica1.stem(n3,vx2)
    p.stem(n2,vx2)
    #j.stem(n2,vx3)
    st.pyplot(fig)

elif w=="Prueba":
  u=st.number_input("Digite el intervalo de tiempo")
  if st.sidebar.button("OK"):
    st.write("Es uan prueba")
    
    d=u
    a=0
    b=(d/3)*1
    c=(d/3)*2

    def tramo1 (x):
      return 0

    def tramo2 (x):
      return x-b

    def tramo3 (x):
      return b
     
    x1=np.arange(a,d+1,1) 
    y1= lambda n: np.piecewise(x1,[(a<=x1) & (x1<b), (b<=x1) & (x1<=c), (c<x1) & (x1<=d)],[lambda x1:tramo1(x1), lambda x1:tramo2(x1), lambda x1:tramo3(x1)])
    
    tramo1=np.vectorize(tramo1)
    tramo2=np.vectorize(tramo2)
    tramo3=np.vectorize(tramo3)
    fig3,(ax1,ax2)= plt.subplots(2, 1)

    ax2.stem(x1[x1<b], tramo1(x1[x1<b]))
    ax2.stem(x1[(b<=x1) & (x1<c)], tramo2(x1[(b<=x1) & (x1<c)]))
    ax2.stem(x1[(c<=x1) & (x1<=d)], tramo3(x1[(c<=x1) & (x1<=d)]))

    st.pyplot(fig3) 


#A= 5  
#F= 1
#puntoinicio=st.sidebar.number_input("Ingrese el valor del punto de inicio")
#puntofinal=st.sidebar.number_input("Ingrese el valor del punto final")

#t1=np.arange(puntoinicio,puntofinal,0.001)
#x1 = A*np.sin(2*np.pi*F*t1)
    


 

#b=3
#t=-2:1/1000:2
#app.y=m*app.t+b;


