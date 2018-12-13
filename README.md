 # GALLERY
 #### Description
 This is my personal gallery website where you can see photos that i have uploaded and can also copy the photo link.
 
 # Author
 Aluoch Sheila
 
 ## As A user you can :
 * View different photos that interest me.
 * Click on a single photo to expand it and view the details of the photo.
 * View different categories of photos.
 * Copy a link to the photo to share with my friends.
 * View photos based on the location they were taken.
 
## Usage example
1. Open the website and browse the images.
2. If  image captures your attention  you you can click on it to view in a better size
2. If  image captures your attention  you you can click on it to view in a better size\
 ## Specifications
| Behaviour | Input | Output |
| :---------------- | :---------------: | ------------------: |
| Display all images | **Home page** | Clickable links to open any images in a modal |
| Display single images on click | **On  click** | All details should be viewed|
| To add an image  | **Through Admin dashboard** | Add and add categories and tag location of Image|
| To edit image  | **Through Admin dashboard** | Redirected to the  image form details and editing happens|
| To delete an image  | **Through Admin dashboard** | click on image object and confirm by delete button|

 ## Development setup
  To access  this site Coding system  , you will need to:
 
 1. Clone this repo:
   git clone https://github.com/aluoch-sheila/GALLERY.git

 2. Move to the folder and install requirements
   cd My-gallery
   pip install -r requirements.txt
   
 3. Create database on psql shell
 
   psql
   CREATE DATABASE pictures;
 
 4. Migrate the database and run the application
 
   python manage.py migrate
   python manage.py runserver
 
 ##Django admin
  Username: Sheila
  Password: lastborn20
  
 ## Technologies Used
 * python3:Django
 * Flask :Jinja
 * HTML & CSS
 * Bootstrap
 * Heroku
 * Git
 
 ## Known Bugs
 * There are currently no known bugs. If you experience any feel free to open an issue
 or contact me personally.
 
 ### Support and contact details
 If you have any queries regarding the my site,
 Please feel free to contact on [gmail](aluochsheila1999@gmail.com) and we will be happy to look into your query
 
 ## Licensing
  This Project is under the MIT License 2018
