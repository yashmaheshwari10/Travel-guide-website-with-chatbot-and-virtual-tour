$(".outline").on('click', function(e){
  e.preventDefault();
  let id = $(this).attr("name");
  if (id === "login") {
    $("form").animate({
      "right": null,
      "left": "440px"
    }, "swing");
		$("input[name*='Name']").fadeOut("slow").slideUp("slow");
		$(".formButton").text('Login');
  } else if (id === "signup") {
    $("form").animate({
      "left": null,
			"right": "440px"
    });
		$("input[name*='Name']").fadeIn("slow").slideDown("slow");
		$(".formButton").text('Sign Up');
  }
});