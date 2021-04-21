var userData = {
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

  // var x = "<table>" //create the table
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
  // x += "<tr><th>ID</th><th>NAME</th><th>PASSWORD</th><th>EMAIL</th><th>SCHOOL EMAIL</th><th>DISTANCE</th><th>LOCATION</th><th>MAJOR</th><th>BIO</th><th>IMAGE-LINK</th><th>CLASSIFICATION</th><th>BIRTHDATE</th><th>GENDER</th></tr>"

var table = document.getElementById("srp-table");
var allUsers = userData.users;
for(i in allUsers){
  var data = allUsers[i];
  var userEntry = document.createElement("div");
  userEntry.className = "user-entry";
  var contentHldr = document.createElement("div");
  contentHldr.className = "content-holder";
  var imgHldr = document.createElement("div");
  imgHldr.className = "img-holder";
  var pfp = document.createElement("img");
  pfp.src = "./assets/pfp.jpg";
  var userName = document.createElement("h2");
  userName.innerHTML = data["Name"];
  var userBio = document.createElement("p");
  userBio.innerHTML = data["Bio"];
  var tagDiv = document.createElement("div");
  tagDiv.className = "tags";
  var majorTag = document.createElement("div");
  majorTag.className = "tag";
  var userMajor = document.createElement("p");
  userMajor.innerHTML = data["Major"];

  majorTag.appendChild(userMajor);
  tagDiv.appendChild(majorTag);
  contentHldr.appendChild(userName);
  contentHldr.appendChild(userBio);
  contentHldr.appendChild(tagDiv);
  imgHldr.appendChild(pfp);
  userEntry.appendChild(imgHldr);
  userEntry.appendChild(contentHldr);
  table.appendChild(userEntry);
}
  
// Get the modal
var modal = document.getElementById("myModal");

// Get the button that opens the modal
var btn = document.getElementById("floatBtn");

// Get the <span> element that closes the modal
var span = document.getElementsByClassName("close")[0];

// When the user clicks on the button, open the modal
btn.onclick = function() {
  modal.style.display = "block";
}

// When the user clicks on <span> (x), close the modal
span.onclick = function() {
  modal.style.display = "none";
}

// When the user clicks anywhere outside of the modal, close it
window.onclick = function(event) {
  if (event.target == modal) {
    modal.style.display = "none";
  }
}