# backend

```shell
python manage.py makemigrations 
python manage.py migrate 
```

# 后端部署

## 服务器

IP：43.138.29.81

ssh登录端口：22

用户名：ubuntu

密码：123qweASD

*可以用xshell连接*

## 项目更新

```bash
cd ~/backend
git pull
```

## 运行与停止

git pull之后可能要重新添加脚本的权限

```bash
cd ~/backend/djangoProject
chmod +777 start.sh
chmod +777 stop.sh
```

启动(关闭终端后依然有效)

```bash
./start.sh
```

关闭

```bash
./stop.sh
```

输出日志：nohup.out

## 访问api

http://43.138.29.81:8080/api/

