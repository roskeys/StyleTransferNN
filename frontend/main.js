const handleImageUpload = (event) => {
  document.querySelector(".result .msg").innerHTML = "";
  const files = event.target.files;
  const formData = new FormData();
  formData.append("file", files[0]);

  fetch("http://localhost:8000/uploadfile", {
    method: "POST",
    body: formData,
  })
    .then((res) => {
      return res.json();
    })
    .then((data) => {
      document.querySelector(".result .msg").innerHTML =
        "Upload success, please select stype you want from left panel";
      localStorage.setItem("filename", data.filename);
    })
    .catch((error) => {
      console.error(error);
    });
};

document.querySelector("#upload_file").addEventListener("change", (event) => {
  handleImageUpload(event);
});

var styles = [
  { url: "44296041_46.jpg" },
  { url: "wuguanzhong_3.jpg" },
  { url: "wuguanzhong_33.jpg" },
  { url: "claborate4.jpg" },
  { url: "44296041_9.jpg" },
];

window.onload = function () {
  styles.forEach((element) => {
    var div = document.createElement("div");
    div.classList.add("styleimage");
    var img = document.createElement("IMG");
    img.setAttribute("src", element["url"]);
    img.addEventListener("click", function () {
      similarity = document.querySelector(".similarity input").value;
      style_id = element["url"];
      fetch(
        "http://localhost:8000/getimage?filename=" +
          localStorage.getItem("filename") +
          "&style=" +
          style_id + '&similarity=' + similarity,
        {
          method: "GET",
        }
      )
        .then((res) => {
          return res.json();
        })
        .then((data) => {
          console.log(data);
          var img = document.createElement('IMG')
          // img.setAttribute('src', '/temp_image/' + data.imagepath)
          img.setAttribute('src', 'temp_image/' + 'b7378dc65b79613b912f3313a2fe1ec5.png')
          document.querySelector('.result .imgcontainer').innerHTML = ''
          document.querySelector('.result .imgcontainer').appendChild(img)
        });
    });
    div.appendChild(img);
    document.querySelector(".style_panel").appendChild(div);
  });
};
