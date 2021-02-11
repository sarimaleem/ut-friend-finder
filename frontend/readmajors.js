let getTxt = function (selectTag) {
  $.ajax({
    url: "majors.txt",
    success: function (data) {
      let majors = data.split("\n");
      for (let i = 0; i < majors.length; i++) {
        let major = majors[i];
        let option = document.createElement("OPTION");
        option.textContent = major;
        selectTag.appendChild(option)
      }
    },
  });
};
let majorSelect = document.getElementById("major")
getTxt(majorSelect);
