# Welcome to  file upload Python project!

To manually create a virtualenv on MacOS and Linux:


```
$ python3 -m venv .venv
After the init process completes and the virtualenv is created, you can use the following step to activate your virtualenv.
```


```
$ source .venv/bin/activate
If you are a Windows platform, you would activate the virtualenv like this:
```

```
% .venv\Scripts\activate.bat
Once the virtualenv is activated, you can install the required dependencies.
```


```
Before installing requirements you should know which platform your installing the requirements
if it is windows as it is below mentioned command
```


```
$ pip install -r requirements.txt
At this point you can now synthesize the CloudFormation template for this code.
```

```
on MacOS and Linux:
Comment pywin32==303 & pypiwin32==223 & python-ldap in requirements.txt then run the as it is
$ pip install -r requirements.txt

```


```
Run Your Project in Locally:
$ python manage.py runserver 
```

```buildoutcfg
Rest API - 

1)Login API - login api we are using JWT toekn

* url- {{ip}}/api/login/

request body -
{
    
    "username":"mayur",
    "password":"Pass123#$"
    

}

Response body - 
{
    "access": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjc3MTIxMzU5LCJpYXQiOjE2NzUzOTMzNTksImp0aSI6IjZjNWM1NDdlYmUxOTQwMGM5MjJhNzRlZTQ0NDIxOWNhIiwidXNlcl9pZCI6M30.OdJbzmSrs4tRLdm6Ez5lzvyFgK-7oqh4oZCTvXXWfUw",
    "username": "mayur",
    "group": "staff",
    "user_id": 3
}


Note - Access token reuired in all api   

Brearer Token -"eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjc3MTIxMzU5LCJpYXQiOjE2NzUzOTMzNTksImp0aSI6IjZjNWM1NDdlYmUxOTQwMGM5MjJhNzRlZTQ0NDIxOWNhIiwidXNlcl9pZCI6M30.OdJbzmSrs4tRLdm6Ez5lzvyFgK-7oqh4oZCTvXXWfUw"
2)upload any file using form data
url - {{ip}}/uploader/file_upload/      Type - POST

request body -
upload_file - "jpg/png/csv/pdf file"

Response body
{
    "status": "success",
    "data": {
        "id": 12,
        "upload_file": "/media/pma-ERD.pdf",
        "upload_date": "2023-02-03T04:30:28.724283Z"
    }
}

3) List of Uploaded file  

url - {{ip}}/uploader/file_upload/      Type - GET

Response body -

{
    "status": "success",
    "students": [
        {
            "id": 14,
            "upload_file": "/media/pickerapp.postman_collection_bitu",
            "upload_date": "2023-02-03T04:36:31.344907Z"
        },
        {
            "id": 15,
            "upload_file": "/media/Screenshot_35.png",
            "upload_date": "2023-02-03T04:36:52.555011Z"
        },
        {
            "id": 16,
            "upload_file": "/media/pma-ERD.pdf",
            "upload_date": "2023-02-03T04:37:02.039733Z"
        },
        {
            "id": 18,
            "upload_file": "/media/ADFS_Active_3_3.csv",
            "upload_date": "2023-02-03T04:37:25.068977Z"
        },
        {
            "id": 19,
            "upload_file": "/media/MoreRetail-Invoice-159412652.pdf",
            "upload_date": "2023-02-03T04:38:21.967417Z"
        },
        {
            "id": 21,
            "upload_file": "/media/Screenshot_170.png",
            "upload_date": "2023-02-03T04:40:41.456699Z"
        }
    ]
}


4) Download file:

url - localhost:8000/uploader/download/{{pk}}/   type  - GET
response  - file data show in text format but you can download the file from  the frontend side

```
* Note --  go to the http://localhost:8000/uploader/ url you will see the uploded items on browser as well as you can download that items with password protected

* password - teacher 
