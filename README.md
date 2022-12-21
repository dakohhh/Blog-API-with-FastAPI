# DCLR  BACKEND 

## Installation

Use the bash command:

```bash
npm install 
```


## 1. Navigate To database.js and consfigure your database connection
Execute the function create_database()

```javascript
export function create_database(){

    let con = mysql.createConnection({
    host: "yourhostname or localhost",
    user: "yourusername",
    password: "your password"
    });

	.....

create_database()

```

## 2. Navigate To schema.sql and execute the database schema

```sql
CREATE TABLE carginie_users(id INTEGER PRIMARY KEY .....
```


## IMPORTANT!!! PLEASE MAKE ALL FORM FIELD REQUIRED TO PREVENT ERROR


## 3. Test API ENDPOINT
http://localhost:3000/api
### 


```javascript

var axios = require("axios").default;

var options = {method: 'GET', url: 'http://localhost:3000/api/'};

axios.request(options).then(function (response) {
  console.log(response.data);
}).catch(function (error) {
  console.error(error);
});
```

### Response:
```bash
Welcome to Carginie!
```

## 4A. Test API ENDPOINT -> SIGNUP USERS
http://localhost:3000/api/signup
### 


```javascript
import axios from "axios";

let headersList = {
 
}

let formdata = new FormData();
formdata.append("first_name", "Wisdom");
formdata.append("last_name", "Dakoh");
formdata.append("password", "blackbird");
formdata.append("email", "cargenie@gmail.com");

let bodyContent =  formdata;

let reqOptions = {
  url: "http://localhost:3000/api/signup",
  method: "POST",
  headers: headersList,
  data: bodyContent,
}

let response = await axios.request(reqOptions);
console.log(response.data);

```

### Response:
```json
{
  "data": {
    "first_name": "Wisdom",
    "last_name": "Dakoh",
    "user_id": "rhuMAG",
    "email": "cargenie@gmail.com",
    "phone_number": null
  }
}
```
### Response 2:
```json
{
  "msg": "email_already_exist"
}
```

### Response 3:
```json
{
  "msg": "Error_occured"
}
```


## 4B. Test API ENDPOINT -> LOGIN USERS
http://localhost:3000/api/login
### 


```javascript
import axios from "axios";

let headersList = {
 
}

let formdata = new FormData();
formdata.append("email", "cargenie@gmail.com");
formdata.append("password", "blackbird");

let bodyContent =  formdata;

let reqOptions = {
  url: "http://localhost:3000/api/login",
  method: "POST",
  headers: headersList,
  data: bodyContent,
}

let response = await axios.request(reqOptions);
console.log(response.data);

```

### Response:
```json
{
  "data": {
    "first_name": "Wisdom",
    "last_name": "Dakoh",
    "user_id": "rhuMAG",
    "email": "cargenie@gmail.com",
    "phone_number": null // not_null if phone number is verified =>(check 6.)
  }
}
```
### Response 2:
```json
{
  "msg": "incorrect_email_or_password"
}
```

### Response 3:
```json
{
  "msg": "Error_occured"
}
```
### IMPORTANT!!! PLEASE MAKE ALL FORM FIELD REQUIRED TO PREVENT ERROR


## 5. Test API ENDPOINT -> PROFILE IMAGE UPLOAD
http://localhost:3000/api/upload_profile_pic/:user_id
### 


```javascript
import axios from "axios";
var fs = require('fs');

let headersList = {
 
}

let formdata = new FormData();
formdata.append("profile", fs.createReadStream("C:\Users\Hp\Pictures\New folder\ProfilePhoto young wisdom.jpg"));

let bodyContent =  formdata;

let reqOptions = {
  url: "http://localhost:3000/api/update_profile_pic/d66kLI",
  method: "PUT",
  headers: headersList,
  data: bodyContent,
}

let response = await axios.request(reqOptions);
console.log(response.data);

```

### Response:
```json
{
  "msg": "profile_pic_updated"
}
```
### Response 2:
```json
{
  {
  "msg": "image_wasnt_provided"
}
}
```

### Response 3:
```json
{
  {
  "msg": "Error_occured"
}
}
```
### Response 4:
```json
{
  "msg": "user_id_does_not_exist"
}
```
### Response 4:
```json
{
  "msg": "user_id_wasnt_provided"
}
```

### IMPORTANT!!! PLEASE MAKE ALL FORM FIELD REQUIRED TO PREVENT ERROR


## 6. Test API ENDPOINT -> VERIFY AND UPDATE USER PHONE NUMBER
http://localhost:3000/api/verify_and_update_phone_number/:user_id
### 


```javascript
import axios from "axios";

let headersList = {
 
}

let formdata = new FormData();
formdata.append("phone_number", "07052316803");

let bodyContent =  formdata;

let reqOptions = {
  url: "http://localhost:3000/api/verify_and_update_phone_number/d66kLI",
  method: "POST",
  headers: headersList,
  data: bodyContent,
}

let response = await axios.request(reqOptions);
console.log(response.data);

```

### Response:
```json
{
  "msg": "phone_number_verified_and_updated"
}
```
### Response 2:
```json
{
  {
  "msg": "not_a_valid_number"
}
}
```

### Response 3:
```json
{
  {
  "msg": "user_id_does_not_exist"
}
}
```
### Response 4:
```json
{
  "msg": "phone_number_wasnt_provided"
}
```
### Response 5:
```json
{
  "msg": "id_wasnt_provided"
}
```







## 7. Test API ENDPOINT -> PASSWORD RESET
http://localhost:3000/api/password_reset/:user_id
### 


