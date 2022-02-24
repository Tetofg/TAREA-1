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
      cont=1;
      for x=1:2:100
          V(cont)=x;
          cont=cont+1;
      endfor
      
      fprintf("La cantidad de numero imapares es: %d \n",cont-1);
      disp(V);

      s=cont-1;
      save('impares.txt','V','s','-ascii');
      params= cell(1,2);
      ss=mat2str(V);
      params{1,1}=ss;
      params{1,2}=s;
      conn = pq_connect(setdbopts('dbname','HWP','host','localhost',
      'port','5432','user','postgres','password','123fgthg'));
      N=pq_exec_params(conn, "insert into impar1(imapres,cantidad) values($1,$2);",params); %insertar datos en la tabla
      save('impares.txt','V','-ascii');
      retry=false;1
    endif
    if m==2
      conn = pq_connect(setdbopts('dbname','HWP','host','localhost',
      'port','5432','user','postgres','password','123fgthg'));
      N=pq_exec_params(conn, "Select * from impar1;"); %insertar datos en la tabla
      disp(N)
      retry=false;
    endif
    
  catch
    fprintf("A ingresado un valor erroneo vuelva a intentarlo %d \n");
    msg = lasterror.message;
    fprintf(msg);
  end_try_catch


endwhile

