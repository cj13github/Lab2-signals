import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import scipy.signal as signal
from scipy import integrate
import time 
import math
from ast import Lambda


tiposeñal=st.sidebar.selectbox("Por favor eliga el tipo de señal:", options=["Continua","Discreta"])

X_tn=st.sidebar.selectbox("Eliga el tipo de señal para X", options=["Exponencial","Sinusoidal", "Triangular","Rectangular","Rampa_1","Rampa_2","Rampa_3"])

H_tn=st.sidebar.selectbox("Eliga el tipo de señal para H", options=["Exponencial","Sinusoidal", "Triangular", "Rectangular", "Rampa_1", "Rampa_2", "Rampa_3"] )


clicked1 = st.sidebar.button("Graph #1")
clicked2 = st.sidebar.button("Convolucion continua (x se mueve)")
clicked3 = st.sidebar.button("Convolucion continua (h se mueve)")
clicked4 = st.sidebar.button("Convolucion discreta (x se mueve)")
clicked5 = st.sidebar.button("Convolucion discreta (h se mueve)")

rampax=0
rampah=0

if tiposeñal=="Continua":
     

     

     if X_tn=="Exponencial":
          A1=st.sidebar.number_input("Ingrese el valor del intercepto de la función X(k) ")
          B1=st.sidebar.number_input("Ingrese el factor de decrecimiento X(k)")
          puntoinicio1=st.sidebar.number_input("Ingrese el valor del punto de inicio X(k)")
          puntofinal1=st.sidebar.number_input("Ingrese el valor del punto final X(k)")
          t1=np.arange(puntoinicio1,puntofinal1,0.001)
          x1=A1*(np.exp(-B1*t1))

     if H_tn=="Exponencial":
          A2=st.sidebar.number_input("Ingrese el valor del intercepto de la función H(k)")
          B2=st.sidebar.number_input("Ingrese el factor de decrecimiento b H(k)")
          puntoinicio2=st.sidebar.number_input("Ingrese el valor del punto de inicio H(k)")
          puntofinal2=st.sidebar.number_input("Ingrese el valor del punto final H(k)")
          t2=np.arange(puntoinicio2,puntofinal2,0.001)
          x2=A2*(np.exp(-B2*t2))


     if X_tn=="Sinusoidal":
          A1=st.sidebar.number_input("Ingrese el valor de la amplitud X(k)")
          F1=st.sidebar.number_input("Ingrese el valor de la frecuencia [Hz] X(k)")
          puntoinicio1=st.sidebar.number_input("Ingrese el valor del punto de inicio X(k)")
          puntofinal1=st.sidebar.number_input("Ingrese el valor del punto final X(k)")
          t1=np.arange(puntoinicio1,puntofinal1,0.001)
          x1= A1*np.sin(2*np.pi*F1*t1)

     if H_tn=="Sinusoidal":
          A2=st.sidebar.number_input("Ingrese el valor de la amplitud H(k)")
          F2=st.sidebar.number_input("Ingrese el valor de la frecuencia [Hz] H(k)")
          puntoinicio2=st.sidebar.number_input("Ingrese el valor del punto de inicio H(k)")
          puntofinal2=st.sidebar.number_input("Ingrese el valor del punto final H(k)")
          t2=np.arange(puntoinicio2,puntofinal2,0.001)
          x2= A2*np.sin(2*np.pi*F2*t2)
     # plt.ylabel("hola")
     if X_tn=="Triangular":
          A1=st.sidebar.number_input("Ingrese el valor de la amplitud X(k)")
          F1=st.sidebar.number_input("Ingrese el valor de la frecuencia [Hz] X(k)")
          puntoinicio1=st.sidebar.number_input("Ingrese el valor del punto de inicio X(k)")
          puntofinal1=st.sidebar.number_input("Ingrese el valor del punto final X(k)")
          t1=np.arange(puntoinicio1,puntofinal1,0.001)
          x1=A1*signal.sawtooth(2*np.pi*F1*t1,0.5)

     if H_tn=="Triangular":
          A2=st.sidebar.number_input("Ingrese el valor de la amplitud H(k)")
          F2=st.sidebar.number_input("Ingrese el valor de la frecuencia [Hz] H(k)")
          puntoinicio2=st.sidebar.number_input("Ingrese el valor del punto de inicio H(k)")
          puntofinal2=st.sidebar.number_input("Ingrese el valor del punto final H(k)")
          t2=np.arange(puntoinicio2,puntofinal2,0.001)
          x2=A2*signal.sawtooth(2*np.pi*F2*t2,0.5)

     if X_tn=="Rectangular":
          A1=st.sidebar.number_input("Ingrese el valor de la amplitud X(k)")
          F1=st.sidebar.number_input("Ingrese el valor de la frecuencia [Hz] X(k)")
          puntoinicio1=st.sidebar.number_input("Ingrese el valor del punto de inicio X(k)")
          puntofinal1=st.sidebar.number_input("Ingrese el valor del punto final X(k)")
          t1=np.arange(puntoinicio1,puntofinal1,0.001)
          x1=A1*signal.square(2*np.pi*F1*t1)

     if H_tn=="Rectangular":
          A2=st.sidebar.number_input("Ingrese el valor de la amplitud H(k)")
          F2=st.sidebar.number_input("Ingrese el valor de la frecuencia [Hz] H(k)")
          puntoinicio2=st.sidebar.number_input("Ingrese el valor del punto de inicio H(k)")
          puntofinal2=st.sidebar.number_input("Ingrese el valor del punto final H(k)")
          t2=np.arange(puntoinicio2,puntofinal2,0.001)
          x2=A2*signal.square(2*np.pi*F2*t2)

     if X_tn=="Rampa_1":
          rampax=1
          u1=st.number_input("Digite el intervalo de tiempo X(k)")
          d1=u1
          a1=0
          b1=(d1/3)*1
          c1=(d1/3)*2

          def tramo1 (x1):
               return 0

          def tramo2 (x1):
               return x1-b1

          def tramo3 (x1):
               return b1

          x1=np.arange(a1,d1,0.01) 
          y1=np.piecewise(x1,[(a1<=x1) & (x1<b1), (b1<=x1) & (x1<=c1), (c1<x1) & (x1<=d1)],[lambda x:tramo1(x1), lambda x1:tramo2(x1), lambda x1:tramo3(x1)])
          tramo1=np.vectorize(tramo1)
          tramo3=np.vectorize(tramo3)
          

     if H_tn=="Rampa_1":
          rampah=1
          u2=st.number_input("Digite el intervalo de tiempo H(k)")
          d2=u2
          a2=0
          b2=(d2/3)*1
          c2=(d2/3)*2

          def tramo11 (x2):
               return 0

          def tramo22 (x2):
               return x2-b2

          def tramo33 (x2):
               return b2

          x2=np.arange(a2,d2,0.01) 
          y2=np.piecewise(x2,[(a2<=x2) & (x2<b2), (b2<=x2) & (x2<=c2), (c2<x2) & (x2<=d2)],[lambda x2:tramo11(x2), lambda x2:tramo22(x2), lambda x2:tramo33(x2)])
          tramo11=np.vectorize(tramo11)
          tramo33=np.vectorize(tramo33)

     if X_tn=="Rampa_2":
          rampax = 1
          u1=st.number_input("Digite el intervalo de tiempo X(k)")        
          d1=u1
          a1=0
          b1=(d1/3)*1
          c1=(d1/3)*2

          def tramo1 (x1):
               return b1

          def tramo2 (x1):
               return -x1+b1*2

          def tramo3 (x1):
               return 0

          x1=np.arange(a1,d1,0.01) 
          y1=np.piecewise(x1,[(a1<=x1) & (x1<b1), (b1<=x1) & (x1<=c1), (c1<x1) & (x1<=d1)],[lambda x1:tramo1(x1), lambda x1:tramo2(x1), lambda x1:tramo3(x1)])
          tramo1=np.vectorize(tramo1)
          tramo3=np.vectorize(tramo3)

     if H_tn=="Rampa_2":
          rampah = 1
          u2=st.number_input("Digite el intervalo de tiempo H(k)")        
          d2=u2
          a2=0
          b2=(d2/3)*1
          c2=(d2/3)*2

          def tramo11 (x2):
               return b2

          def tramo22 (x2):
               return -x2+b2*2

          def tramo33 (x2):
               return 0

          x2=np.arange(a2,d2,0.01) 
          y2=np.piecewise(x2,[(a2<=x2) & (x2<b2), (b2<=x2) & (x2<=c2), (c2<x2) & (x2<=d2)],[lambda x2:tramo11(x2), lambda x2:tramo22(x2), lambda x2:tramo33(x2)])
          tramo11=np.vectorize(tramo11)
          tramo33=np.vectorize(tramo33)

     if X_tn=="Rampa_3":
          rampax=1
          u1=st.number_input("Digite el intervalo de tiempo X(k)")
          d1=u1
          a1=0
          b1=(d1/3)*1
          c1=(d1/3)*2

          def tramo1 (x1):
               return x1

          def tramo2 (x1):
               return b1

          def tramo3 (x1):
               return -x1+b1*3

          x1=np.arange(a1,d1,0.01) 
          y1=np.piecewise(x1,[(a1<=x1) & (x1<b1), (b1<=x1) & (x1<=c1), (c1<x1) & (x1<=d1)],[lambda x1:tramo1(x1), lambda x1:tramo2(x1), lambda x1:tramo3(x1)])
          tramo1=np.vectorize(tramo1)
          tramo2=np.vectorize(tramo2)
          tramo3=np.vectorize(tramo3)

     if H_tn=="Rampa_3":
          rampah=1
          u2=st.number_input("Digite el intervalo de tiempo H(k)")
          d2=u2
          a2=0
          b2=(d2/3)*1
          c2=(d2/3)*2

          def tramo11 (x2):
               return x2

          def tramo22 (x2):
               return b2

          def tramo33 (x2):
               return -x2+b2*3

          x2=np.arange(a2,d2,0.01) 
          y2=np.piecewise(x2,[(a2<=x2) & (x2<b2), (b2<=x2) & (x2<=c2), (c2<x2) & (x2<=d2)],[lambda x2:tramo11(x2), lambda x2:tramo22(x2), lambda x2:tramo33(x2)])
          tramo11=np.vectorize(tramo11)
          tramo22=np.vectorize(tramo22)
          tramo33=np.vectorize(tramo33)

     

     if clicked1:
          fig, (grafica1,grafica2)=plt.subplots(2,1)
          if rampax == 1:
               grafica1.plot(x1[x1<b1], tramo1(x1[x1<b1]))
               grafica1.plot(x1[(b1<=x1) & (x1<c1)], tramo2(x1[(b1<=x1) & (x1<c1)]))
               grafica1.plot(x1[(c1<=x1) & (x1<=d1)], tramo3(x1[(c1<=x1) & (x1<=d1)]))

          if rampah == 1:
               grafica2.plot(x2[x2<b2], tramo11(x2[x2<b2]))
               grafica2.plot(x2[(b2<=x2) & (x2<c2)], tramo22(x2[(b2<=x2) & (x2<c2)]))
               grafica2.plot(x2[(c2<=x2) & (x2<=d2)], tramo33(x2[(c2<=x2) & (x2<=d2)]))

          if rampax == 0:
               grafica1.plot(t1,x1)

          if rampah == 0:
               grafica2.plot(t2,x2)

          st.pyplot(fig)


