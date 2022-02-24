clc; clear all; close all;
strt = input('Ingrese su palabra:   ','s');
Voc=['a','e','i','o','u'];
x=[];
for i=1:5
    x=[x strfind(strt,Voc(i))];
end
cvo=length(x);
fprintf("Cantidad de Vocales en la Palabra: %d",cvo);
s=mat2str(cvo);
params{1,1}=strt;
params{1,2}=cvo;
save('CantVoc.txt','cvo','-ascii');
conn = pq_connect(setdbopts('dbname','HWP','host','localhost',
'port','5432','user','postgres','password','123fgthg'));
N=pq_exec_params(conn, "insert into NumVocG(Palabra, NumVoc) values($1,$2);",params); %insertar datos en la tabla
