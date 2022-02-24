clc; clear all; close all;
st=input('Ingrese el numero de inicio:  ');
en=input('Ingrese el numero de fin:  ');
cont=1;
for x=st:2:en
  V(cont)= x;
  cont=cont+1;
endfor
disp(V)
params= cell(1,3);
params{1,1}=st;
params{1,2}=en;
s=mat2str(V);
params{1,3}=s;
save('Num2e2.txt','V','-ascii');
conn = pq_connect(setdbopts('dbname','HWP','host','localhost',
'port','5432','user','postgres','password','123fgthg'));
N=pq_exec_params(conn, "insert into plus2(numStr, numEnd, num2num) values($1,$2,$3);",params); %insertar datos en la tabla
