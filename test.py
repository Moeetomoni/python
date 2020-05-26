# -*-coding:utf-8 -*

import math
import os

maxOfInterval = 100;
limite = 12;
pointer = maxOfInterval / 2;
ecart = math.fabs(limite - pointer);
i = 1;

while(ecart >= 1) :
    if(pointer < limite) :
      ecart = math.fabs(limite - pointer);
      pointer = pointer + (math.fabs(limite - pointer) / 2);

    elif(pointer > limite) :
      ecart = math.fabs(limite - pointer);
      pointer = pointer - (math.fabs(limite - pointer) / 2);

    else :
      ecart = 1;

    print('pointer : ', pointer, ' - limite : ', limite, ' - ecart : ', ecart, ' - i : ', i);

    i += 1;

print('Resut : ', i);
os.system("pause")