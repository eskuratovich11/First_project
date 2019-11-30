import numpy as np                                    #импортируем библиотеки 
import matplotlib.pyplot as plt
G1=6.6743
G2=10**-11
G=G1*G2 #гравитационная постоянная (м3/кг*с**2)
c1=2.99792458
c2=10**8
c=c1*c2 #скорость света(м/сек)
R1_sun=6.9655
R2_sun=10**8
R_sun=R1_sun*R2_sun #радиус Солнца, м
M1_sun=1.9855
M2_sun=10**30
M_sun=M1_sun*M2_sun #масса Солнца, кг
sdvig_sun=0.5 #расстояние от звезды до луча света х10**8, м
alpha1_sun=(4*G1*M1_sun)/((R1_sun+sdvig_sun)*c1**2)
alpha2_sun=(G2*M2_sun)/(R2_sun*c2**2)
alpha_sun=alpha1_sun*alpha2_sun#угол отклонения, рад
print(alpha_sun,alpha_sun*60*180/3.1415926,alpha_sun*3600*180/3.1415926 )
r0_sun=R1_sun+sdvig_sun #расстояние от центра звезды до луча света
def iskr_sun(R1_sun=6.9655, t=np.arange(-2*np.pi,2*np.pi,0.1)):#Функция созданиия искревленного луча
    x=R1_sun*np.sin(t)
    y=R1_sun*np.cos(t)#параметрическое задание круга
    plt.plot(x,y, color='k')##вызов круга
    plt.plot([r0_sun,r0_sun], [-2*R1_sun,0], color='b')#команда изображения y от x
    plt.plot([r0_sun,r0_sun], [0,2*R1_sun], color='b', linestyle='--')#команда изображения y от x
    plt.plot([r0_sun,r0_sun-2*R1_sun*np.tan(alpha_sun)], [0,2*R1_sun], color='g')#команда изображения y от x
    plt.xlabel('Расстояние*10**8,м') #подпись оси Ох
    plt.ylabel('Расстояние*10**8,м') #подпись оси Оу
    plt.title('Угол отклонения света вблизи Солнца,') #подпись всего графика
    plt.legend() #вызов окна подписей графиков
    plt.axis('equal')
    plt.show()   #команда вывода графика на экран
iskr_sun(R1_sun=6.9655, t=np.arange(-2*np.pi,2*np.pi,0.1))#Вызов функции

G1=6.6743
G2=10**-11
G=G1*G2 #гравитационная постоянная (м3/кг*с**2)
c1=2.99792458
c2=10**8
c=c1*c2 #скорость света(м/сек)
R1_VY=9.8789
R2_VY=10**11
R_VY=R1_VY*R2_VY #м
M1_VY=3.384
M2_VY=10**31
M_VY=M1_VY*M2_VY #кг
sdvig_VY=1 #расстояние от звезды до луча света х10**11, м
alpha1_VY=(4*G1*M1_VY)/((R1_VY+sdvig_VY)*c1**2)
alpha2_VY=(G2*M2_VY)/(R2_VY*c2**2)
alpha_VY=alpha1_VY*alpha2_VY #угол отклонения, рад
print(alpha_VY,alpha_VY*60*180/3.1415926,alpha_VY*3600*180/3.1415926 )
r0_VY=R1_VY+sdvig_VY #расстояние от центра звезды до луча света
def iskr_VY(R1_VY=9.8789, t=np.arange(-2*np.pi,2*np.pi,0.1)):#Функция созданиия искревленного луча
    x=R1_VY*np.sin(t)
    y=R1_VY*np.cos(t)#параметрическое задание круга
    plt.plot(x,y, color='k')#вызов круга
    plt.plot([r0_VY,r0_VY], [-2*R1_VY,0], color='y') #команда изображения y от x
    plt.plot([r0_VY,r0_VY], [0,2*R1_VY], color='y', linestyle='--') #команда изображения y от x
    plt.plot([r0_VY,r0_VY-2*R1_VY*np.tan(alpha_VY)], [0,2*R1_VY], color='r') #команда изображения y от x
    plt.xlabel('Расстояние*10**11,м')#подпись оси Ох
    plt.ylabel('Расстояние*10**11,м') #подпись оси Оу
    plt.title('Угол отклонения света вблизи VY Большого пса') #подпись всего графика
    plt.legend() #вызов окна подписей графиков 
    plt.axis('equal')
    plt.show() #команда вывода графика на экран
iskr_VY(R1_VY=9.8789, t=np.arange(-2*np.pi,2*np.pi,0.1))#Вызов функции

