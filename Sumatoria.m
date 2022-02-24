clc; clear all; close all;
pkg load database %cargar el paquete;
nm=input('Ingrese el numero maximo de la sumatoria:  ');
sum=0;
for x=0:1:nm
  sum=sum+x;
endfor
fprintf('Resultado: %d\n',sum)
params= cell(1,2);
params{1,1}=nm;
params{1,2}=sum;
save('Sumatoria.txt','nm','sum','-ascii');
conn = pq_connect(setdbopts('dbname','HWP','host','localhost',
'port','5432','user','postgres','password','123fgthg'));
N=pq_exec_params(conn, "insert into Sumatoria(NumMax, Resultado) values($1,$2);",params); %insertar datos en la tabla
%N=pq_exec_params(conn, 'select * from redes;') %ver datos en la tabla