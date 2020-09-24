# Backend dashboard (Python Flask)
## Project Structure
    ├── deployment                   // deploy với ansible, run api bằng docker
    ├── src                          // main source code
    │   ├── db                      // các truy vẫn mongodb
    │   ├── main                    // api cho frontend
    │   ├── settings                // câu hình db
    │   ├── utils                   // funtion cho main.py
    ├── nginx.conf                  // cấu hình nginx cho api
    └── requirements.json           // những thư viện cần thiết cho api
## Build và deploy code
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