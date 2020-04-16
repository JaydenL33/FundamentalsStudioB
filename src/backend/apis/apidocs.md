# API Documentation 


## Job Searching

```
POST api://jobsearch


body
-----------------------
{
    userid: REQUIRED str ID of user e.g. "clara.franco",
    location: OPTIONAL [str] city names as a string e.g. "Melbourne Sydney"
    incountry: OPTIONAL boolean (overrides location)
    careerlevel: OPTIONAL int career level 
    employeecareerlevelonly: OPTIONAL boolean (overrides careerlevel)
    keywords: OPTIONAL [str] keywords to include in search e.g. "java drones"
    department: OPTIONAL str any accenture group e.g. "Accenture Technology"
    use_favourites OPTIONAL boolean
}


returns     application/json
-----------------------
{
    successful: bool,
    totalhits: int,
    hits: [
        {
            jobid: str,
            title: str,
            description: str,
            location: str,
            startdate: str,
            enddate: str,
            status: str (e.g "open", "closed),
            careerLevelFrom: int, 
            careerLevelTo: int,
            quadrant1: str,
            quadrant2: str,
            department: str
        }
    ]
    
}
```
## Query Favourites

```
POST api://jobsearch


body
-----------------------
{
    userid: REQUIRED str ID of user e.g. "clara.franco"
}


returns     application/json
-----------------------
{
    successful: bool,
    totalhits: int,
    hits: [
        {
            jobid: str,
            title: str,
            description: str,
            location: str,
            startdate: str,
            enddate: str,
            status: str (e.g "open", "closed),
            careerLevelFrom: int, 
            careerLevelTo: int,
            quadrant1: str,
            quadrant2: str,
            department: str
        }
    ]
    
}
```

## Logging in

```
POST api://login

body        application/json
-----------------------
{
    userid: str REQUIRED
    password: str REQUIRED
}

returns     application/json
-----------------------
IF SUCCESSFUL:
{
    successful: bool
    userid: str
}

IF UNSUCCESSFUL:
{
    successful: bool
    message: str
}

```


## Adding favourites

```
POST api://addfavourite

body        application/json
-----------------------
{
    userid: str REQURIED
    jobid: str REQUIRED
}

returns     application/json
-----------------------
{
    userid: str REQURIED
    successful: bool,
}


```

## Remove Favourites

```
POST api://addfavourite

body        application/json
-----------------------
{
    userid: str REQURIED
    jobid: str REQUIRED
}

returns     application/json
-----------------------
{
    userid: str REQURIED
    successful: bool,
}


```



## Get User Info
```

POST api://userinfo

body        application/json
-----------------------
{
    userid: str REQUIRED
}



returns     application/json
-----------------------
{
    successful: bool,
    name: str,
    strengths: list,
    interests: list
}


```

## Set User Info (Set Interest)
```

POST api://modifyInterests

body        application/json
-----------------------
{
    userid: str REQUIRED
    interests: list Optional

}



returns     application/json
-----------------------
{
    successful: bool,
    name: str,
    strengths: list,
    interests: list
}


```

## Adding Favourites (Based off _id of Job)
```

POST api://addFavourite

body        application/json
-----------------------
{
    userid: str REQUIRED
    jobids: str REQURIED

}



returns     application/json
-----------------------
{
    successful: bool,
    _id
}


```
