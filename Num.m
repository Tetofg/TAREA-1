clc; clear all; close all;
strt = input('Ingrese su palabra:      ','s');
voc=['a','e','i','o','u'];
cant=[0,0,0,0,0];
cont=0;
 for x=1:1:length(strt)
    if strt(x) == voc(1)||strt(x) == 'A'
      cont=cont+1;
    endif
    if strt(x) == voc(2)||strt(x) == 'E'
      cont=cont+1;
    endif
    if strt(x) == voc(3)||strt(x) == 'I'
      cont=cont+1;
    endif
    if strt(x) == voc(4)||strt(x) == 'O'
      cont=cont+1;
    endif
    if strt(x) == voc(5)||strt(x) == 'U'
      cont=cont+1;
    endif
 endfor

fprintf('La cantidad de vocales es es: %d \n', cont);

params= cell(1,2);
params{1,1}=strt;
params{1,2}=cont;

save('Num.txt','strt','cont','-ascii');
fprintf('Vocales Totales: %d \n',cont);

conn = pq_connect(setdbopts('dbname','HWP','host','localhost',
'port','5432','user','postgres','password','123fgthg'));
N=pq_exec_params(conn, "insert into numvocg(palabra, numvoc) values($1,$2);",params); %insertar datos en la tabla