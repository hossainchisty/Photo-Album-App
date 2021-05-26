

*A Photo Album App made with Django framework in the backend. Tailwindcss for the frontend. I will host Images on AWS S3 Buckets in few days later.*

# Photo Album Features:
* Sign Up.
* Sign In.
* Password Reset with email.
* Add Image with title, description and category.
* Update Image with title, description and category.
* Delete Image with title, description and category.
* Search with Image title.
* User can change Profile picture/cover Image/Bio/Full Name.
* User-friendly.

## Setup, Installation and Run

To run the app on your local machine, you need Python 3+, installed on your computer. Follow all the steps to run this project.
   
1.  Create `venv` virtual environment:
```bash
virtualenv virtualenv_name
```
    
2.  Activate `venv` virtual environment:
```bash
On Linux - source virtualenv_name/bin/activate
On Windows - virtualenv_name/Scripts/activate
```

3. Firstly you need to clone or download my project from github repositories:
```bash
git clone https://github.com/hossainchisty/Photo-Album-App.git
```

4. Then enter the corresponding directory:
```bash
cd Photo-Album-App
```
    
5. Install all the requirements using pip:
```python
pip install -r requirements.txt
``` 

6.	Run server:
```python
  python manage.py runserver
```

7. Then go to ```http://127.0.0.1:8000``` in your browser
8. Create Admin
```
 python manage.py createsuperuser
```
9. Access the admin dashboard ```http://127.0.0.1:8000/admin```

### Home 
![Image of demo](https://github.com/hossainchisty/Photo-Album-App/blob/master/demo/homepage.png)

### Add Image 
![Image of demo](https://github.com/hossainchisty/Photo-Album-App/blob/master/demo/addphoto.png)

### Update and Delete Image 
![Image of demo](https://github.com/hossainchisty/Photo-Album-App/blob/master/demo/updatephoto.png)

### View Image 
![Image of demo](https://github.com/hossainchisty/Photo-Album-App/blob/master/demo/viewphoto.png)

### User Profile
![Image of demo](https://github.com/hossainchisty/Photo-Album-App/blob/master/demo/userprofile.png)

### Sign Up
![Image of demo](https://github.com/hossainchisty/Photo-Album-App/blob/master/demo/sign-up.png)

### Sign In
![Image of demo](https://github.com/hossainchisty/Photo-Album-App/blob/master/demo/sign-in.png)

### Password Rest
![Image of demo](https://github.com/hossainchisty/Photo-Album-App/blob/master/demo/password-rest.png)

### Thanks ❤ 
