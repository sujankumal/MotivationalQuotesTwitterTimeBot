@echo off
START C:\xampp\xampp-control.exe
timeout /t 60
cmd /k "cd /d C:\Users\sujan\Desktop\Ovenv\Scripts & activate & cd /d C:\Users\sujan\Desktop\MoticationalTweet & python tweetmotivation.py"
