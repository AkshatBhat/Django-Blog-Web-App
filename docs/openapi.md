<!-- Generator: Widdershins v4.0.1 -->

<h1 id="django-blog">Django Blog v1</h1>

> Scroll down for code samples, example requests and responses. Select a language for code samples from the tabs above or the mobile navigation menu.

This is the API documentation for my [Django Blog](https://thenewdjangoblogapp.herokuapp.com/) web app! Using Postman, cURL, Python requests or any other framework or tool you can send requests just the way you would using the GUI.

Remember to include the Authorization Header with the auth token string as value for requests that require authentication!

Base URLs:

* <a href="http://thenewdjangoblogapp.herokuapp.com/api">http://thenewdjangoblogapp.herokuapp.com/api</a>

 License: 

<h1 id="django-blog-user">User</h1>

## RegisterUser

<a id="opIdRegisterUser"></a>

> Code samples

```shell
# You can also use wget
curl -X POST http://thenewdjangoblogapp.herokuapp.com/api/user/register/ \
  -H 'Content-Type: multipart/form-data' \
  -H 'Accept: application/json'

```

```http
POST http://thenewdjangoblogapp.herokuapp.com/api/user/register/ HTTP/1.1
Host: thenewdjangoblogapp.herokuapp.com
Content-Type: multipart/form-data
Accept: application/json

```

```javascript
const inputBody = '{
  "username": "Falcao2",
  "email": "falcao@gmail.com",
  "password": "falcao@123",
  "password2": "falcao@123"
}';
const headers = {
  'Content-Type':'multipart/form-data',
  'Accept':'application/json'
};

fetch('http://thenewdjangoblogapp.herokuapp.com/api/user/register/',
{
  method: 'POST',
  body: inputBody,
  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Content-Type' => 'multipart/form-data',
  'Accept' => 'application/json'
}

result = RestClient.post 'http://thenewdjangoblogapp.herokuapp.com/api/user/register/',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Content-Type': 'multipart/form-data',
  'Accept': 'application/json'
}

r = requests.post('http://thenewdjangoblogapp.herokuapp.com/api/user/register/', headers = headers)

print(r.json())

```

```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Content-Type' => 'multipart/form-data',
    'Accept' => 'application/json',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('POST','http://thenewdjangoblogapp.herokuapp.com/api/user/register/', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...

```

```java
URL obj = new URL("http://thenewdjangoblogapp.herokuapp.com/api/user/register/");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("POST");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Content-Type": []string{"multipart/form-data"},
        "Accept": []string{"application/json"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("POST", "http://thenewdjangoblogapp.herokuapp.com/api/user/register/", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`POST /user/register/`

*Register User*

Register a new user on this website.

> Body parameter

```yaml
username: Falcao2
email: falcao@gmail.com
password: falcao@123
password2: falcao@123

```

<h3 id="registeruser-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|object|true|Register a new user on this website.|
|» username|body|string|true|none|
|» email|body|string|true|none|
|» password|body|string|true|none|
|» password2|body|string|true|none|

> Example responses

> 201 Response

```json
{
  "success": "Successfully registered a new user.",
  "username": "<username>",
  "email": "<email>",
  "token": "<token>"
}
```

<h3 id="registeruser-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|none|None|
|201|[Created](https://tools.ietf.org/html/rfc7231#section-6.3.2)|Register User|[201](#schema201)|

<aside class="success">
This operation does not require authentication
</aside>

## LoginUser

<a id="opIdLoginUser"></a>

> Code samples

```shell
# You can also use wget
curl -X POST http://thenewdjangoblogapp.herokuapp.com/api/user/login/ \
  -H 'Content-Type: multipart/form-data' \
  -H 'Accept: application/json'

```

```http
POST http://thenewdjangoblogapp.herokuapp.com/api/user/login/ HTTP/1.1
Host: thenewdjangoblogapp.herokuapp.com
Content-Type: multipart/form-data
Accept: application/json

```

```javascript
const inputBody = '{
  "username": "{{username}}",
  "password": "{{password}}"
}';
const headers = {
  'Content-Type':'multipart/form-data',
  'Accept':'application/json'
};

