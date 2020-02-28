# Exam Topics

## 1.0 Software Development and Design (15%)

### 1.1 Compare data formats (XML, JSON, YAML)

- YAML (YAML Aint Markup Language)
  - Great for configuration files
  - Uses indentation to define data structure, similar to how Python structures code.
  - Purposefully made to be easy for humans to read/write
  - Allows commenting
  - YAML Example:

  ``` yaml
    --- # Authors And Books
    authors:
      -
        first_name: Madeleine
        last_name: L'Engle
        books:
            -
              title: A Wrinkle In Time
              publisher: Ariel Books
              genres:
                -  Young Adult
                -  Science Fantasy
              pages: 218
              publish_date: 1962-01-01
              description: A Wrinkle in Time is the story of Meg Murry, a high-school-aged girl who is transported on an adventure through time and space with her younger brother Charles Wallace and her friend Calvin O'Keefe to rescue her father, a gifted scientist, from the evil forces that hold him prisoner on another planet.
  ```

- JSON (JavaScript Object Notation)
  - Great for serialized data -- communication between APIs
  - Fairly easy to read. A little more difficult to write correctly.
  - Uses {} to denote objects, [] to denote arrays, etc. More "programmatical" in nature.
  - JSON Example:

  ``` json
  {
    "authors": [
      {
        "first_name": "Madeleine",
        "last_name": "L'Engle",
        "books": [
            {
                "title": "A Wrinkle In Time",
                "publisher": "Ariel Books",
                "genres": [
                    "Young Adult",
                    "Science Fantasy"
                ],
                "pages": 218,
                "publish_date": "1962-01-01",
                "description": "A Wrinkle in Time is the story of Meg Murry, a high-school-aged girl who is transported on an adventure through time and space with her younger brother Charles Wallace and her friend Calvin O'Keefe to rescue her father, a gifted scientist, from the evil forces that hold him prisoner on another planet."
            }
        ]
      }
    ]
  }
  ```

- XML (eXtensible Markup Language)
  - Uses tags, angle brackets, etc
  - Not as common with modern APIs
  - Extremely verbose. More difficult to read and write.
  - XML Example:

  ``` xml
    <?xml version="1.0" encoding="UTF-8" ?>
    <root>
      <authors>
        <first_name>Madeleine</first_name>
        <last_name>L&#x27;Engle</last_name>
        <books>
        <title>A Wrinkle In Time</title>
        <publisher>Ariel Books</publisher>
        <genres>Young Adult</genres>
        <genres>Science Fantasy</genres>
        <pages>218</pages>
        <publish_date>1962-01-01T00:00:00.000Z</publish_date>
        <description>A Wrinkle in Time is the story of Meg Murry, a high-school-aged girl who is transported on an adventure through time and space with her younger brother Charles Wallace and her friend Calvin O&#x27;Keefe to rescue her father, a gifted scientist, from the evil forces that hold him prisoner on another planet.</description>
        </books>
      </authors>
    </root>
  ```

### 1.2 Describe parsing of common data format to Python data structures

#### Parse YAML in Python

``` python

import yaml # Need to install pyyaml

with open('authors.json') as authors_file:
    data=authors_file.read()

authors_json = yaml.safe_load(data)
authors = authors_json['authors']

print(f'Number of Authors: {len(authors)}')
for author in authors:
    print(f'Author Name: {author["first_name"]} {author["last_name"]}')
    books = author["books"]
    for book in books:
        print(f'Title: {book["title"]}')
        print(f'Pages: {book["pages"]}')
        print(f'Description: {book["description"]}')

```

#### Parse JSON in Python

``` python

import json

with open('authors.json') as authors_file:
    data=authors_file.read()

authors_json = json.loads(data)
authors = authors_json['authors']

print(f'Number of Authors: {len(authors)}')
for author in authors:
    print(f'Author Name: {author["first_name"]} {author["last_name"]}')
    books = author["books"]
    for book in books:
        print(f'Title: {book["title"]}')
        print(f'Pages: {book["pages"]}')
        print(f'Description: {book["description"]}')

```

#### Parse XML in Python

