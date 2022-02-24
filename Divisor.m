clc; clear all; close all;
pkg load database;
fprintf('Bienvenido al programa\n');
fprintf('Divisores de un numero: A continuacion ingrese un numero\n');
a=input('Ingrese su numero:');
c=1;
for x=1:a
  y=mod(a,x);
  if y==0
    V(c)=x;
    c=c+1;
    
  endif
endfor
fprintf('Los divisores de %i son:\n', a);
disp(V);
s=mat2str(V);
params= cell(1,2);
params{1,1}=a;
params{1,2}=s;
save('Divisor.txt','V','-ascii');
conn = pq_connect(setdbopts('dbname','HWP','host','localhost',
'port','5432','user','postgres','password','123fgthg'));
N=pq_exec_params(conn, "insert into Divisores(numero,divisores) values($1,$2);",params); %insertar datos en la tabla
