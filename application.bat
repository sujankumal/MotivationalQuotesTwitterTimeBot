@echo off
START C:\xampp\mysql\bin\mysqld.exe
timeout /t 60
@REM cmd /k "cd /d C:\Users\sujan\Desktop\Ovenv\Scripts & activate & cd /d C:\Users\sujan\Desktop\MoticationalTweet & python tweetmotivation.py"
cmd /k "cd /d C:\Users\sujan\Desktop\MoticationalTweet & dist\tweetmotivation.exe"