# if clicked2:

#      delta=0,1
#      s=np.convolve(x1,x2)
#      s1=s*delta
#      fig,(ax2)=plt.subplots(1,1)
#      ax2.plot(t1,s1)


     

          


if tiposeñal=="Discreta":

     if X_tn=="Exponencial":
          b1=st.sidebar.number_input("Ingree el factor de decrecimiento b 1 exp")
          A1=st.sidebar.number_input("Ingree el valor del intercepto de la función A 1 exp")
          puntoinicio1=int(st.sidebar.number_input("Ingrese el valor del punto de inicio 1 exp"))
          puntofinal1=st.sidebar.number_input("Ingrese el valor del punto final 1 exp")
          vx1=np.arange((puntofinal1-puntoinicio1)/0.999999)
          n1=np.arange(puntoinicio1,puntofinal1,0.999999)
          c1=int(puntofinal1-puntoinicio1+1)
          i1=puntoinicio1
          for i in range(puntoinicio1,c1,1):

               vx1[i1]= A1*(np.exp(-b1*i1))
               i1=i1+1

     if H_tn=="Exponencial":
          b2=st.sidebar.number_input("Ingree el factor de decrecimiento b")
          A2=st.sidebar.number_input("Ingree el valor del intercepto de la función A")
          puntoinicio2=int(st.sidebar.number_input("Ingrese el valor del punto de inicio"))
          puntofinal2=st.sidebar.number_input("Ingrese el valor del punto final")
          vx2=np.arange((puntofinal2-puntoinicio2)/0.999999)
          n2=np.arange(puntoinicio2,puntofinal2,0.999999)
          c2=int(puntofinal2-puntoinicio2+1)
          k1=puntoinicio2
          for k in range(puntoinicio2,c2,1):

               vx2[k1]= A2*(np.exp(-b2*k1))
               k1=k1+1

     if X_tn=="Sinusoidal":
          A1=st.sidebar.number_input("Ingrese el valor de la amplitud 1 sin")
          W1=st.sidebar.number_input("Ingrese el valor de la frecuencia [rad/s] 1 sin")
          puntoinicio1=int(st.sidebar.number_input("Ingrese el valor del punto de inicio (numero entero) 1 sin"))
          puntofinal1=st.sidebar.number_input("Ingrese el valor del punto final (numero entero) 1 sin")
          vx1=np.arange((puntofinal1-puntoinicio1)/0.999999)
          n1=np.arange(puntoinicio1,puntofinal1,0.999999)
          c1=int(puntofinal1-puntoinicio1+1)
          i1=puntoinicio1
          for i in range(puntoinicio1,c1,1):
               vx1[i1]= A1*np.sin(W1*i1)
               i1=i1+1

     if H_tn=="Sinusoidal":
          A2=st.sidebar.number_input("Ingrese el valor de la amplitud 2 sin")
          W2=st.sidebar.number_input("Ingrese el valor de la frecuencia [rad/s] 2 sin")
          puntoinicio2=int(st.sidebar.number_input("Ingrese el valor del punto de inicio (numero entero) 2 sin"))
          puntofinal2=st.sidebar.number_input("Ingrese el valor del punto final (numero entero) 2 sin")
          vx2=np.arange((puntofinal2-puntoinicio2)/0.999999)
          n2=np.arange(puntoinicio2,puntofinal2,0.999999)
          c2=int(puntofinal2-puntoinicio2+1)
          k1=puntoinicio2
          for k in range(puntoinicio2,c2,1):
               vx2[k1]= A2*np.sin(W2*k1)
               k1=k1+1
               
     if X_tn=="Triangular":
          A1=st.sidebar.number_input("Ingree el valor de la amplitud 1 tri")
          W1=st.sidebar.number_input("Ingree el valor de la frecuencia [Hz] 1 tri ")
          puntoinicio1=int(st.sidebar.number_input("Ingrese el valor del punto de inicio 1 tri"))
          puntofinal1=st.sidebar.number_input("Ingrese el valor del punto final 1 tri")
          vx1=np.arange((puntofinal1-puntoinicio1)/0.999999)
          n1=np.arange(puntoinicio1,puntofinal1,0.999999)
          c1=int(puntofinal1-puntoinicio1+1)
          i1=puntoinicio1
          for i in range(puntoinicio1,c1,1):

               vx1[i1]= A1*signal.sawtooth(W1*i1,0.5)
               i1=i1+1

     if H_tn=="Triangular":
          A2=st.sidebar.number_input("Ingree el valor de la amplitud 2 tri")
          W2=st.sidebar.number_input("Ingree el valor de la frecuencia [Hz] 2 tri")
          puntoinicio2=int(st.sidebar.number_input("Ingrese el valor del punto de inicio 2 tri"))
          puntofinal2=st.sidebar.number_input("Ingrese el valor del punto final 2 tri")
          vx2=np.arange((puntofinal2-puntoinicio2)/0.999999)
          n2=np.arange(puntoinicio2,puntofinal2,0.999999)
          c2=int(puntofinal2-puntoinicio2+1)
          k1=puntoinicio2
          for k in range(puntoinicio2,c2,1):

               vx2[k1]= A2*signal.sawtooth(W2*k1,0.5)
               k1=k1+1  

     if X_tn=="Rectangular":
          A1=st.sidebar.number_input("Ingree el valor de la amplitud 1 rec")
          W1=st.sidebar.number_input("Ingree el valor de la frecuencia [Hz] 1 rec")
          puntoinicio1=int(st.sidebar.number_input("Ingrese el valor del punto de inicio 1 rec"))
          puntofinal1=st.sidebar.number_input("Ingrese el valor del punto final 1 rec")
          vx1=np.arange((puntofinal1-puntoinicio1)/0.999999)
          n1=np.arange(puntoinicio1,puntofinal1,0.999999)
          c1=int(puntofinal1-puntoinicio1+1)
          i1=puntoinicio1
          for i in range(puntoinicio1,c1,1):

               vx1[i1]= A1*signal.square(W1*i1)
               i1=i1+1
     
     if H_tn=="Rectangular":
          A2=st.sidebar.number_input("Ingree el valor de la amplitud 2 rec")
          W2=st.sidebar.number_input("Ingree el valor de la frecuencia [Hz] 2 rec")
          puntoinicio2=int(st.sidebar.number_input("Ingrese el valor del punto de inicio 2 rec"))
          puntofinal2=st.sidebar.number_input("Ingrese el valor del punto final 2 rec")
          vx2=np.arange((puntofinal2-puntoinicio2)/0.999999)
          n2=np.arange(puntoinicio2,puntofinal2,0.999999)
          c2=int(puntofinal2-puntoinicio2+1)
          k1=puntoinicio2
          for k in range(puntoinicio2,c2,1):

               vx2[k1]= A2*signal.square(W2*k1)
               k1=k1+1

     if X_tn=="Rampa_1":
          rampax=1
          u1=st.number_input("Digite el intervalo de tiempo H(k)")
          d1=u1
          a1=0
          b1=(d1/3)*1
          c1=(d1/3)*2

          def tramo1 (xx1):
               return 0

          def tramo2 (xx1):
               return xx1-b1

          def tramo3 (xx1):
               return b1
     
          x1=np.arange(a1,d1+1,1) 
          y1= lambda n: np.piecewise(x1,[(a1<=x1) & (x1<b1), (b1<=x1) & (x1<=c1), (c1<x1) & (x1<=d1)],[lambda x1:tramo1(x1), lambda x1:tramo2(x1), lambda x1:tramo3(x1)])
    
          tramo1=np.vectorize(tramo1)
          tramo2=np.vectorize(tramo2)
          tramo3=np.vectorize(tramo3)

     if H_tn=="Rampa_1":
          rampah=1
          u2=st.number_input("Digite el intervalo de tiempo H(n)")
          d2=u2
          a2=0
          b2=(d2/3)*1
          c2=(d2/3)*2

          def tramo11 (xx2):
               return 0

          def tramo22 (xx2):
               return xx2-b2

          def tramo33 (xx2):
               return b2
     
          x2=np.arange(a2,d2+1,1) 
          y2= lambda n: np.piecewise(x2,[(a2<=x2) & (x2<b2), (b2<=x2) & (x2<=c2), (c2<x2) & (x2<=d2)],[lambda x2:tramo11(x2), lambda x2:tramo22(x2), lambda x2:tramo33(x2)])
    
          tramo11=np.vectorize(tramo11)
          tramo22=np.vectorize(tramo22)
          tramo33=np.vectorize(tramo33)

     if X_tn=="Rampa_2":
          rampax=1
          u1=st.number_input("Digite el intervalo de tiempo X(n)")
          d1=u1
          a1=0
          b1=(d1/3)*1
          c1=(d1/3)*2

          def tramo1 (xx1):
               return b1

          def tramo2 (xx1):
               return -xx1+b1*2

          def tramo3 (xx1):
               return 0
     
          x1=np.arange(a1,d1+1,1) 
          y1= lambda n: np.piecewise(x1,[(a1<=x1) & (x1<b1), (b1<=x1) & (x1<=c1), (c1<x1) & (x1<=d1)],[lambda x1:tramo1(x1), lambda x1:tramo2(x1), lambda x1:tramo3(x1)])
    
          tramo1=np.vectorize(tramo1)
          tramo2=np.vectorize(tramo2)
          tramo3=np.vectorize(tramo3)


     if H_tn=="Rampa_2":
          rampah=1
          u2=st.number_input("Digite el intervalo de tiempo H(n)")
          d2=u2
          a2=0
          b2=(d2/3)*1
          c2=(d2/3)*2

          def tramo11 (xx2):
               return b2

          def tramo22 (xx2):
               return -xx2+b2*2

          def tramo33 (xx2):
               return 0
     
          x2=np.arange(a2,d2+1,1) 
          y2= lambda n: np.piecewise(x2,[(a2<=x2) & (x2<b2), (b2<=x2) & (x2<=c2), (c2<x2) & (x2<=d2)],[lambda x2:tramo11(x2), lambda x2:tramo22(x2), lambda x2:tramo33(x2)])
    
          tramo11=np.vectorize(tramo11)
          tramo22=np.vectorize(tramo22)
          tramo33=np.vectorize(tramo33)

     if X_tn=="Rampa_3":
          rampax=1
          u1=st.number_input("Digite el intervalo de tiempo X(k)")
          d1=u1
          a1=0
          b1=(d1/3)*1
          c1=(d1/3)*2

          def tramo1 (xx1):
               return xx1

          def tramo2 (xx1):
               return b1

          def tramo3 (xx1):
               return -xx1+b1*3
 
          x1=np.arange(a1,d1+1,1) 
          y1= lambda n: np.piecewise(x1,[(a1<=x1) & (x1<b1), (b1<=x1) & (x1<=c1), (c1<x1) & (x1<=d1)],[lambda x1:tramo1(x1), lambda x1:tramo2(x1), lambda x1:tramo3(x1)])
          tramo1=np.vectorize(tramo1)
          tramo2=np.vectorize(tramo2)
          tramo3=np.vectorize(tramo3)
          


     if H_tn=="Rampa_3":
          rampah=1
          u2=st.number_input("Digite el intervalo de tiempo H(n)")
          d2=u2
          a2=0
          b2=(d2/3)*1
          c2=(d2/3)*2

          def tramo11 (xx2):
               return xx2

          def tramo22 (xx2):
               return b2

          def tramo33 (xx2):
               return -xx2+b2*3
 
          x2=np.arange(a2,d2+1,1) 
          y2= lambda n: np.piecewise(x2,[(a2<=x2) & (x2<b2), (b2<=x2) & (x2<=c2), (c2<x2) & (x2<=d2)],[lambda x2:tramo1(x2), lambda x2:tramo2(x2), lambda x2:tramo3(x2)])
          tramo11=np.vectorize(tramo11)
          tramo22=np.vectorize(tramo22)
          tramo33=np.vectorize(tramo33)
          

     if clicked1:
          fig, (grafica1,grafica2)=plt.subplots(2,1)

          if rampax==0:
               grafica1.stem(n1,vx1)
               

          if rampah==0:
               grafica2.stem(n2,vx2)
               

          if rampax==1:
               grafica1.stem(x1[x1<b1], tramo1(x1[x1<b1]))
               grafica1.stem(x1[(b1<=x1) & (x1<c1)], tramo2(x1[(b1<=x1) & (x1<c1)]))
               grafica1.stem(x1[(c1<=x1) & (x1<=d1)], tramo3(x1[(c1<=x1) & (x1<=d1)]))
               

          if rampah==1:
               grafica2.stem(x2[x2<b2], tramo11(x2[x2<b2]))
               grafica2.stem(x2[(b2<=x2) & (x2<c2)], tramo22(x2[(b2<=x2) & (x2<c2)]))
               grafica2.stem(x2[(c2<=x2) & (x2<=d2)], tramo33(x2[(c2<=x2) & (x2<=d2)]))
               
          st.pyplot(fig)
          
     # if clicked1:
     #      fig, (grafica1,grafica2)=plt.subplots(2,1)
     #      grafica1.stem(n1,vx1)
     #      grafica2.stem(n2,vx2)
     #      st.pyplot(fig)


