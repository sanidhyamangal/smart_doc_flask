# Smart Doc Flask
A Flask based App for perfroming diagnosis of Malaria cells and Chest X-ray for pneumonia detection. 

### Docker Pull command:
```cmd
docker pull sanidhyamangal/smart_doc
```

### [Github link](https://github.com/sanidhyamangal/smart_doc_flask)

### Requirements
```txt
flask==1.1.1
gunicorn==20.0.4
tensorflow==2.1.0
```

### Project Setup
* Unzip the files in uploads section and then run following commands to serve this application
#### Without Docker
```shell
python app.py 
```
#### With Docker
```shell
docker-compose up -d
```
