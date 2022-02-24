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
      fprintf('Bienvenido al programa\n');
      fprintf('A continuacion ingrese 3 numeros enteros positivos\n');
      b='';
      n1=input('Primer Numero: ');
      n2=input('Segundo Numero: ');
      n3=input('Tercero Numero: ');

      if (n1==n2 && n1~=n3)||(n1==n3 & n1~=n2)||(n2==n3 & n2~=n1)
        fprintf('Es un Triangulo Isoceles\n');
        b='Isoseles';
      endif

      if n1~=n2 && n2~=n3 && n1~=n3
        fprintf('Es un Triangulo Escaleno\n');
        b='Escaleno';
      endif

      if n1==n3 && n1==n2 && n2==n3
        fprintf('Es un Triangulo Equilatero \n');
        b='Equilatero';
      endif
      params= cell(1,4);
      params{1,1}=n1;
      params{1,2}=n2;
      params{1,3}=n3;
      params{1,4}=b;
      save('num3.txt','b','-ascii');
      conn = pq_connect(setdbopts('dbname','HWP','host','localhost',
      'port','5432','user','postgres','password','123fgthg'));
      N=pq_exec_params(conn, "insert into triangulo(n1, n2, n3, res) values($1,$2,$3,$4);",params); %insertar datos en la tabla
      retry=false;
    endif
    if m==2
      conn = pq_connect(setdbopts('dbname','HWP','host','localhost',
      'port','5432','user','postgres','password','123fgthg'));
      N=pq_exec_params(conn, "Select * from triangulo;"); %insertar datos en la tabla
      disp(N)
      retry=false;
    endif
  catch
    fprintf("A ingresado un valor erroneo vuelva a intentarlo %d \n");
    msg = lasterror.message;
    fprintf(msg);
  end_try_catch
endwhile