```javascript
import axios from "axios";

let headersList = {
 
}

let formdata = new FormData();
formdata.append("new_password", "wisdomdakoh12");

let bodyContent =  formdata;

let reqOptions = {
  url: "http://localhost:3000/api/password_reset/d66kLI", // user_id => d66kLI
  method: "POST",
  headers: headersList,
  data: bodyContent,
}

let response = await axios.request(reqOptions);
console.log(response.data);

```

### Response:
```json
{
  "msg": "password_reset_successfull"
}
```
### Response 2:
```json
{
  {
  "msg": "new_password_wasnt_provided"
}
}
```

### Response 3:
```json
{
  {
  "msg": "user_id_does_not_exist"
}
}
```
### Response 4:
```json
{
  "msg": "Error_occured"
}
```



## 8. Test API ENDPOINT -> UPDATE FIRST NAME 
http://localhost:3000/api/update_first_name/:user_id
### 


```javascript
import axios from "axios";

let headersList = {
 
}

let formdata = new FormData();
formdata.append("first_name", "Wisdom");

let bodyContent =  formdata;

let reqOptions = {
  url: "http://localhost:3000/api/update_first_name/d66kLI", // user_id => d66kLI 
  method: "PUT",
  headers: headersList,
  data: bodyContent,
}

let response = await axios.request(reqOptions);
console.log(response.data);

```

### Response:
```json
{
  "msg": "first_name_updated"
}
```
### Response 2:
```json
{
  {
  "msg": "name_wasnt_provided"
}
}
```

### Response 3:
```json
{
  {
  "msg": "user_id_does_not_exist"
}
}
```
### Response 4:
```json
{
  "msg": "Error_occured"
}
```



## 9. Test API ENDPOINT -> HOST LISTING CAR/VEHICLE  
http://localhost:3000/api/host_list_car/:user_id
### 


```javascript
import axios from "axios";
var fs = require('fs');

let headersList = {
 
}

let formdata = new FormData();
formdata.append("vehicle_make", "Toyota");
formdata.append("vehicle_type", "yeaj");
formdata.append("number_of_seats", "4");
formdata.append("year_of_make", "2009");
formdata.append("colour", "blue");
formdata.append("transmission", "wewee");
formdata.append("odometer", "wewewe");
formdata.append("is_bluetooth", "1"); // TRUE OR FALSE(MUST BE IN STRING->use 1 for true 0 for false)
formdata.append("is_wheel_chair", "1"); // TRUE OR FALSE
formdata.append("is_gps", "1"); // TRUE OR FALSE
formdata.append("is_usb", "0"); // TRUE OR FALSE
formdata.append("is_heated", "0"); // TRUE OR FALSE
formdata.append("is_bike", "1"); // TRUE OR FALSE
formdata.append("is_child", "1"); // TRUE OR FALSE
formdata.append("is_back_camera", "1"); // TRUE OR FALSE
formdata.append("is_navigation", "1"); // TRUE OR FALSE
formdata.append("proof_of_own_number", "2323232323");
formdata.append("pickup_location", "sdfsd");
formdata.append("drop_off_location", "sdfsdfd");
formdata.append("price", "1221");
formdata.append("bank_name", "wisdomBnxk");
formdata.append("bank_account_name", "wisdomdakoh");
formdata.append("bank_account_number", "112121211221221");
formdata.append("proof_of_own_photo", fs.createReadStream("C:\Users\Hp\Pictures\New folder\ProfilePhoto young wisdom.jpg"));
formdata.append("vehicle_registration", fs.createReadStream("C:\Users\Hp\Pictures\New folder\ProfilePhoto young wisdom.jpg"));
formdata.append("certificate_of_road", fs.createReadStream("C:\Users\Hp\Pictures\New folder\ProfilePhoto young wisdom.jpg"));
formdata.append("insurance", fs.createReadStream("C:\Users\Hp\Pictures\New folder\ProfilePhoto young wisdom.jpg"));
formdata.append("front_view_image", fs.createReadStream("C:\Users\Hp\Pictures\New folder\ProfilePhoto young wisdom.jpg"));
formdata.append("back_view_image", fs.createReadStream("C:\Users\Hp\Pictures\New folder\ProfilePhoto young wisdom.jpg"));
formdata.append("right_side_image", fs.createReadStream("C:\Users\Hp\Pictures\New folder\ProfilePhoto young wisdom.jpg"));
formdata.append("left_side_image", fs.createReadStream("C:\Users\Hp\Pictures\New folder\ProfilePhoto young wisdom.jpg"));
formdata.append("dashboard_view_image", fs.createReadStream("C:\Users\Hp\Pictures\New folder\ProfilePhoto young wisdom.jpg"));
formdata.append("front_seat_image", fs.createReadStream("C:\Users\Hp\Pictures\New folder\ProfilePhoto young wisdom.jpg"));
formdata.append("back_seat_image", fs.createReadStream("C:\Users\Hp\Pictures\New folder\ProfilePhoto young wisdom.jpg"));
formdata.append("trunk_view_image", fs.createReadStream("C:\Users\Hp\Pictures\New folder\ProfilePhoto young wisdom.jpg"));

let bodyContent =  formdata;

let reqOptions = {
  url: "http://localhost:3000/api/host_list_car/YzOHgX", // user_id => YzOHgX
  method: "POST",
  headers: headersList,
  data: bodyContent,
}

let response = await axios.request(reqOptions);
console.log(response.data);

```

### Response:
```json
{
  "msg": "vehicle_listed"
}
```
### Response 2:
```json
{
  {
  "msg": "user_id_does_not_exist"
}
}
```
### Response 3:
```json
{
  "msg": "Error_occured"
}
```








## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.


Please make sure to update tests as appropriate.


## Contact Information

Email: wiizzydreadmill@gmail.com

Linkedin Profile: https://www.linkedin.com/in/wisdomdakoh/

Made with ❤️ By Wisdom Dakoh