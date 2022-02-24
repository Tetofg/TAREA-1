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
      a=input('Ingrese el año:  ');
      Es='';
      if (mod(a,400)==0)||(mod(a,4)==0)||(mod(a,100)==0)
         Es='Bisiesto';
         fprintf("El año es Bisiesto \n");
      elseif
         Es='No es bisiesto'; 
         fprintf("El año no es bisiesto \n");
      endif
      params= cell(1,2);
      params{1,1}=a;
      params{1,2}=Es;
      conn = pq_connect(setdbopts('dbname','HWP','host','localhost',
      'port','5432','user','postgres','password','123fgthg'));
      N=pq_exec_params(conn, "insert into bisiesto(yer, bis) values($1,$2);",params); %insertar datos en la tabla
      retry=false;
    endif
    if m==2
      conn = pq_connect(setdbopts('dbname','HWP','host','localhost',
      'port','5432','user','postgres','password','123fgthg'));
      N=pq_exec_params(conn, "Select * from bisiesto;"); %insertar datos en la tabla
      disp(N)
      retry=false;
    endif
  catch
    fprintf("A ingresado un valor erroneo vuelva a intentarlo %d \n");
    msg = lasterror.message;
    fprintf(msg);
  end_try_catch
endwhile