``` python

from xml.dom.minidom import parse

domTree = parse('authors.xml')
root = domTree.documentElement

authors = root.getElementsByTagName('authors')
print(f'Number of Authors: {len(authors)}')
for author in authors:
    firstName = author.getElementsByTagName('first_name')[0]
    lastName = author.getElementsByTagName('last_name')[0]
    print(f'Author Name: {firstName.firstChild.data} {lastName.firstChild.data}')
    books = author.getElementsByTagName('books')
    for book in books:
        title = book.getElementsByTagName("title")[0]
        pages = book.getElementsByTagName("pages")[0]
        descr = book.getElementsByTagName("description")[0]
        print(f'Title: {title.firstChild.data}')
        print(f'Pages: {pages.firstChild.data}')
        print(f'Description: {descr.firstChild.data}')

```

### 1.3 Describe the concepts of test-drive development

> Test-driven development (TDD) is a software development process that relies on the repetition of a very short development cycle: requirements are turned into very specific test cases, then the software is improved so that the tests pass. This is opposed to software development that allows software to be added that is not proven to meet requirements. - [Wikipedia Link](https://en.wikipedia.org/wiki/Test-driven_development)

TDD is usually looked at through a lens of strict "Write Tests Before Code". This is a good practice to try and adhere to, but some people just don't work that way. The primary goal of TDD is that the vast majority of your code has tests that prove your code works the way that it should -- and that any changes to one part of your code do not have consequences to other parts of your code you don't catch immediately. So it doesn't matter (to me) whether you write tests or code first, as long as you write tests.

### 1.4 Compare software development methods (agile, lean, waterfall)

- Agile:
  - Flexibility focused.
  - Allows for evolution of the product as it is being worked on
  - Work is performed in short planned phases (i.e. every 2-3 weeks)
    - The goal of each iteration to provide a working product.
    - Tests must pass at the end of each cycle
    - Stakeholders get updated at the end of each cycle and may provide feedback
      - Changes may be incorporated from feedback in the next phase
  - Downside: The openness to change may result in fluxuating timelines
- Waterfall:
  - Development doesn't start until all planning is done
  - Sequential and Linear development cycle
  - Longer development cycles between producing updates
  - Inflexible -- Very hard to make changes in the middle of a dev cycle
  - Lacks visibility. I.e. fewer check-ins / updates
  - Upside: Since scope is known ahead of time:
    - Timelines tend to be more stable
    - Progress is more easily measured against an end goal
- Lean
  - Focused on producing an MVP as quickly as possible.
  - Can "fail fast" from a business perspective.
    - i.e. Are you building the right product? Allows you to abandon early if you aren't.
  - Reduce project delivery time and cost while delivering to a specific set of minimum requirements
  - Downside: Little effort and time is spent considering the future needs of the application.

### 1.5 Explain the benefits of organizing code into methods/ functions, classes, and modules

The primary purposes for organizing code are reusability, testability, and refactoring.

Consider this piece of code:

``` python
people = [
    {
        "firstName": "John",
        "lastName": "Carpenter",
        "occupation": "Director"
    },
    {
        "firstName": "Madeleine",
        "lastName": "L'Engle",
        "occupation": "Author"
    }
]

print(f'{people[0]["firstName"]} {people[0]["lastName"]}')
print(f'{people[1]["firstName"]} {people[1]["lastName"]}')
```

So we have an array of "anonymous" objects. i.e. the structure is unclear, you won't get intellisense when working on it.

We'll improve this a little at a time, starting with methods/functions:

``` python
def getFullName(person):
    return f'{person["firstName"]} {person["lastName"]}'

people = [
    {
        "firstName": "John",
        "lastName": "Carpenter",
        "occupation": "Director"
    },
    {
        "firstName": "Madeleine",
        "lastName": "L'Engle",
        "occupation": "Author"
    }
]

print(getFullName(people[0]))
print(getFullName(people[1]))
```

This time instead of repeating the same structure of code to produce a full name, we extracted it into a function. A piece of code that we can reuse over and over again to produce the same result. And if something needs to be changed we only need to change it in one place. Not 2 or more.

But there is still some improvement to be had here. For instance, what happens if we sent in an object that didn't have a firstName and a lastName? It would break. That's an extremely fragile piece of code. Lets see what a class can do for us here:

``` python

class Person:
  def __init__(self, firstName, lastName, occupation):
    self.firstName = firstName
    self.lastName = lastName
    self.occupation = occupation

  def getFullName(self):
      return f'{self.firstName} {self.lastName}'

people = []
people.append(Person('John', 'Carpenter', 'Director'))
people.append(Person('Madeleine', "L'Engle", 'Author'))

print(people[0].getFullName())
print(people[1].getFullName())

```

Ahhh... Now we're getting somewhere. We have a class named person with a constructor that takes a firstName, a lastName, and an occupation. So if we were to do people[0] and put a period, we would get intellisense showing us options available on this type of object.

Then we moved our getFullName() function inside that class. So every person object now has a method to get the fullname of that person. MUCH cleaner! And reuseable! And testable! We only have to test whether the Person class and its methods work correctly. If they don't we can fix it all in one place.

As far as modules go, they're more for separating classes, functions, and values into groups that make sense. i.e. you might make one module that handles logging, so you can import it into any other python file you're using. Or you might create a module that has all the methods for talking to an API. And then you could have a main python file that imports the API module and the logging module. And you'd know exactly what each is for because the logic is separated based on responsibility.

### 1.6 Identify the advantages of common design patterns (MVC and Observer)

#### MVC or Model-View-Controller

This is a pattern used in many languages -- it is for the use of applications with a GUI.

- Model: Your data structures and potentially business logic. Though it may just be used to get data from a database.
- View: What your user sees
- Controller: The glue between your model and your view. It gets data from the model to be shown to the user, and sends data from the view to the model layer to be saved to databases etc.

#### Observer Pattern

The simplest way I can think of to describe the observer pattern is: What if you had an editable table of data on a screen, and to the left of that data you had a chart based on that data. Every time you update the data in the table you'd expect the graph to change right? That's exactly the kind of problem that the Observer pattern is a solution for.

It quite literally "observes" an object that other objects rely on. And when that object's state changes, the observer says "Hey, you over there, this object you rely on just changed." Then those other objects can be update based on the object's new state.

#### Why Patterns

People have been programming for a long time. And it's very common for programmers to run into the same problems that other people have run into. It's the reason things like StackOverflow exist. Patterns were created to help remedy the most common "big" problems. So it's beneficial to learn common design patterns so that you can use proven solutions instead of banging your head against the wall trying to solve design issues on your own.

### 1.8 Utilize common version control operations with Git

#### Git Clone

``` git
git clone [url]
```

- **Example:** ```git clone git@github.com:FooBartn/WxTeamsSharp.git```
- **Purpose:** retrieve an entire repository from a hosted location via URL

#### Git Add/Remove

``` git
git add [file]
```

- **Example**: ```git add parsejson.py```
- **Purpose**: Add a file as it looks now to your next commit. Also known as Staging. Using ```git add .``` will add/stage all new and modified files. ```git add -A``` will stage all new, modified, and deleted files

#### Git Commit

``` git
git commit -m “[descriptive message]”
```

- **Purpose**: Commit your staged content as a new commit snapshot

#### Git Push / Pull

``` git
git push [alias] [branch]
```

- **Example**: ```git push origin master``` <-- Push the local master branch to remote named origin
- **Purpose**: Transmit local branch commits to the remote repository branch

``` git
git pull
```

- **Purpose**: Fetch and merge any commits from the tracking remote branch

#### Git Branch

``` git
git branch
```

- **Purpose**: List your branches. a * will appear next to the currently active branch

``` git
git branch [branch-name]
```

- **Purpose**: Create a new branch at the current commit

``` git
git checkout [branch]
```

- **Purpose**: Switch to another branch and check it out into your working directory

``` git
git checkout -b [branch]
```

- **Purpose**: Create another branch, switch to it, and check it out into your working directory

### Git Merge and handling conflicts

``` git
git merge [branch]
```

- **Purpose**: Merge the specified branch’s history into the current one

``` git
git status
```

- **Purpose**: One of the primary purposes is to list out any any files affected by merge conflicts.

> For more detail on resolving merge conflicts see [Git-Tower: Merge Conflicts](https://www.git-tower.com/learn/git/ebook/en/command-line/advanced-topics/merge-conflicts)

#### Git Diff

``` git
git diff
```

- **Purpose**: Diff of what is changed but not staged

``` git
git diff --staged
```

- **Purpose**: Diff of what is staged but not yet commited

## 2.0 Software Development and Design (20%)

### Construct a REST API request to accomplish a task given API documentation

#### HTTP Verbs / Actions

- **POST**: Create
- **GET**: Read
- **PUT**: Update
- **PATCH**: Update
- **DELETE**: Delete

#### Reading API Documentation

Let's take a look at one of my favorite little APIs: [ICanHazDadJoke API](https://icanhazdadjoke.com/api)

The documentation states that I do not need Authentication, and that it will adjust its return output based on the Accept headers we send in. It will return text/html by default.

The API states that the main endpoint is this:

``` na
GET https://icanhazdadjoke.com/ fetch a random dad joke.
```

Notice that the first part of this says GET. API documentation will let you know the correct verb to use to interact with that endpoint.

So lets try to get a Dad joke using Python's requests library!

``` python
import requests

response = requests.get('https://icanhazdadjoke.com/')
joke = response.content
print(joke)
```

Oh... if we do that, we get back a whole HTML page! Remember, the default return is text/html. This is so you can browse to 'https://icanhazdadjoke.com' and you will see a nicely formatted joke in your browser.

Alright, so what to do to get JSON? We need to change our Accept header to tell the API what kind of response we want back.

``` python

import requests

url = 'https://icanhazdadjoke.com/'
headers = {
    'Accept': 'application/json'
}
response = requests.get(url, headers=headers)
joke = response.json()
print(joke)

```

Ah! Much better. Now we get json back that looks something like this:

``` json
{
    "id": "pzXvHl3EYg",
    "joke": "Why don’t seagulls fly over the bay? Because then they’d be bay-gulls!",
    "status": 200
}
```

And if you run it again you'll get a different joke. But what if I wanted a specific joke?

There is another endpoint that says:

``` na
GET https://icanhazdadjoke.com/j/<joke_id> fetch a specific dad joke.
```

See in the json above, each joke also comes with an ID. You can use this to refer to a specific joke.

``` python

import requests

url = 'https://icanhazdadjoke.com/j/ukOCYoWDQuc'
headers = {
    'Accept': 'application/json'
}
response = requests.get(url, headers=headers)
joke = response.json()
print(joke)

```

This particular ID should result in the joke: My sea sickness comes in waves. I love it.

There's even a search endpoint. And this one is a good one to check out, because it uses query parameters. Query parameters are those things you see after the ? in a URL.

The endpoint is this:

``` na
GET https://icanhazdadjoke.com/search - search for dad jokes.
```

And the API states that the endpoint accepts these query parameters:

``` na
page - which page of results to fetch (default: 1)
limit - number of results to return per page (default: 20) (max: 30)
term - search term to use (default: list all jokes)
```

Hmm.. Let's try searching for a joke about dogs. But we only want it to return 5 results per page.

``` python
import requests

url = 'https://icanhazdadjoke.com/search'
headers = {
    'Accept': 'application/json'
}
params = {
    'term': 'dog',
    'limit': '5'
}
response = requests.get(url, headers=headers, params=params)
joke = response.json()
print(joke)
```

And that returned:

``` json
{
    "current_page": 1,
    "limit": 5,
    "next_page": 2,
    "previous_page": 1,
    "results": [
        {
            "id": "EBQfiyXD5ob", 
            "joke": "what do you call a dog that can do magic tricks? a labracadabrador"
        },
        {
            "id": "DIeaUDlbUDd",
            "joke": "“My Dog has no nose.” “How does he smell?” “Awful”"
        }
        // and more jokes..
    ],
    "search_term": "dog",
    "status": 200,
    "total_jokes": 12,
    "total_pages": 2
}
```

Whoa. That's way more than just jokes. We've got current_page, limit, next_page, previous_page, search_term, total_jokes, total_pages... 

Remember there was a 3rd query parameter available for the endpoint called page? If we called this same endpoint but used the query paramter ```'page': 2``` we'd get the second page of results. Try it out on your own!

### Describe common usage patterns related to webhooks

APIs are wonderful. You ask them for information, they give it to you. But what if that information changes all the time, and your application relies on up-to-date data?

Well, you just query it more often right? Maybe. But most APIs have a rate-limit. After a certain number of requests per second or minute they tell you "Whoa, slow down." by denying your request and usually sending a header along to tell you how long your timeout is for.

"But I need the new data as soon as it changes!!", you say. In comes the webhook to save the day, IF the API you're working with has made them available.

Instead of relying on you asking for more information, you register a link to an API of your own that is capable of receiving a POST request. This tells the API you need information from -- "Hey, everytime this data changes **YOU** send **ME** an update!". When the data changes, the API sees your registered webhook and sends a POST request to your API with the new data. Voila! No more sending GET requests every 5 seconds to the API!

### Identify the constraints when consuming APIs

I'm not entirely sure what they're looking for here, but my guess is things like:

- How often you can make a request of the API before it gives you back a 429 TooManyRequests response
- What type of authentication is required to use the API
- How many requests you can make in any given time period (day,week,month) before you hit your limit

### Explain common HTTP response codes associated with REST APIs

- **200** OK: All looks good
- **201** Created: New resource created
- **400** Bad Request: Request was invalid
- **401** Unauthorized: Authentication missing or incorrect
- **403** Forbidden Request: was understood but not allowed
- **404** Not Found: Resource not found
- **500** Internal Server Error: Something wrong with the server
- **503** Service Unavailable: Server is unable to complete request

### Troubleshoot a problem given the HTTP response code, request and API documentation

We'll take a look at a slightly more "professional" API than ICanHazDadJoke this time around. Let's check out the [Webex Teams API: Basics](https://developer.webex.com/docs/api/basics)

Scroll down to the API Errors section. You should see a table like this:

| Code | Status       | Description                                                                                               |
|------|--------------|-----------------------------------------------------------------------------------------------------------|
| 200  | OK           | Successful Request                                                                                        |
| 204  | No Content   | Successful request without body content                                                                   |
| 400  | Bad Request  | The request was invalid or cannot be otherwise served. An accompanying error message will explain further |
| 401  | Unauthorized | Authentication credentials were missing or incorrect                                                      |

Most APIs will have information like this to let you know what went wrong and how to handle it.

> Note: If you see an error message in the 50x range, you're all outta luck. Those are server issues and the only thing you can do is send a message to the owners of that API and hope they fix it.

### Identify the parts of an HTTP response (response code, headers, body)

![Cisco REST Infographic](https://developer.cisco.com/learning/posts/files/what-are-rest-apis/assets/images/request-response.png) - From [Cisco DevNet: What are REST APIs?](https://developer.cisco.com/learning/lab/what-are-rest-apis/step/1)

### Utilize common API authentication mechanisms: basic, custom token, and API keys

**Most** APIs have some sort of authentication, even if it's just to keep track of who is doing what so abusers can be caught. Not many are as open as the ICanHazDadJoke API, where its only request is that if you're using it from an application of your own (as opposed to just playing around with it) you put the application name in the User-Agent header so they can tell where it's coming from.

The most common form of this that I see is an API Key. You register for a service, agree to all the terms, and they give you an API key that is strictly for your account. You then put that in the header of every request you make. I.e. if ICanHazDadJoke did require an API key, the request might look like this:

``` python
import requests

url = 'https://icanhazdadjoke.com/search'
headers = {
    'Accept': 'application/json',
    'Authorization': 'Bearer 235235235xyz'
}
params = {
    'term': 'dog',
    'limit': '5'
}
response = requests.get(url, headers=headers, params=params)
joke = response.json()
print(joke)
```

You also have Basic Authentication, Digest Authentication, and OAuth (1 and 2) Authentication.

Basic authentication is the simplest. And the least secure. You send the username and password over plain text. So if it's done, it really should be done using Transport Layer Security (TLS) -- i.e. it should use https, not http. In Python it looks like this:

``` python
requests.get('https://api.github.com/user', auth=HTTPBasicAuth('user', 'pass'))
```

Digest Authentication is very similar to Basic, except that it encrypts the data with a hash instead of sending it in plain text. So even though TLS is always preferred, in this case it's not as risky.

``` python
requests.get('https://api.github.com/user', auth=HTTPDigestAuth('user', 'pass'))
```

OAuth is the most common form of authentication if you're authenticating on behalf of other users. Think of an app that you've signed up for that was 3rd party for a large service. Or when you use a Facebook account to authenticate with a non-Facebook service. When you sign up, you've probably seen a page that says "This application would like to access your account with these privileges: Read your username, Read your email, etc". That's the Oauth workflow at work!

It basically goes like this:
Your app has a Client Id and probably a Client Secret, along with a redirect URI (where to go back to once a user has authenticated). You also specify a scope of rights your app should have.

Whenever a user wants to authenticate, you send them to the API services Oauth url with the parameters we talked about in the paragraph above. They will get a message like "FooBarton's app would like to access your profile". If they click accept, their service uses the redirect URI to send them back to your page along with a special code. Your app then uses that code to make a **second** request to a different endpoint to get a token with that code. That token is then good for a set amount of time before it must be renewed or the user must re-authenticate.

To see more about how to use Oauth with Python, check out [requests-oauthlib](https://requests-oauthlib.readthedocs.io/en/latest/oauth2_workflow.html)

### Compare common API styles (REST, RPC, synchronous, and asynchronous)


#### REST and RPC

REST, which has become the most popular form of communication with APIs has rules and standards that help making talking to any API a near-ubiquitous experience. If you've done a GET with one REST API that returns JSON, you've done them all. This allows an API to last for a very long time without needing to be changed.

Some of the restrictions REST API developers are supposed to follow:

- REST must be stateless: not persisting sessions between requests.
- Responses should declare cacheablility: helps your API scale if clients respect the rules.
- REST focuses on uniformity: if you’re using HTTP you should utilize HTTP features whenever possible, instead of inventing conventions.

> See all 6 architectural constraints described [here](https://restfulapi.net/rest-architectural-constraints/)

REST APIs will commonly use all of the available HTTP verbs for a given endpoint to allow you to do CRUD-based (Create, Read, Update, Delete) operations. GET, POST, PUT, DELETE, PATCH

And these can take data payloads in the form of JSON, or query parameters like we used previously to modify the request

RPC stands for "Remote Procedure Call". Think of it like calling a python function. An RPC API is a list of functions available to call where you give it the name of the function and the argument/parameter for it. And these APIs typically only serve GET or POST requests.

One of the big differences is that, with RPC, *everything* is a separate function.

Say you have a person directory. If you want to get people by first name you might do:

```
POST /getPersonByFirstName
Content-Type: application/json

{"firstName": "Elliot"}
```

But if you wanted to get people by last name:

```
POST /getPersonByLastName
Content-Type: application/json

{"lastName": "Baker"}
```

Two different endpoints to get the same type of object, just by a different value. In comparison, you'd probably see this for a REST API

```
GET /getPerson?lastName=Baker
GET /getPerson?firstName=Elliot
```

Same API endpoint, just with a different query parameter.

In this regard, REST is usually seen as the best way to deal with CRUD, while RPC is more action based.

Slack uses an RPC api because things like kick, ban, etc don't really fit well in the GET, POST, PUT, DELETE, PATCH semantics. In REST you expect that GET is for reading, POST is for adding new things, etc. Where do kick and ban fit in? You could make them, for sure. But when you start shoehorning REST with RPC-style actions, it gets a little confusing. Not just for developers, but for users who expect your REST API to act just like a REST API.

#### Synchronous and Asynchronous

The easiest way to think of synchronous and asynchronous is that synchronous is synonomous with the wait symbol (hourlgass, spinner, etc). You know when you go to a website and it sits there with a spinner in the browser tab? That's a synchronous operation. You have to wait for it, and while you're waiting the app (or webpage) is stalled.

An asynchronous operation is one that you do not have to wait for directly. Let's say, for instance, that you make an RPC call to configure and deploy a new server. And that operation will take 10 minutes. Do you want your app to make that call and then sit there locked up for 10 minutes waiting for it to finish? (synch)

Or do you want to make that call and let a webhook notify you whenever it's done. And in the meantime your user is still able to use the app to look at other things. (async)

Or maybe you want to GET a list of all your transactions for the last 20 years. And this will take 30 minutes to complete. You could send a request to the API with your email address and it could send you an email with a link to your download when it's ready. But you didn't have to sit there waiting 30 minutes. You can go do other things. (async)

As with REST and RPC, Synchronous and Asynchronous APIs have their uses!

### Construct a Python script that calls a REST API using the requests library

We've done a few of these ^___^

## 3.0 Cisco Platforms and Development (15%)
