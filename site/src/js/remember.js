$(document).ready(function(){
    $("a").click(function(){
        $(this).addClass("disabled");
    });
    $("#reset").click(function(){
        $(".disabled").removeClass("disabled");
    });
});