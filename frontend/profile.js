var info = {
  first: "Bob",
  last: "Bill",
  bio: "hello, my name is bob the builder and I am from pakistan. I really like making buildings. In my free time I read books and don't study but also watch a lot of tv. I really like food because every one likes food. One of my hobbies is that I really like to bake which is always somewhat nice I suppose",
};

var socials = {
    "discord" : "bob#123",
    "facebook" : "bobthebuilder",
    "snapchat" : "bobthebuilderyeswecan"
}

document.getElementById("name").innerText = info.first + " " + info.last;
document.getElementById("bio").value = info.bio

for (var key of Object.keys(socials)) {
  let obj = document.createElement("p");
  obj.innerHTML = key + ": " + socials[key];
  document.getElementById("socialsList").appendChild(obj);
}

function save() {
  // document.getElementById("bio") = bio.value;
  // document.getElementById("bio").disabled = true;
  let bioButton = document.getElementById("bioButton");
  document.getElementById("bio").style.borderWidth = 0;
  bioButton.style.display = "none";
  // push to the backend
  // do stuff
}

function addsocial() {
  let obj = document.createElement("p");
  obj.innerHTML =
    document.getElementById("socialName").value + " " + 
    document.getElementById("socialUsername").value;
  document.getElementById("socialsList").appendChild(obj);
}

function edit() {
  bioButton.style.display = "block";
  bio = document.getElementById("bio");
  bio.style.width = bio.value.length + "ch";
  document.getElementById("bio").style.borderWidth = 1;
}