fetch('http://thenewdjangoblogapp.herokuapp.com/api/user/login/',
{
  method: 'POST',
  body: inputBody,
  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Content-Type' => 'multipart/form-data',
  'Accept' => 'application/json'
}

result = RestClient.post 'http://thenewdjangoblogapp.herokuapp.com/api/user/login/',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Content-Type': 'multipart/form-data',
  'Accept': 'application/json'
}

r = requests.post('http://thenewdjangoblogapp.herokuapp.com/api/user/login/', headers = headers)

print(r.json())

```

```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Content-Type' => 'multipart/form-data',
    'Accept' => 'application/json',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('POST','http://thenewdjangoblogapp.herokuapp.com/api/user/login/', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...

```

```java
URL obj = new URL("http://thenewdjangoblogapp.herokuapp.com/api/user/login/");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("POST");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Content-Type": []string{"multipart/form-data"},
        "Accept": []string{"application/json"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("POST", "http://thenewdjangoblogapp.herokuapp.com/api/user/login/", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`POST /user/login/`

*Login User*

Used to obtain token for authentication for logging in.

> Body parameter

```yaml
username: "{{username}}"
password: "{{password}}"

```

<h3 id="loginuser-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|object|true|Used to obtain token for authentication for logging in.|
|» username|body|string|true|none|
|» password|body|string|true|none|

> Example responses

> 200 Response

```json
{
  "token": "<token>"
}
```

<h3 id="loginuser-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Login User|[200](#schema200)|

<aside class="success">
This operation does not require authentication
</aside>

## EditUserProfile

<a id="opIdEditUserProfile"></a>

> Code samples

```shell
# You can also use wget
curl -X PATCH http://thenewdjangoblogapp.herokuapp.com/api/user/profile/ \
  -H 'Content-Type: multipart/form-data' \
  -H 'Security: Token {{token}}'

```

```http
PATCH http://thenewdjangoblogapp.herokuapp.com/api/user/profile/ HTTP/1.1
Host: thenewdjangoblogapp.herokuapp.com
Content-Type: multipart/form-data

Security: Token {{token}}

```

```javascript
const inputBody = '{
  "file": "string",
  "username": "falcao",
  "email": "falcao@gmail.com"
}';
const headers = {
  'Content-Type':'multipart/form-data',
  'Security':'Token {{token}}'
};

fetch('http://thenewdjangoblogapp.herokuapp.com/api/user/profile/',
{
  method: 'PATCH',
  body: inputBody,
  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Content-Type' => 'multipart/form-data',
  'Security' => 'Token {{token}}'
}

result = RestClient.patch 'http://thenewdjangoblogapp.herokuapp.com/api/user/profile/',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Content-Type': 'multipart/form-data',
  'Security': 'Token {{token}}'
}

r = requests.patch('http://thenewdjangoblogapp.herokuapp.com/api/user/profile/', headers = headers)

print(r.json())

```

```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Content-Type' => 'multipart/form-data',
    'Security' => 'Token {{token}}',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('PATCH','http://thenewdjangoblogapp.herokuapp.com/api/user/profile/', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...

```

```java
URL obj = new URL("http://thenewdjangoblogapp.herokuapp.com/api/user/profile/");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("PATCH");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Content-Type": []string{"multipart/form-data"},
        "Security": []string{"Token {{token}}"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("PATCH", "http://thenewdjangoblogapp.herokuapp.com/api/user/profile/", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`PATCH /user/profile/`

*Edit User Profile*

Edit the user profile of the currently authorized user.

> Body parameter

```yaml
file: string
username: falcao
email: falcao@gmail.com

```

<h3 id="edituserprofile-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|Security|header|string|true|none|
|body|body|object|true|Edit the user profile of the currently authorized user.|
|» file|body|string(binary)|true|none|
|» username|body|string|true|none|
|» email|body|string|true|none|

<h3 id="edituserprofile-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|none|None|

<aside class="success">
This operation does not require authentication
</aside>

<h1 id="django-blog-post">Post</h1>

## GetPostList

<a id="opIdGetPostList"></a>

> Code samples

```shell
# You can also use wget
curl -X GET http://thenewdjangoblogapp.herokuapp.com/api/blog/posts/?page=0

```

```http
GET http://thenewdjangoblogapp.herokuapp.com/api/blog/posts/?page=0 HTTP/1.1
Host: thenewdjangoblogapp.herokuapp.com

```

```javascript

fetch('http://thenewdjangoblogapp.herokuapp.com/api/blog/posts/?page=0',
{
  method: 'GET'

})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

result = RestClient.get 'http://thenewdjangoblogapp.herokuapp.com/api/blog/posts/',
  params: {
  'page' => 'number'
}

p JSON.parse(result)

```

```python
import requests

r = requests.get('http://thenewdjangoblogapp.herokuapp.com/api/blog/posts/', params={
  'page': '0'
})

print(r.json())

```

```php
<?php

require 'vendor/autoload.php';

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('GET','http://thenewdjangoblogapp.herokuapp.com/api/blog/posts/', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...

```

```java
URL obj = new URL("http://thenewdjangoblogapp.herokuapp.com/api/blog/posts/?page=0");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("GET");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("GET", "http://thenewdjangoblogapp.herokuapp.com/api/blog/posts/", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`GET /blog/posts/`

*Get Post List*

Get the list of all the blog posts available on the website.

<h3 id="getpostlist-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|page|query|number|true|none|

<h3 id="getpostlist-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|none|None|

<aside class="success">
This operation does not require authentication
</aside>

## GetPostDetails

<a id="opIdGetPostDetails"></a>

> Code samples

```shell
# You can also use wget
curl -X GET http://thenewdjangoblogapp.herokuapp.com/api/blog/post/{pk}/

```

```http
GET http://thenewdjangoblogapp.herokuapp.com/api/blog/post/{pk}/ HTTP/1.1
Host: thenewdjangoblogapp.herokuapp.com

```

```javascript

fetch('http://thenewdjangoblogapp.herokuapp.com/api/blog/post/{pk}/',
{
  method: 'GET'

})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

result = RestClient.get 'http://thenewdjangoblogapp.herokuapp.com/api/blog/post/{pk}/',
  params: {
  }

p JSON.parse(result)

```

```python
import requests

r = requests.get('http://thenewdjangoblogapp.herokuapp.com/api/blog/post/{pk}/')

print(r.json())

```

```php
<?php

require 'vendor/autoload.php';

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('GET','http://thenewdjangoblogapp.herokuapp.com/api/blog/post/{pk}/', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...

```

```java
URL obj = new URL("http://thenewdjangoblogapp.herokuapp.com/api/blog/post/{pk}/");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("GET");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("GET", "http://thenewdjangoblogapp.herokuapp.com/api/blog/post/{pk}/", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`GET /blog/post/{pk}/`

*Get Post Details*

Get the details of a specific blog post.

<h3 id="getpostdetails-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|pk|path|number|true|none|

<h3 id="getpostdetails-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|none|None|

<aside class="success">
This operation does not require authentication
</aside>

## GetUserPosts

<a id="opIdGetUserPosts"></a>

> Code samples

```shell
# You can also use wget
curl -X GET http://thenewdjangoblogapp.herokuapp.com/api/user/{username}/

```

```http
GET http://thenewdjangoblogapp.herokuapp.com/api/user/{username}/ HTTP/1.1
Host: thenewdjangoblogapp.herokuapp.com

```

```javascript

fetch('http://thenewdjangoblogapp.herokuapp.com/api/user/{username}/',
{
  method: 'GET'

})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

result = RestClient.get 'http://thenewdjangoblogapp.herokuapp.com/api/user/{username}/',
  params: {
  }

p JSON.parse(result)

```

```python
import requests

r = requests.get('http://thenewdjangoblogapp.herokuapp.com/api/user/{username}/')

print(r.json())

```

```php
<?php

require 'vendor/autoload.php';

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('GET','http://thenewdjangoblogapp.herokuapp.com/api/user/{username}/', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...

```

```java
URL obj = new URL("http://thenewdjangoblogapp.herokuapp.com/api/user/{username}/");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("GET");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("GET", "http://thenewdjangoblogapp.herokuapp.com/api/user/{username}/", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`GET /user/{username}/`

*Get User Posts*

Get the list of all blog posts by a user.

<h3 id="getuserposts-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|username|path|string|true|none|

<h3 id="getuserposts-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|none|None|

<aside class="success">
This operation does not require authentication
</aside>

## UpdatePost

<a id="opIdUpdatePost"></a>

> Code samples

```shell
# You can also use wget
curl -X PUT http://thenewdjangoblogapp.herokuapp.com/api/blog/post/{pk}/update/ \
  -H 'Content-Type: text/plain' \
  -H 'Security: Token {{token}}'

```

```http
PUT http://thenewdjangoblogapp.herokuapp.com/api/blog/post/{pk}/update/ HTTP/1.1
Host: thenewdjangoblogapp.herokuapp.com
Content-Type: text/plain

Security: Token {{token}}

```

```javascript
const inputBody = '{
  "title": "{{$randomCatchPhrase}}",
  "content": "{{$randomCatchPhraseDescriptor}}",
  "date_posted": "{{todayDate}}"
}';
const headers = {
  'Content-Type':'text/plain',
  'Security':'Token {{token}}'
};

fetch('http://thenewdjangoblogapp.herokuapp.com/api/blog/post/{pk}/update/',
{
  method: 'PUT',
  body: inputBody,
  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Content-Type' => 'text/plain',
  'Security' => 'Token {{token}}'
}

result = RestClient.put 'http://thenewdjangoblogapp.herokuapp.com/api/blog/post/{pk}/update/',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Content-Type': 'text/plain',
  'Security': 'Token {{token}}'
}

r = requests.put('http://thenewdjangoblogapp.herokuapp.com/api/blog/post/{pk}/update/', headers = headers)

print(r.json())

```

```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Content-Type' => 'text/plain',
    'Security' => 'Token {{token}}',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('PUT','http://thenewdjangoblogapp.herokuapp.com/api/blog/post/{pk}/update/', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...

```

```java
URL obj = new URL("http://thenewdjangoblogapp.herokuapp.com/api/blog/post/{pk}/update/");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("PUT");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Content-Type": []string{"text/plain"},
        "Security": []string{"Token {{token}}"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("PUT", "http://thenewdjangoblogapp.herokuapp.com/api/blog/post/{pk}/update/", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`PUT /blog/post/{pk}/update/`

*Update Post*

Update a particular blog post.

> Body parameter

```
title: "{{$randomCatchPhrase}}"
content: "{{$randomCatchPhraseDescriptor}}"
date_posted: "{{todayDate}}"

```

<h3 id="updatepost-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|pk|path|number|true|none|
|Security|header|string|true|none|
|body|body|string|true|Update a particular blog post.|

<h3 id="updatepost-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|none|None|

<aside class="success">
This operation does not require authentication
</aside>

## CreatePost

<a id="opIdCreatePost"></a>

> Code samples

```shell
# You can also use wget
curl -X POST http://thenewdjangoblogapp.herokuapp.com/api/blog/post/new/ \
  -H 'Content-Type: text/plain' \
  -H 'Security: Token {{token}}'

```

```http
POST http://thenewdjangoblogapp.herokuapp.com/api/blog/post/new/ HTTP/1.1
Host: thenewdjangoblogapp.herokuapp.com
Content-Type: text/plain

Security: Token {{token}}

```

```javascript
const inputBody = '{
  "title": "{{$randomPhrase}}",
  "content": "{{$randomCatchPhraseDescriptor}}",
  "date_posted": "{{todayDate}}"
}';
const headers = {
  'Content-Type':'text/plain',
  'Security':'Token {{token}}'
};

fetch('http://thenewdjangoblogapp.herokuapp.com/api/blog/post/new/',
{
  method: 'POST',
  body: inputBody,
  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Content-Type' => 'text/plain',
  'Security' => 'Token {{token}}'
}

result = RestClient.post 'http://thenewdjangoblogapp.herokuapp.com/api/blog/post/new/',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Content-Type': 'text/plain',
  'Security': 'Token {{token}}'
}

r = requests.post('http://thenewdjangoblogapp.herokuapp.com/api/blog/post/new/', headers = headers)

print(r.json())

```

```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Content-Type' => 'text/plain',
    'Security' => 'Token {{token}}',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('POST','http://thenewdjangoblogapp.herokuapp.com/api/blog/post/new/', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...

```

```java
URL obj = new URL("http://thenewdjangoblogapp.herokuapp.com/api/blog/post/new/");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("POST");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Content-Type": []string{"text/plain"},
        "Security": []string{"Token {{token}}"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("POST", "http://thenewdjangoblogapp.herokuapp.com/api/blog/post/new/", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`POST /blog/post/new/`

*Create Post*

Create a new blog post.

> Body parameter

```
title: "{{$randomPhrase}}"
content: "{{$randomCatchPhraseDescriptor}}"
date_posted: "{{todayDate}}"

```

<h3 id="createpost-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|Security|header|string|true|none|
|body|body|string|true|Create a new blog post.|

<h3 id="createpost-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|none|None|

<aside class="success">
This operation does not require authentication
</aside>

## DeletePost

<a id="opIdDeletePost"></a>

> Code samples

```shell
# You can also use wget
curl -X DELETE http://thenewdjangoblogapp.herokuapp.com/api/blog/post/{pk}/delete/ \
  -H 'Security: Token {{token}}'

```

```http
DELETE http://thenewdjangoblogapp.herokuapp.com/api/blog/post/{pk}/delete/ HTTP/1.1
Host: thenewdjangoblogapp.herokuapp.com

Security: Token {{token}}

```

```javascript

const headers = {
  'Security':'Token {{token}}'
};

fetch('http://thenewdjangoblogapp.herokuapp.com/api/blog/post/{pk}/delete/',
{
  method: 'DELETE',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Security' => 'Token {{token}}'
}

result = RestClient.delete 'http://thenewdjangoblogapp.herokuapp.com/api/blog/post/{pk}/delete/',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Security': 'Token {{token}}'
}

r = requests.delete('http://thenewdjangoblogapp.herokuapp.com/api/blog/post/{pk}/delete/', headers = headers)

print(r.json())

```

```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Security' => 'Token {{token}}',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('DELETE','http://thenewdjangoblogapp.herokuapp.com/api/blog/post/{pk}/delete/', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...

```

```java
URL obj = new URL("http://thenewdjangoblogapp.herokuapp.com/api/blog/post/{pk}/delete/");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("DELETE");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Security": []string{"Token {{token}}"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("DELETE", "http://thenewdjangoblogapp.herokuapp.com/api/blog/post/{pk}/delete/", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`DELETE /blog/post/{pk}/delete/`

*Delete Post*

Delete an existing blog post.

<h3 id="deletepost-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|pk|path|number|true|none|
|Security|header|string|true|none|

<h3 id="deletepost-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|none|None|

<aside class="success">
This operation does not require authentication
</aside>

# Schemas

<h2 id="tocS_200">200</h2>
<!-- backwards compatibility -->
<a id="schema200"></a>
<a id="schema_200"></a>
<a id="tocS200"></a>
<a id="tocs200"></a>

```json
{
  "token": "<token>"
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|token|string|false|none|none|

<h2 id="tocS_201">201</h2>
<!-- backwards compatibility -->
<a id="schema201"></a>
<a id="schema_201"></a>
<a id="tocS201"></a>
<a id="tocs201"></a>

```json
{
  "success": "Successfully registered a new user.",
  "username": "<username>",
  "email": "<email>",
  "token": "<token>"
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|success|string|false|none|none|
|username|string|false|none|none|
|email|string|false|none|none|
|token|string|false|none|none|

