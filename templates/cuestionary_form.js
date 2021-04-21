const formValues = $('#cuestionary').serialize();
    $.post("/handle_answers", formValues, resultHandler);

$("cuestionary").on("submit", formValues(evt){
    evt.preventDefault():
    console.log( $("input").serialize());
});