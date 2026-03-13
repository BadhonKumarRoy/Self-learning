function toggleLight() {
  const img = document.getElementById("image");

  if (img.src.includes("pic_bulboff")) {
    img.src = "../images/pic_bulbon.gif";
  } else {
    img.src = "../images/pic_bulboff.gif";
  }
}