# if clicked2 :  
     #           fig, (grafica3) = plt.subplots(1,1)
     #           st_a = st.pyplot(plt)
     #           ty = np.arange(puntoinicio1+puntoinicio2,puntofinal1+puntofinal2+0.001, 0.001)
               # if tiposeñal=="Discreta":

               #      y_conv=np.convolve()

               #      y_conv = np.convolve(vx,vh, mode='full')*r
        
               #      y_conv=np.resize(y_conv, np.shape(ty)) 

               #      hs = vh[::-1]
               #      tm = np.arange(xi1-(xf2-xi2),xi1,r)
               #      aniy = np.zeros(len(y_conv))
               #      frames = max(np.size(t1),np.size(t2))
               #      factor = len(ty)/frames
               #      factor = math.floor(factor)
               #      factor_t = (max(ty)-min(ty))/frames

               #      vx =np.resize(vx, np.shape(t1))
               #      hs =np.resize(hs,np.shape(tm))
               #      for i in range(frames):
               #           aniy[:i*factor] = y_conv[:i*factor]
               #           grafica3.clear()
               #           grafica3.stem(tm,hs,linefmt='g',basefmt="purple")
               #           grafica3.stem(t1,vx)
               #           grafica3.axis(xmin=xi1-(xf2-xi2),xmax=xf1+(xf2-xi2))
               #           grafica4.clear()
               #           grafica4.stem(ty,aniy)
               #           tm = tm + factor_t
               #           time.sleep(0.01)
               #           grafica3.legend(['h(t)','x(t)'])
               #           st_a.pyplot(plt)

               # if tiposeñal == "continua":
               #      y_conv = np.convolve(x1,x2, mode='full')*0.001
               #      grafica3.plot(t1,y_conv) 
               #      y_conv = np.resize(y_conv, np.shape(ty))
               #      hs =x2[::-1]
               #      tm = np.arange(puntoinicio1-(puntofinal2-puntoinicio2),puntoinicio1+0.001,0.001)
               #      aniy = np.zeros(len(y_conv))
               #      frames = 30
               #      factor = len(ty)/frames
               #      factor = math.floor(factor)
               #      factor_t = (max(ty)-min(ty))/frames
               #      x1 =np.resize(x1, np.shape(t1))
               #      hs =np.resize(hs,np.shape(tm))
               #      for i in range(frames+2):
               #           aniy[:i*factor] = y_conv[:i*factor]
               #           grafica3.clear()
               #           grafica3.plot(tm,hs,t1,x1)
               #           grafica3.axis(xmin=puntoinicio1-(puntofinal2-puntoinicio2),xmax=puntofinal1+(puntofinal2-puntoinicio2))
               #           grafica4.clear()
               #           grafica4.plot(ty,aniy)
               #           tm = tm + factor_t
               #           time.sleep(0.01)
               #           grafica3.legend(['h(t)','x(t)'])
               #      st_a.pyplot(plt)

                     



               

