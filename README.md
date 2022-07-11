# Django REST Image Upload Example
This API Example allows any user to upload an image in PNG or JPG format.

Details/ main functionalities of the app:
- users are created via admin panel
- users are grouped in 3 main Plans:
    - Basic:
        - upon uploading an image users get a link directing to the thumbnail of the picture (200px height)
    - Premium:
        - Same options as in 'Basic' Plan, additionally:
        - upon uploading an image users get a link directing to the thumbnail of the picture (400px height),
        - upon uploading an image users get a link directing to the originally uploaded image
    - Enterprise:
        - Same options as in 'Premium' Plan, additionally:
        - upon uploading an image users get a link directing to the binary image on the uploaded picture which expires after a number of seconds (user can specify any number between 300 and 30000)
- users are able to list their images
- when administrators create new Plans they can customize:
    - thumbnail sizes,
    - presence of the link to the originally uploaded file (bool field)
    - ability to generate expiring links (bool field)

# Assumptions
- The time in seconds provided by the user for Expiring links, for plan 'Enterprise' is counted from the time the original image was uploaded
- Users should only be able to access the app after being authenticated
- Users should only be able to see their own images
- Binary images, created for 'Enterprise' Plan should be represented by a black - white picture (not by a binary number format such as e.g. "001101000...")
- Urls to all images, thumbnails, binary pictures should be given a unique identifier, so the user cannot deduct different filenames seeing one in the address bar, in the browser
- For performance considerations images should not be saved in the database as such, just figure as serialized representation of themselves kept in the database (memo for future development)


## Quick Start
Installation Steps
```bash
git clone https://github.com/Woodchucks/django_rest_image_upload.git
cd django_rest_image_upload
mkdir media
py -m venv venv
.\venv\Scripts\activate
pip install -r requirements.txt
cd django_rest_image_upload
py manage.py migrate
py manage.py runserver
```

## Run app on http://127.0.0.1:8000/api/

## Requirements
- asgiref==3.5.2
- codegen==1.0
- Django==4.0.6
- django-appconf==1.0.5
- django-patterns==0.0.3
- djangorestframework==3.13.1
- et-xmlfile==1.1.0
- numpy==1.23.0
- openpyxl==3.0.10
- patterns==0.3
- pilkit==2.0
- Pillow==9.2.0
- pytz==2022.1
- six==1.16.0
- sqlparse==0.4.2
- tzdata==2022.1
- views==0.3

Please see [requirements.txt](requirements.txt) for more information.

## Docker Image
TBD
