clc; clear all; close all;
pkg load database;
retry= true;
res=1;
fac=0;
div = "";
while retry
  try
    fprintf("\n Elija una opcion \n 1.Correr el programa \n 2.Mostrar Historial \n");
    m=(input('Elija:   '));
    if m>2||m==0|m<01
      fprintf("Elija una opcion correcta \n");
    endif
    if m==1
      p=input("Ingrese un numero:   ");
      w=mod(p,7);
      if w==0
        div="SI"
        for x=p:-1:1
          res=res*x;
        endfor
        fprintf("El Factorial es: %d",res);
        conn = pq_connect(setdbopts('dbname','HWP','host','localhost',
        'port','5432','user','postgres','password','123fgthg'));
        params= cell(1,3);
        params{1,1}=p;
        fac=res;
        params{1,2}=fac;
        params{1,3}=div;
        N=pq_exec_params(conn, "insert into factorial(num,fac,div) values($1,$2,$3);",params); %insertar datos en la tabla
        save('factorial.txt','p','fac','div','-ascii');
        retry=false;
      endif
      if w~=0
        fprintf("Numero no Divisible entre 7\n");
        div="NO";
        conn = pq_connect(setdbopts('dbname','HWP','host','localhost',
        'port','5432','user','postgres','password','123fgthg'));
        params= cell(1,3);
        params{1,1}=p;
        params{1,2}=fac;
        params{1,3}=div;
        N=pq_exec_params(conn, "insert into factorial(num,fac,div) values($1,$2,$3);",params); %insertar datos en la tabla
        save('factorial.txt','p','fac','div','-ascii');
        retry=false;
      endif
    endif
    if m==2
      conn = pq_connect(setdbopts('dbname','HWP','host','localhost',
      'port','5432','user','postgres','password','123fgthg'));
      N=pq_exec_params(conn, "Select * from factorial;"); %insertar datos en la tabla
      disp(N);
      retry=false;
    endif
  catch
    fprintf("A ingresado un valor erroneo vuelva a intentarlo %d \n");
    msg = lasterror.message;
    fprintf(msg);
  end_try_catch
endwhile