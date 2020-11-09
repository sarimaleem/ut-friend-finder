var hey = {
    "status": "pass",
    "users": [
      {
        "id": 3,
        "Name": "gabby something",
        "Password": "sdjfladksj;f",
        "Email": "hello@gmail.com",
        "School email": "myboi@utexas.org",
        "distance" : 4,
        "Location": "(Location object)",
        "Major": "Computer Science",
        "Bio": "OMG hey!!! they call me jay jay",
        "image-link": "/image.png",
        "Classification": "Sophmore",
        "Birthdate": "DateTime()",
        "Gender": "male"
      },
      {
        "id": 2,
        "Name": "angelo cullocatta (sorry)",
        "Password": "43042jdfjsdkl3u4$#_d",
        "Email": "myboi@gmail.com",
        "School email": "myboi@utexas.org",
        "Distance": 7,
        "Location": "(Location object)",
        "Major": "Computer Science",
        "Bio": "OMG hey!!! they call me jay jay",
        "image-link": "/image.png",
        "Classification": "Sophmore",
        "Birthdate": "DateTime()",
        "Gender": "male"
      }
    ]
  }

  var x = "<table>" //create the table
  /* <tr>
          <th>ID</th>
          <th>NAME</th>
          <th>PASSWORD</th>
          <th>EMAIL</th>
          <th>SCHOOL EMAIL</th>
          <th>DISTANCE</th>
          <th>LOCATION</th>
          <th>MAJOR</th>
          <th>BIO</th>
          <th>IMAGE-LINK</th>
          <th>CLASSIFICATION</th>
          <th>BIRTHDATE</th>
          <th>GENDER</th>
        </tr> */

  //add the header (labels)
  x += "<tr><th>ID</th><th>NAME</th><th>PASSWORD</th><th>EMAIL</th><th>SCHOOL EMAIL</th><th>DISTANCE</th><th>LOCATION</th><th>MAJOR</th><th>BIO</th><th>IMAGE-LINK</th><th>CLASSIFICATION</th><th>BIRTHDATE</th><th>GENDER</th></tr>"

  for(i in hey.users){

    x += "<tr>" //for each user, create a new row
    var user = hey.users[i];
    var keys = Object.keys(user) //get list of all data stored (name, id, etc)

    for(j in keys){
      x += "<th>"+(user[keys[j]])+"</th>" //get the info for each key
    }
    x += "</tr>"
  }
  x += "</table>"

  document.body.innerHTML += x; //append to the doc
  console.log(x)