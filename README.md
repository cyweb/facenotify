facenotify
==========



[facebook notify](http://www.youtube.com/watch?v=qNkOQW3JYYU)

How to Work
===========

1- Fisrt you need to install [notify2](https://bitbucket.org/takluyver/pynotify2) python3 package

2- Click [Facebook Notification](https://www.facebook.com/notifications) and copy RSS link, paste it file as "id" 
something like -> "https://www.facebook.com/feeds/notifications.php?id=**************&viewer=**************&key=**************&format=rss20" 
Do not share this link anyone !!!

3- Edit notifications.py.desktop Exec=python3 /home/your_username/facenotify/notifications.py and move it /home/YOUR_USER_NAME/.config/autostart/ 

4- Restart session

Nasıl Çalışır
=============

1- Öncelikle [notify2](https://bitbucket.org/takluyver/pynotify2) python3 paketine ihtiyacımız olacak.

2- Tıkla [Facebook Notification](https://www.facebook.com/notifications) ve RSS linkini kopyaladıktan sonra "id" adlı dosyaya yapıştır. 
RSS linki şuna benzer -> "https://www.facebook.com/feeds/notifications.php?id=**************&viewer=**************&key=**************&format=rss20"
Bu linki kimseyle paylaşma !!!

3- notifications.py.desktop daki Exec=python3 /home/your_username/facenotify/notifications.py satırını düzenle ve bu dosyayı /home/KULLANICI_ADIN/.config/autostart/ taşı.

4- Oturumu yeniden başlat
