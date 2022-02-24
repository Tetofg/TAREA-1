clc; clear all; close all;
pkg load database;
retry= true;
retry2= true;
h=0;
while retry
  try
    fprintf("\n Elija una opcion \n 1.Correr el programa \n 2.Mostrar Historial \n");
    m=(input('Elija:   '));
    if m>2||m==0|m<0
      fprintf("Elija una opcion correcta \n");
    endif
    if m==1
      while retry2
        try
           fprintf("A continuacion elija la figura a la cual necesitasacar el area\n");
           fprintf("Elija una opcion:\n1.Circulo\n2.Triangulo\n3.Cuadrado\n4.Rectangulo\n");
           r=input("Elija:   ");
           if r>4||r==0|r<0
             fprintf("Elija una opcion correcta \n");
           endif
           if r==1
             ra=input("Ingrese el radio del Circulo:\n");
             fig="Circulo";
             a= (ra^2)*pi ;
           endif
           if r==2
             ra=input("Ingrese  la base del Triangulo:\n");
             h= input("Ingrese la altura del triangulo:\n");
             fig="Triangulo";
             a=ra*h*1/2 ;
           endif
           if r==3
             ra=input("Ingrese  el lado del cuadrado:\n");
             h = ra;
             a=ra^2;
             fig="Cuadrado";
           endif
           if r==4
             ra=input("Ingrese  la base del rectangulo:\n");
             h=input("Ingrese  la altura del rectangulo \n");
             a=ra*h;
             fig="Rectangulo";
           endif
           fprintf("El Area de %s es de: %d \n", fig,a);
           params= cell(1,4);
           params{1,1}=fig;
           params{1,2}=ra;
           params{1,3}=h;
           params{1,4}=a;
           conn = pq_connect(setdbopts('dbname','HWP','host','localhost',
           'port','5432','user','postgres','password','123fgthg'));
           N=pq_exec_params(conn, "insert into areas(fig, BaOR, h, A) values($1,$2,$3,$4);",params); %insertar datos en la tabla
           retry2=false;
           retry=false;
        catch
          fprintf("A ingresado un valor erroneo vuelva a intentarlo %d \n");
          msg = lasterror.message;
          fprintf(msg);
        end_try_catch
      endwhile
    endif
    if m==2
      conn = pq_connect(setdbopts('dbname','HWP','host','localhost',
      'port','5432','user','postgres','password','123fgthg'));
      N=pq_exec_params(conn, "Select * from Areas;"); %insertar datos en la tabla
      disp(N)
      retry=false;
    endif
  catch
    fprintf("A ingresado un valor erroneo vuelva a intentarlo %d \n");
    msg = lasterror.message;
    fprintf(msg);
  end_try_catch
endwhile
