# Tự động gửi thông báo những từ mới, hay quên qua telegram. Nhắc nhở luyện tập bài dịch, nghe...
* Gửi từ vựng trước, sau một phút gửi nghĩa tiếng việt
* Gửi những nhắc nhở khác vào thời gian phù hợp như thời tiết, hoặc một bài báo công nghệ crawl tự động về (chỉnh sửa tại file crontab)
![Screenshot from 2020-09-24 10-54-18](https://user-images.githubusercontent.com/36092539/94099132-69906480-fe54-11ea-8cb7-823be198d028.png)

## Build và deploy code, đặt crontab
* Thay đổi thông tin tại file docker /.env (build 3 container: redis, bot-core, mongo)
* Chạy lệnh sau để build tại localhost:
```bash
set .env && docker-compose up -d --build
```
![Screenshot from 2020-09-23 16-11-05](https://user-images.githubusercontent.com/36092539/93992271-8d519d00-fdb7-11ea-8e18-a51c0ee062c2.png)

Deploy code lên host:
* Thay host tại file /deployment/hosts
* Chạy ansible để deploy + run container trên host:
```bash
ansible-playbook -i deployment/hosts deployment/site.yml -l telebot -t telebot -u {username}
```