if clicked2:
     
               fig, (grafica1,grafica2)=plt.subplots(2,1)
               fig1, (grafica3)=plt.subplots(1,1)
               tt1=t1
               tt2=t2
               if rampax == 0:
                    grafica1.plot(tt1,x1)

               if rampah == 0:
                    grafica2.plot(tt2,x2)

               j= -puntoinicio1-puntoinicio2+1
               t1=-t1-j
               grafica3.plot(t1,x1)
               grafica3.plot(t2,x2)
               st.pyplot(fig)
               st.pyplot(fig1)
if clicked3:
     
               fig, (grafica1,grafica2)=plt.subplots(2,1)
               fig1, (grafica3)=plt.subplots(1,1)
               tt1=t1
               tt2=t2
               if rampax == 0:
                    grafica1.plot(tt1,x1)

               if rampah == 0:
                    grafica2.plot(tt2,x2)

               j= -puntoinicio2-puntoinicio1+1
               t2=-t2-j
               grafica3.plot(t1,x1)
               grafica3.plot(t2,x2)
               st.pyplot(fig)
               st.pyplot(fig1)
          #      rodamiento= puntofinal2-(puntoinicio2-1-(puntofinal1-puntoinicio1+1))
          #      puntoinicioT=puntoinicio2-1-(puntofinal1-puntoinicio1)
          #      puntofinalT=puntoinicioT+(puntofinal1-puntoinicio1)

          #      fig, (grafica1,grafica2)=plt.subplots(2,1)
          #      fig1, (grafica3)=plt.subplots(1,1)
               
          #      if rampax == 0:
          #           grafica1.plot(tt1,x1)

          #      if rampah == 0:
          #           grafica2.plot(tt2,x2)

          #      vxi=np.arange((puntofinalT-puntoinicioT)/0.999999)
          #      ni=np.arange(puntoinicioT,puntofinalT,0.999999)

          #      while puntoinicioT<puntofinal2:
          #           integral= integrate.simps(x1,x2)
          #           vxi[puntofinalT]=integral
          #           grafica3.stem(t1,x1)
          #           t1=t1+0.001
          #           puntoinicioT=puntoinicioT+0.001
          #           puntofinalT=puntofinalT+0.001


          #      x3=np.arange()














