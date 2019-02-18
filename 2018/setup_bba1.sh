#mkdir miniAOD
#cd miniAOD

#cp -r /mnt/t3nfs01/data01/shome/ytakahas/work/prod/private_bba1/forKorbinian/* .

sed -i "s,\#\$ -o .*,\#\$ -o $PWD/job/,g" submit_Yuta.sh
sed -i "s,\#\$ -e .*,\#\$ -e $PWD/job/,g" submit_Yuta.sh
sed -i "s,^BASEDIR=.*,BASEDIR=\'$PWD\'," submit_Yuta.sh
sed -i "s,USER.*=.*,USER = \'$USER\'," *.py