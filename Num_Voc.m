clc; clear all; close all;
strt = input('Ingrese su palabra:   ','s');
voc=['a','e','i','o','u'];
cant=[0,0,0,0,0];
  for x=1:1:length(strt)
    if strt(x) == voc(1)
      cant(1)=cant(1)+1;
    endif
    if strt(x) == voc(2)
      cant(2)=cant(2)+1;
    endif
    if strt(x) == voc(3)
      cant(3)=cant(3)+1;
    endif
    if strt(x) == voc(4)
      cant(4)=cant(4)+1;
    endif
    if strt(x) == voc(5)
      cant(5)=cant(5)+1;

    endif
    endfor

disp(cant);
fprintf('\nLa # de la vocal a es de: %d', cant(1));
fprintf('\nLa # de la vocal e es de: %d', cant(2));
fprintf('\nLa # de la vocal i es de: %d', cant(3));
fprintf('\nLa # de la vocal o es de: %d', cant(4));
fprintf('\nLa # de la vocal u es de: %d\n', cant(5));

params= cell(1,6);
params{1,1}=strt;
params{1,2}=cant(1);
params{1,3}=cant(2);
params{1,4}=cant(3);
params{1,5}=cant(4);
params{1,6}=cant(5);
save('Num_Voc.txt','strt','cant','-ascii');
conn = pq_connect(setdbopts('dbname','HWP','host','localhost',
'port','5432','user','postgres','password','123fgthg'));
N=pq_exec_params(conn, "insert into vowc(palabra,numa,nume,numi,numo,numu) values($1,$2,$3,$4,$5,$6);",params); %insertar datos en la tabla