#      #CONVOLUCIÓN!!!

# if tiposeñal=="Discreta":
#           #x(t-T)

#      if X_tn=="Exponencial":
#                vx1=np.linspace(1,20,20)
#      if X_tn=="Sinusoidal":
#                          vx1=np.arange((puntofinal1-puntoinicio1)/0.001)
#      if X_tn=="Triangular":
#                vx1=np.arange((puntofinal1-puntoinicio1)/0.001)
#      if X_tn=="Rectangular":
#                vx1=np.arange((puntofinal1-puntoinicio1)/0.001)
#      if X_tn=="Rampa_1":
#                a+1
#      if X_tn=="Rampa_2":
#                a+1
#      if X_tn=="Rampa_3":
#                a+1

#      n=puntofinal1-puntoinicio1+1
     # k1=puntoinicio1
     # k=puntofinal1

     # for i in range(n):
     #      vx1[k1]=vx[k]
     #      k1=k1+1
     #      k=k-1

#           k=puntofinal1-puntoinicio1+1
#           l=puntoinicio1
#           for i in range(n):
#                vx1[l-k]=vx1[l]
#                vx1[l]=0
#                l=l+1

#           tamaño1=puntofinal1-puntoinicio1+1
#           tamaño2=puntofinal2-puntoinicio2+1
#           n=tamaño1+tamaño2-1

#           for i in range(n)
#                for i in range(n)



# if tiposeñal == "Continua":

#      if clicked2 :

#           def convolucion(x1,x2):
#                fh = np.flip(x1)
#                rc = np.zeros(x1.size + x2.size - 1)
#                fig, (grafica3)=plt.subplots(1,1)
#                cx = np.insert(x2, 0, np.zeros(x1.size - 1))
#                cx = np.insert(cx, cx.size, np.zeros(x1.size - 1))

#                for n in np.arange(0,rc.size):
#                     for k in np.arange(0,x1.size):
#                          idcx = k + n
#                          rc[n] = rc[n] + fh[k]*cx[idcx]

#                          grafica3.stem(n,rc)
#                return rc

     


















