const BASEURL = "http://localhost:64190";

const handleImageUpload = (event) => {
  document.querySelector(".result .msg").innerHTML = "";
  const files = event.target.files;
  const formData = new FormData();
  formData.append("file", files[0]);

  fetch(BASEURL + "/api/uploadfile", {
    method: "POST",
    body: formData,
  })
    .then((res) => {
      return res.json();
    })
    .then((data) => {
      document.querySelector('.oriimgcontainer').innerHTML = ''
      document.querySelector(".result .msg").innerHTML =
        "Upload success, please select style you want from left panel";
      localStorage.setItem("filename", data.filename);
      var img = document.createElement("IMG")
      img.setAttribute('src', 'temp_image/' + data.filename)
      document.querySelector('.oriimgcontainer').appendChild(img)
    })
    .catch((error) => {
      console.error(error);
    });
};

document.querySelector("#upload_file").addEventListener("change", (event) => {
  handleImageUpload(event);
});

var styles = [
  { url: "640.jpg" },
  { url: "44296041_16.jpg" },
  { url: "44296041_24.jpg" },
  { url: "44296041_30.jpg" },
  { url: "44296041_39.jpg" },
  { url: "claborate6.jpg" },
  { url: "fuchun3_1.jpg" },
  { url: "shanshui19.jpg" },
  { url: "shuimo22.jpg" },
  { url: "xishan_linmo1.jpg" },
  { url: "xishan_linmo4.jpg" },
];

window.onload = function () {
  styles.forEach((element) => {
    var div = document.createElement("div");
    div.classList.add("styleimage");
    var img = document.createElement("IMG");
    img.setAttribute("src", "style/" + element["url"]);
    img.addEventListener("click", function () {
      var similarity = document.querySelector(".similarity input").value;
      if (similarity == "") {
        similarity = "25";
      }
      style_id = element["url"];
      fetch(
        BASEURL +
          "/api/getimage?filename=" +
          localStorage.getItem("filename") +
          "&style=" +
          style_id +
          "&similarity=" +
          similarity,
        {
          method: "GET",
        }
      )
        .then((res) => {
          return res.json();
        })
        .then((data) => {
          console.log(data);
          var img = document.createElement("IMG");
          img.setAttribute("src", "temp_image/" + data.imagepath);
          // img.setAttribute('src', 'temp_image/' + 'b7378dc65b79613b912f3313a2fe1ec5.png')
          document.querySelector(".result .imgcontainer").innerHTML = "";
          document.querySelector(".result .imgcontainer").appendChild(img);
        });
    });
    div.appendChild(img);
    document.querySelector(".style_panel").appendChild(div);
  });
};
