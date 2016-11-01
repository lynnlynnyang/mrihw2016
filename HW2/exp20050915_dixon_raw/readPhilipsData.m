
fp=fopen('cpx_101.data', 'rb');
d = fread(fp, ([256*2 256]), 'float');
fclose(fp);
d1= d(1:2:end,:) + i* d(2:2:end,:);
fp=fopen('cpx_102.data', 'rb');
d = fread(fp, ([256*2 256]), 'float');
fclose(fp);

d2= d(1:2:end,:) + i* d(2:2:end,:);



