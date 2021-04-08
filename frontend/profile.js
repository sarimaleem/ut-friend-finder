var info = {
  first: "Bob",
  last: "Bill",
  bio:
    "hello, my name is bob the builder and I am from pakistan. I really like making buildings. In my free time I read books and don't study but also watch a lot of tv. I really like food because every one likes food. One of my hobbies is that I really like to bake which is always somewhat nice I suppose",
};

var socials = {
  discord: "bob#123",
  facebook: "bobthebuilder",
  snapchat: "bobthebuilderyeswecan",
};

document.getElementById("name").innerText = info.first + " " + info.last;
document.getElementById("bio").value = info.bio;

Object.keys(socials).map((key, _) => addsocial(key, socials[key]))

function save() {
  // document.getElementById("bio") = bio.value;
  // document.getElementById("bio").disabled = true;
  let bioButton = document.getElementById("bioButton");
  document.getElementById("bio").style.borderWidth = 0;
  bioButton.style.display = "none";
  // push to the backend
  // do stuff
}

function addsocial(socialName, socialUsername) {
  let socialContainer = document.createElement("div");
  let description = document.createElement("span");
    description.innerHTML = socialName + " " + socialUsername;

  socialContainer.classList.add("social-container");
  socialContainer.appendChild(description);
  let button = document.createElement("button");
  button.innerHTML = "X";
  button.onclick = deletesocial;
  socialContainer.appendChild(button);
  document.getElementById("socialsList").appendChild(socialContainer);
}

function appendSocial() {
    let socName = document.getElementById("socialName").value;
    let socUser = document.getElementById("socialUsername").value;

    addsocial(socName, socUser);
}

function deletesocial() {
    parentnode = this.parentNode;
    parentnode.parentNode.removeChild(parentnode);
}

function edit() {
  bioButton.style.display = "block";
  bio = document.getElementById("bio");
  document.getElementById("bio").style.borderWidth = 1;
}
