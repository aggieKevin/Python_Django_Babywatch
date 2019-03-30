function myFunction(clicked_id) {
      var ds_1 = document.getElementById("contact");
      var ds_2 = document.getElementById("child");
      var ds_3 = document.getElementById("pass");
      var ds_4 = document.getElementById("preferences");
      ds_1.style.display = "none";
      ds_2.style.display = "none";
      ds_3.style.display = "none";
      ds_4.style.display = "none";

    if(clicked_id =="preflink")
    {
      var show = document.getElementById("preferences");
      show.style.display = "block";
    }
    else if(clicked_id == "contactlink")
    {
      var show = document.getElementById("contact");
      show.style.display = "block";
    }
    else if(clicked_id == "childlink")
    {
      var show = document.getElementById("child");
      show.style.display = "block";
    }
    else if(clicked_id == "passlink")
    {
      var show = document.getElementById("pass");
      show.style.display = "block";
    }
}