$(document).ready(function() {
  //jquery
  $(".side_menu").hide();
  $(".extra-menu").hide();

  //on event

  //hidden menu
  $(".menu-btn").click(function() {
    $(".side_menu").slideToggle("slow");
  });

  $(".close-btn").click(function() {
    $(".side_menu").slideUp("slow");
  });

  //end
});
