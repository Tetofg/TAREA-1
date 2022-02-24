clc; clear all; close all;
pkg load database;
fprintf('Bienvenido al programa\n');
fprintf('A continuacion ingrese 3 numeros enteros positivos\n');
a=0;
b='';
n1=input('Primer Numero: ');
n2=input('Segundo Numero: ');
n3=input('Tercero Numero: ');

if n1>n2 && n1>n3
  fprintf('El primer numero es el mas grande\n');
  a=n1+n2+n3;
  b=mat2str(a);
endif

if n2>n1 && n2>n3
  fprintf('El segundo numero es el mas grande\n');
  a=n1*n2*n3;
  b=mat2str(a);
endif

if n3>n1 && n3>n2
  fprintf('El tercer numero es el mas grande\n');
  t1=mat2str(n1);
  t2=mat2str(n2);
  t3=mat2str(n3);
  b= strcat(t1, t2, t3);
endif

if n1==n3 && n1==n2 && n2==n3
  fprintf('Todos son iguales: %d, %d, %d \n', n1, n2, n3);
  b='Todos son iguales';
endif
fprintf('%s \n', b);

params= cell(1,4);
params{1,1}=n1;
params{1,2}=n2;
params{1,3}=n3;
params{1,4}=b;
save('num3.txt','b','-ascii');
conn = pq_connect(setdbopts('dbname','HWP','host','localhost',
'port','5432','user','postgres','password','123fgthg'));
N=pq_exec_params(conn, "insert into ac3(n1, n2, n3, res) values($1,$2,$3,$4);",params); %insertar datos en la tabla





