clc; clear all; close all;
pkg load database;
retry= true;
while retry
  try
    fprintf("\n Elija una opcion \n 1.Correr el programa \n 2.Mostrar Historial \n");
    m=(input('Elija:   '));
    if m>2||m==0|m<0
      fprintf("Elija una opcion correcta \n");
    endif
    if m==1
      fprintf("Ingrese la Primera nota:\n");
      n1=input("Nota 1:  ");
      while n1<0
          fprintf("A ingresado un valor negativo, verifique\n");
          fprintf("Ingrese la Primera nota:\n");
          n1=int(input("Nota 1:  "));
      endwhile
      fprintf("Ingrese la Segunda nota:\n");
      n2=input("Nota 2:\n");
      while n2<0
          fprintf("A ingresado un valor negativo, verifique\n");
          fprintf("Ingrese la Segunda nota:\n");
          n2=input("Nota 2:\n");
      endwhile
      fprintf("Ingrese la Tercera nota:\n");
      n3=input("Nota 3:\n");
      while n3<0
          fprintf("A ingresado un valor negativo, verifique\n");
          fprintf("Ingrese la Tercera nota:\n");
          n3=input("Nota 3:\n");
      endwhile
      mean=(n1+n2+n3)/3;
      if mean>=60
         pas = "APROBADO";
       endif
      if mean<60
          pas="REPROBADO";
      endif
      fprintf("EL ESTADO ES %s CON UN PROMEDIO DE:%s ",pas,mat2str(mean));
      params= cell(1,5);
      params{1,1}=n1;
      params{1,2}=n2;
      params{1,3}=n3;
      params{1,4}=mean;
      params{1,5}=pas;
      conn = pq_connect(setdbopts('dbname','HWP','host','localhost',
      'port','5432','user','postgres','password','123fgthg'));
      N=pq_exec_params(conn, "insert into notas(n1, n2, n3, mean, pass) values($1,$2,$3,$4,$5);",params); %insertar datos en la tabla
      retry=false;
    endif
   
    if m==2
      conn = pq_connect(setdbopts('dbname','HWP','host','localhost',
      'port','5432','user','postgres','password','123fgthg'));
      N=pq_exec_params(conn, "Select * from Notas;"); %insertar datos en la tabla
      disp(N)
      retry=false;
    endif
  catch
    fprintf("A ingresado un valor erroneo vuelva a intentarlo %d \n");
    msg = lasterror.message;
    fprintf(msg);
  end_try_catch
endwhile