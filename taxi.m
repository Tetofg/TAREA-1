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
      mod=(input('Ingrese el mod del taxi: '));
      km=(input('Ingrese el km en Km del taxi: '));
      if mod<2007&&20<km
         fprintf('Debe renovarse \n');
         sts='Debe renovarse'; 
      elseif 2007<=mod<=2013&&20000==km
        fprintf('Debe recibir mantenimiento \n');
        sts='Debe recibir mantenimiento';
      elseif mod>2013&&10000>km
        fprintf('Esta en optimas condiciones \n');
        sts='Esta en optimas condiciones';
      else
        fprintf('Mecánico \n');
        sts='Mecánico';
      endif
      %Conectar con PGADMIN
      conn = pq_connect(setdbopts('dbname','HWP','host','localhost',
      'port','5432','user','postgres','password','123fgthg'));
      params=cell(1,3);
      params{1,1}=mod;
      params{1,2}=km;
      params{1,3}=sts;
      N=pq_exec_params(conn, "insert into taxi(modelo, km, status) values($1,$2,$3);",params); %insertar datos en la tabla
      %Texto
      save('taxi.txt','mod', 'km','sts','-ascii');
      retry=false;
   endif
    if m==2
      conn = pq_connect(setdbopts('dbname','HWP','host','localhost',
      'port','5432','user','postgres','password','123fgthg'));
      N=pq_exec_params(conn, "Select * from Taxi;"); %insertar datos en la tabla
      disp(N)
      retry=false;
    endif
  catch
    fprintf("A ingresado un valor erroneo vuelva a intentarlo %d \n");
    msg = lasterror.message;
    fprintf(msg);
  end_try_catch
endwhile