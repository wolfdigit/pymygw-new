#!/bin/sh

cd /root
rm -rf pymygw-new
wget http://oj.lssh.tp.edu.tw/pymygw.tgz -O - | tar xzvf -
cd pymygw-new
pip install --upgrade pip
rm -rf /root/.cache/pip
mkdir /root/.cache
mkdir /tmp/cache_pip
ln -s /tmp/cache_pip /root/.cache/pip
pip install -r requirements.txt

pip install sqlite-web
head -n 11 /usr/lib/python2.7/site-packages/sqlite_web/sqlite_web.py > /tmp/sqlite_web.py
echo "#import webbrowser" >> /tmp/sqlite_web.py
tail -n +13 /usr/lib/python2.7/site-packages/sqlite_web/sqlite_web.py >> /tmp/sqlite_web.py
mv -f /tmp/sqlite_web.py /usr/lib/python2.7/site-packages/sqlite_web/sqlite_web.py

head -n -4 /etc/rc.local > /tmp/rc.local
echo "cd /root/pymygw-new/" >> /tmp/rc.local
echo "python app.py 2>&1 >> log.txt &" >> /tmp/rc.local
echo "sqlite_web -x -H 0.0.0.0 pymygw.db &" >> /tmp/rc.local
echo "exit 0" >> /tmp/rc.local
mv -f /tmp/rc.local /etc/rc.local
