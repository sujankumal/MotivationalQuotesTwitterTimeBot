@echo off
START C:\xampp\mysql\bin\mysqld.exe
cmd /k "cd /d C:\Users\sujan\Desktop\Ovenv\Scripts & activate & cd /d C:\Users\sujan\Desktop\MoticationalTweet & python tweetmotivation.py"
