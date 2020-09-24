# Dashboard luyện học từ mới toeic (Vuejs + Python)
## Test bot
* Search trên telegram bot 'LoveYourSmile'
* Bắt đầu bằng lệnh '/study'
## Các bước kiểm tra
* Từ vựng được chia theo chủ đề, chọn chủ để để tiến hành ôn tập. 
* Có kết quả số câu đúng khi kết thúc kiểm tra
* Những câu sai sẽ được lưu vào topic 'memo' để kiểm tra lại, vào tự xóa sau khi trả lời đúng hoặc sau 7 ngày

| 1 | 2 | 
| --- | --- |
| ![Screenshot from 2020-09-24 11-11-19](https://user-images.githubusercontent.com/36092539/94100067-c3922980-fe56-11ea-8e98-468e2c710658.png) | ![Screenshot from 2020-09-24 11-13-39](https://user-images.githubusercontent.com/36092539/94100154-0a801f00-fe57-11ea-8eda-63413828dce6.png)|
## Build và deploy code
| Chọn chủ đề | Kiểm tra | Kiểm tra lại câu sai |
| --- | --- | --- |
| ![Screenshot from 2020-09-24 11-20-28](https://user-images.githubusercontent.com/36092539/94100478-fc7ece00-fe57-11ea-8dd7-feb86125e473.png) | ![Screenshot from 2020-09-24 11-21-34](https://user-images.githubusercontent.com/36092539/94100553-2801b880-fe58-11ea-8dfc-ac237b744335.png)| ![Screenshot from 2020-09-24 11-24-48](https://user-images.githubusercontent.com/36092539/94100802-a8c0b480-fe58-11ea-9cb5-e31ec30b41c7.png)

## Build và deploy code
![Screenshot from 2020-09-24 11-26-57](https://user-images.githubusercontent.com/36092539/94100906-f4735e00-fe58-11ea-9851-ce2a4998682a.png)

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