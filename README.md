# recommendation-service

## 基于Flask Web框架开发推荐系统的服务端程序

#### 创建独立虚拟环境
```bash
# conda create --name recommendation-service python==3.7
```

#### 激活独立虚拟环境
```bash
# conda activate recommendation-service
```

#### 安装Flask
```bash
# pip install flask
```

#### 运行项目
```bash
# make run
```

#### 访问项目
```bash
# curl http://localhost:5000
```

#### 测试访问两个数乘积的路由地址
```bash
# curl -X POST \
  -H "Content-Type: application/json" \
  -d '{"m":5,"n":6}' \
  http://localhost:5000/hello_multiply

# curl http://localhost:5000/hello_multiply?m=5&n=6
```