clc; clear all; close all;
n1=input('Primer Numero:  ');
n2=input('Segundo Numero:  ');
cont=1;
params= cell(1,3);
if n1>n2
  params{1,1}=n1;
  params{1,2}=n2;
  for x=n1:-1:n2
    V(cont)=x;
    cont=cont+1;
  endfor
endif
if n2>n1
  params{1,2}=n1;
  params{1,1}=n2;
  for x=n2:-1:n1
    V(cont)=x;
    cont=cont+1;
  endfor
endif
disp(V)
s=mat2str(V);
params{1,3}=s;
save('MayorAMenor.txt','V','-ascii');
conn = pq_connect(setdbopts('dbname','HWP','host','localhost',
'port','5432','user','postgres','password','123fgthg'));
N=pq_exec_params(conn, "insert into MaxMin(NumMax, NumMin, Resultado) values($1,$2,$3);",params); %insertar datos en la tabla

