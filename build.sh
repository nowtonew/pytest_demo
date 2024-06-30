echo "运行容器python执行自动化"
#-w=$WORKSPACE:指定workspace
#--volumes-from=pyjenkins：将Jenkins容器中的workspace映射到python容器中
docker run --rm -w=$WORKSPACE --volumes-from=pyjenkins python3:pydemo
echo "auto run success!"
