"use strict";
$(document).ready(function() {
$("#mywishes #checked").submit(function () {
    if($("mywishes #checked").is(':checked')) {
        $("#mywishes input[type=checkbox]").each(function () {
            $(this).prop("checked", true);
        });
    } else {
        $("#mywishes input[type=checkbox]").each(function () {
            $(this).prop("checked", false);
        });
    }
    });
    
    const button = $('#love-button');
        button.on('submit', () => {
            alert('Brownie Points!');
        });