G1=6.6743
G2=10**-11
G=G1*G2 #гравитационная постоянная (м3/кг*с**2)
c1=2.99792458
c2=10**8
c=c1*c2 #скорость света(м/сек)
R1_neitr_star=2
R2_neitr_star=10**4
R_neitr_star=R1_neitr_star*R2_neitr_star #м
M1_neitr_star=2.464
M2_neitr_star=10**31
M_neitr_star=M1_neitr_star*M2_neitr_star #кг
sdvig_neitr_star=25 #расстояние от звезды до луча света х10**4, м
alpha1_neitr_star=(4*G1*M1_neitr_star)/((R1_neitr_star+sdvig_neitr_star)*c1**2)
alpha2_neitr_star=(G2*M2_neitr_star)/(R2_neitr_star*c2**2)
alpha_neitr_star=alpha1_neitr_star*alpha2_neitr_star #угол отклонения, рад
print(alpha_neitr_star,alpha_neitr_star*180/3.1415926 )
r0_neitr_star=R1_neitr_star+sdvig_neitr_star #расстояние от центра звезды до луча света
def iskr_neitr_star(R1_neitr_star=2, t=np.arange(-2*np.pi,2*np.pi,0.1)):#Функция созданиия искревленного луча
    x=R1_neitr_star*np.sin(t)
    y=R1_neitr_star*np.cos(t)#параметрическое задание круга
    plt.plot(x,y, color='k')#вызов круга
    plt.plot([r0_neitr_star,r0_neitr_star], [-5*R1_neitr_star,0], color='c')#команда изображения y от x
    plt.plot([r0_neitr_star,r0_neitr_star], [0,5*R1_neitr_star], color='c', linestyle='--')#команда изображения y от x
    plt.plot([r0_neitr_star,r0_neitr_star-5*R1_neitr_star*np.tan(alpha_neitr_star)], [0,5*R1_neitr_star], color='m')#команда изображения y от x
    plt.xlabel('Расстояние*10**4,м') #подпись оси Ох
    plt.ylabel('Расстояние*10**4,м') #подпись оси Оу
    plt.title('Угол отклонения света вблизи SGR 1806-20') #подпись всего графика
    plt.legend() #вызов окна подписей графиков 
    plt.axis('equal')
    plt.show() #команда вывода графика на экран
iskr_neitr_star(R1_neitr_star=2, t=np.arange(-2*np.pi,2*np.pi,0.1))#Вызов функции


def grafic(M_neitr_star=2.464*10**31):             #функция графика
    """
    этот график показывает зависимость угла отклонения от массы и 
    расстояния до центра нейтронная звезды
    """
    x=np.arange(19*10**3, 5*10**4, 10**3) #определяем переменную x по радиусу звезды
    y = (4*G*M_neitr_star)/(x*c**2) # определяем переменную y в зависимости от x по формуле определения угла отклонения света                                                         
    plt.plot(x,y,color='y', label = 'Нейтронная звезда') #вызов графика
    plt.xlabel('Прицельное расстояние,м')#подпись оси Ох
    plt.ylabel('Угол отклонения,рад')#подпись оси Оу
    plt.title('Угол отклонения света вблизи нейтронной звезды')#подпись всего графика
    plt.legend() #вызов окна подписей графиков 
    plt.show()   #команда вывода графика на экран
grafic(M_neitr_star=2.464*10**31) #вызов функции


def grafic_sun(M_sun=2*10**30):                                 #функция графика
    """
    этот график показывает зависимость угла отклонения от массы и 
    расстояния до центра Солнца
    """
    x=np.arange(696*10**6, 696*10**7, 10**4) #определяем переменную x по радиусу звезды
    y = (4*G*M_sun)/(x*c**2)      # определяем переменную y в зависимости от x по формуле определения угла отклонения света                 
    plt.plot(x,y,color='r',label = 'Cолнце')             #вызов графика
    plt.xlabel('Прицельное расстояние,м')#подпись оси Ох
    plt.ylabel('Угол отклонения,рад')  #подпись оси Оу
    plt.title('Угол отклонения света вблизи Солнца')#подпись всего графика
    plt.legend()    #вызов окна подписей графиков                           
    plt.show()  #команда вывода графика на экран
grafic_sun(M_sun=2*10**30) #вызов функции
                             
def grafic_VY (M_VY=3.381*10**31):            #функция графика 
    """
    этот график показывает зависимость угла отклонения от массы VY большого пса  и 
    расстояния до центра VY большого пса 
    """                      
    x=np.arange(9.8789*10**11, 9.8789*10**12, 10**6) #определяем переменную x по радиусу звезды
    y = (4*G*M_VY)/(x*c**2)     # определяем переменную y в зависимости от x по формуле определения угла отклонения света
    plt.plot(x,y, color='b',label='VY Большого пса')     #вызов графика
    plt.xlabel('Прицельное расстояние,м')#подпись оси Ох
    plt.ylabel('Угол отклонения,рад') #подпись оси Оу
    plt.title('Угол отклонения света вблизи VY Большого пса') #подпись всего графика
    plt.legend()   #вызов окна подписей графиков                 
    plt.show() #команда вывода графика на экран
    
grafic_VY(M_VY=3.381*10**31) #вызов функции